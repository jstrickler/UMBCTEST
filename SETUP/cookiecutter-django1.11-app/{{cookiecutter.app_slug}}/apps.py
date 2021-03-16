from django.apps import AppConfig

class {{cookiecutter.app_slug.title()|replace('_', '')}}Config(AppConfig):
    name = '{{cookiecutter.app_slug}}'
