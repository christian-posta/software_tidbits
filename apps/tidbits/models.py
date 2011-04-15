from django.db import models

# Create your models here.
class TidbitManager(models.Manager):

    def recent_tidbits(self, num_to_display=25):
        '''Recent tidbits are the last num_to_display tidbits posted '''

        return self.order_by('-created')[:25]


class Tidbit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # from the docs: take note that the first custom manager created will be used as the
    # default manager
    objects = TidbitManager()

    def __unicode__(self):
        return self.title

class TidbitUrl(models.Model):

    # default max_length for this field is 200. Setting it to be
    # explicit
    url = models.URLField(verify_exists=False, max_length=200, help_text="A URL that you used as reference")
    tidbit = models.ForeignKey(Tidbit)