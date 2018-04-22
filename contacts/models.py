from django.db import models
from django.contrib.auth.models import User

from students.models import Student

from shortuuidfield import ShortUUIDField


class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contacts'

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.full_name

    @models.permalink
    def get_absolute_url(self):
        return 'contact_detail', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'contact_update', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'contact_delete', [self.id]
