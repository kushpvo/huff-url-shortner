from django.db import models
from django.urls import reverse
from hashids import Hashids

hashids = Hashids(salt='this is a very unique salt to make things interesting',
                  min_length=6, alphabet='abcdefghijklmnpqrstuvwxyz123456789')


class Link(models.Model):
    long_url = models.URLField()

    def get_absolute_url(self):
        return reverse("link_detail", kwargs={"pk": self.pk})

    # Converts long_url to short url
    @staticmethod
    def shorten_url(url):
        link = Link.objects.filter(long_url=url).first()
        return str(hashids.encode(link.pk))

    # Convert/decode short url to original long url's pk id
    @staticmethod
    def decode_url(hash):
        # Decoding and getting the dirty value '(12,)'
        dirty_id = str(hashids.decode(hash))
        # removing the extra comma and brackets at the end
        clean_id = dirty_id.strip("(,)")
        print(clean_id)
        # convert string id to int id
        long_url_id = int(clean_id)
        link_obj = Link.objects.get(pk=long_url_id)
        return link_obj.id

    def short_url(self):
        return str(Link.shorten_url(self.long_url))

    def __str__(self):
        return self.long_url
