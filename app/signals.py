
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from .models import User,LoginLogs

#reciver's function
def login_sucess(sender, request, user, **kwargs):
    print("logged in as ",user.username)
    LoginLogs(user=user,user_type=user.user_type).save()
user_logged_in.connect(login_sucess,sender=User)

