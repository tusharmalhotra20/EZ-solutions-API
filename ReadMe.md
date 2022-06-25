> Dependencies:
- Python interpreter 3.8.3 or above
- Django
- Django Rest Framework
- Virtualenv

> To test API:

1. open cmd in project folder
2. venv\Scripts\activate    
3. run python manage.py runserver

> Note: To test the email verification feature you need to add your own HOST_USER and HOST_PASWORD in authenticaion/settings.py

EMAIL_HOST='smtp-relay.sendinblue.com'   
EMAIL_PORT = 587    
EMAIL_HOST_USER=''    
EMAIL_HOST_PASSWORD='*************'    
