from django.apps import AppConfig


class SourcefeedConfig(AppConfig):
    #? Set app configuration to add a primary key to all your models automatically
    default_auto_field = 'django.db.models.AutoField'
    name = 'sourcefeed'     
