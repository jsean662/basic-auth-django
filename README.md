# [Basic Auth Django](https://shielded-temple-70406.herokuapp.com)

This is the back-end for `Basic Auth` that communicates with the front-end using REST APIs. This project is hosted on [Heroku](https://www.heroku.com/home) using thier free tier \
This project is built using Django v3 along with:
- JWT for authentication [DRF simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- handling CORS [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- exporting data from admin panel [django-import-export](https://django-import-export.readthedocs.io/en/latest/)
- WSGI HTTP Server [gunicorn](https://gunicorn.org/) 
- PostgreSQL is used for database (free tier provided by Heroku)
- Environment variables [python-dotenv](https://pypi.org/project/python-dotenv/)

Following are the features of this project:
- Create account
- Login into your account
- JWT tokens are used for authentication
- IP addresses are captured whenever a user is successfully authenticated;
- Admin panel can be used to download(CSV, JSON, TSV, etc) the users' history
- All the secrets are stored in environment variables

The project is hosted on Heroku, with the following end point [shielded-temple-70406.herokuapp.com](https://shielded-temple-70406.herokuapp.com/). The admin panel can be accessed using [this link](https://shielded-temple-70406.herokuapp.com/admin/login/)


### NOTE 
- The front for this app is in seperate repositry [here](https://github.com/jsean662/basic-auth-react) and it is hosted on [basic-auth.jsawant.com](https://basic-auth.jsawant.com)
- Since this project is hosted on Heroku's free tier, it suffers from cold starts.
