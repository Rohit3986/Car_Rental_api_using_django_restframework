
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from .models import User,LoginLogs

#reciver's function
def login_sucess(sender, request, user, **kwargs):
    print("----------------------------------")
    LoginLogs(user=user,user_type=user.user_type).save()
    print("save ho gya hai bhai ji check kijiye")
    print("--------------------------------------------")
user_logged_in.connect(login_sucess,sender=User)

