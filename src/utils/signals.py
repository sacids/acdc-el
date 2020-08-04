from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from utils.models import *

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    #get models
    #courses         = StudentRegistration.models.filter(student_id=user.id)
    request.session['courses']  = StudentRegistration.models.filter(student_id=user.id).values()
    print(request.session['courses'])
    print('testing')
    print("user logged in: %s at %s" % (user, request.META['REMOTE_ADDR']))
    logger = logging.getLogger(__name__)
    logger.info("user logged in: %s at %s" % (user, request.META['REMOTE_ADDR']))

@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    #get models
    del request.session['courses']
    print("user logged out: %s at %s" % (user, request.META['REMOTE_ADDR']))