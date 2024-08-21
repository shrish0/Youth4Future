from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_args):
        user=self.model(username=username,**extra_args)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**extra_args):
        extra_args.setdefault('is_staff',1)
        extra_args.setdefault('is_superuser',1)
        extra_args.setdefault('is_active',1)
        return self.create_user(username,password,**extra_args)
    pass