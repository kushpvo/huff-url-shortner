from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['short_url_display']
    list_display = ['long_url', 'short_url_display']

    def short_url_display(self, instance):
        return ("https://huff.pw/" + str(instance.short_url()))


admin.site.register(Link, LinkAdmin)
