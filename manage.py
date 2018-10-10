#!/usr/bin/env python
import importlib
import platform

from django.core.management import execute_from_command_line
from django.conf import settings as django_settings


def load_django_settings(mode='develop'):
    settings = {}
    kwargs = {}
    mods = [importlib.import_module('admin.settings_lin')]

    if platform.system() == "Windows":
        try:
            mods.append(importlib.import_module('settings_win'))
        except ImportError:
            pass

    if hasattr(mods[0], 'load_settings'):
        getattr(mods[0], 'load_settings')(settings, **kwargs)

    django_settings.configure(**settings)


def execute():
    load_django_settings()
    execute_from_command_line()


if __name__ == "__main__":
    execute()
