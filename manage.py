#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lend_frontend.settings")

    from django.core.management import execute_from_command_line

    from lend_frontend.utils.heat_template_fetcher import HeatTemplateFetcher

    fetcher = HeatTemplateFetcher()
    fetcher.startFetching()

    execute_from_command_line(sys.argv)
