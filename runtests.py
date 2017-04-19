#!/usr/bin/env python
import sys
import os
import shutil

from django.core.management import execute_from_command_line


os.environ['DJANGO_SETTINGS_MODULE'] = 'wagtaildocs_previews.tests.settings'


def runtests():
    args = sys.argv[1:]
    argv = sys.argv[:1] + ['test'] + args
    try:
        execute_from_command_line(argv)
    finally:
        from wagtaildocs_previews.tests.settings import STATIC_ROOT, MEDIA_ROOT
        shutil.rmtree(STATIC_ROOT, ignore_errors=True)
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)


if __name__ == '__main__':
    runtests()
