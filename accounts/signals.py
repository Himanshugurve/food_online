from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile


@receiver(post_save, sender=User)
def _post_save_receiver(sender, instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        # print("Create the user profile")
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            print(instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
        print('user is updated')
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    pass
    