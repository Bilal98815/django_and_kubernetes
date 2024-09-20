from django.contrib import admin
from .models import PracticeModel, Tag, ChangeLog, StaticFilesModel

# Register your models here.
admin.site.register(PracticeModel)
admin.site.register(Tag)
admin.site.register(ChangeLog)
admin.site.register(StaticFilesModel)
