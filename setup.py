import os
from setuptools import setup

setup(
  name = "Django-CMS Pagedown Plugin",
  version = "0.0.1dev",
  author = "Timmy O'Mahony",
  author_email = "hello@timmyomahony.com",
  url = "https://github.com/pastylegs/cmsplugin-pagedown/",
  description = ("A plugin for django-cms that includes the StackOverflow pagedown editor"),
  long_description=open('README.md').read(),
  packages=['cmsplugin_pagedown'],
  install_requires=[
    "Django >= 1.2",
  ],
  license='LICENSE.txt',
)
