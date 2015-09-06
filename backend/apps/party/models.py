from django.db import models


class Party(models.Model):
    name = models.CharField(default='', max_length=255)
    image = models.ImageField(upload_to='party')

    class Meta:
        db_table = 'party'
        verbose_name_plural = 'parties'

    def __unicode__(self):
        return u'Party({})'.format(self.name)

