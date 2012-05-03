import os
from setuptools import setup

setup(
  name = "cmsplugin-pagedown",
  version = "0.0.1",
  author = "Timmy O'Mahony",
  author_email = "me@timmyomahony.com",
  url = "https://github.com/timmyomahony/cmsplugin-pagedown",
  description = ("A plugin for django-cms that includes the StackOverflow pagedown editor"),
  long_description=open('README.md').read(),
  packages=['cmsplugin_pagedown'],
  include_package_data=True,
  install_requires=[
    "Django >= 1.3",
    "django-pagedown"
  ],
  license='LICENSE.txt',
)
