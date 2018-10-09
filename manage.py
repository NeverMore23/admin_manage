#!/usr/bin/env python
import importlib

from django.core.management import execute_from_command_line
from django.conf import settings as django_settings


def load_django_settings():
    settings = {}
    kwargs = {}
    mods = [importlib.import_module('admin.settings')]

    if hasattr(mods[0], 'load_settings'):
        getattr(mods[0], 'load_settings')(settings, **kwargs)

    django_settings.configure(**settings)


def execute():
    load_django_settings()
    execute_from_command_line()


if __name__ == "__main__":
    execute()
