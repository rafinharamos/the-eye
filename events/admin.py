from django.contrib import admin

from events.models import Event, Session, EventError

admin.site.register(Event)
admin.site.register(Session)
admin.site.register(EventError)
