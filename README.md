# [Basic Auth Django](https://shielded-temple-70406.herokuapp.com)

This is the back-end for `Basic Auth`. This project is built using:
- Django v3, for JWT [DRF simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) is used, 
- for handling CORS [django-cors-headers](https://github.com/adamchainz/django-cors-headers) is used, 
- for exporting data from admin panel [django-import-export](https://django-import-export.readthedocs.io/en/latest/) is used,
- for WSGI HTTP Server [gunicorn](https://gunicorn.org/) is used
- For database PostgreSQL is used,

Following are the features of this project:
- Create account
- Login into your account
- JWT tokens are used for authentication
- IP addresses are captured whenever a user is successfully authenticated;
- Admin panel can be used to download(CSV, JSON, TSV, etc) the users' history

The project is hosted on Heroku, with the following end point [shielded-temple-70406.herokuapp.com](https://shielded-temple-70406.herokuapp.com/). The admin panel can be accessed using [this link](https://shielded-temple-70406.herokuapp.com/admin/login/)


### NOTE 
The front for this app is in seperate repositry [here](https://github.com/jsean662/basic-auth-react) and it is hosted on [basic-auth.jsawant.com](https://basic-auth.jsawant.com)