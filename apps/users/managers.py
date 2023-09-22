from django.contrib.auth.base_user import BaseUserManager

class CustomeUserManager(BaseUserManager):
    """
    custome user model manager where email is the unique identifier
    instead of username for authetication
    """
    def createuser(self,email,password,**extra_fields):
    # create and save user with email and password 
        if not email:
            raise ValueError({'email must be set'})
        user=self.model(email=email,**extra_fields)
        # we are using the set password method to save the plain password to hash form password
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        #intially we are setting is_active True for superuser
        extra_fields.setdefault('is_active',True)
        #intially we are setting is_superuser True for superuser
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        if extra_fields.get('is_active') is not True:
            raise ValueError({'super user must have is active=True'})
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError({'super user must have is superuser=True'})
        if extra_fields.get('is_staff') is not True:
            raise ValueError({'super user must have is staff=True'})
        
        
        return self.createuser(email,password,**extra_fields)
        
