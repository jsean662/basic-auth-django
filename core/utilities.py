import requests, json
from django.conf import settings
from django.contrib.auth.models import User
from core.models import UserLoginHistory
from rest_framework_simplejwt.tokens import RefreshToken


def createUser(username, password):
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        return True, user
    
    return False, None


def getClientIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def notifyTeamOfIPAddress(ip, user):
    url = settings.__getattr__(settings.ENVIRONMENT)["IP_NOTIFICATION_WEBHOOK"]

    headers = {'Content-Type': "application/json"}
    payload = {
        "user": str(user.id),
        "ip": ip,
    }
    
    # TODO: This can be wrapped in celery function which can then be called asynchronously
    # and with better retry mechanisms
    
    requests.request("POST", url, data=json.dumps(payload), headers=headers)


def saveUsersIPAddress(ip, user):
    history = UserLoginHistory()
    history.ip = ip
    history.userId = user
    history.save()


def notifyTeamAndSaveIPAddress(request, user):
    ip = getClientIP(request)
    saveUsersIPAddress(ip, user)
    notifyTeamOfIPAddress(ip, user)


def getAccessToken(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
