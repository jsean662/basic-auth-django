import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utilities import createUser, notifyTeamAndSaveIPAddress, getAccessToken
from django.contrib.auth import authenticate


class HomeView(APIView):
    def get(self, request):
        content = {'message': 'Welcome back {}!'.format(request.user.username)}
        return Response(content)


class UserView(APIView):
    permission_classes = []
    
    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            username = body.get('username', '')
            password = body.get('password', '')
            if not(username and password and len(username) and len(password)):
                return Response(
                        {'status': 'failed', 'message': 'One or more mandatory fields missing'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            isUserCreated = createUser(username, password)
            if isUserCreated:
                return Response({'status': 'success', 'message': 'User created successfuly'})
            else:
                return Response(
                        {'status': 'failed', 'message': 'Username already taken'},
                        status=status.HTTP_403_FORBIDDEN
                    )
        except:
            return Response(
                    {'status': 'failed', 'message': 'Internal server error'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class LoginView(APIView):
    # Disabling the authentication provided by DRF
    permission_classes = []

    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            username = body.get('username', '')
            password = body.get('password', '')
            if not(username and password and len(username) and len(password)):
                return Response(
                        {'status': 'failed', 'message': 'One or more mandatory fields missing'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                notifyTeamAndSaveIPAddress(request, user)
                return Response({
                        'status': 'success', 
                        'message': 'User is authenticated', 
                        "token": getAccessToken(user)
                    })
            return Response(
                    {'status': 'failed', 'message': 'Authentication failed'},
                    status=status.HTTP_403_FORBIDDEN
                )
        except:
            return Response(
                    {'status': 'failed', 'message': 'Internal server error'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )