from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpec
from imagekit.processors import Crop, Adjust

class Account(models.Model):
    
    user = models.ForeignKey(User, related_name='Username')
    display_pic = models.ImageField(upload_to='accountpics')
    thumbnail = ImageSpec([Adjust(contrast=1.2, sharpness=1.1), Crop(50, 50)], image_field='display_pic', format='JPEG', options={'quality': 90})
    
    def __unicode__(self):
        return '%s'%(self.user)
    
    class Meta:
        ordering=['user']

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class UserLink (models.Model):
    from_user = models.ForeignKey(User, related_name= 'from_user')
    to_user = models.ForeignKey(User, related_name= 'to_user')
    date_added = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s is following %s'%(self.from_user,self.to_user)
    
    def save(self, force_insert=False, force_update=False):
        if self.to_user == self.from_user:
            raise IntegrityError("Users can't follow themselves")
        super(UserLink, self).save(force_insert=force_insert,   force_update=force_update)
    
    class Meta:
        unique_together=(('from_user', 'to_user'),)
        ordering=['from_user']
