Django-CMS Pagedown Plugin
===============

A django-cms plugin to allow the use of [Stack Overflow&#39;s &quot;Pagedown&quot; Markdown editor](http://code.google.com/p/pagedown/)

#### Installation ####

- Make sure you have included `django.contrib.markup` in your `INSTALLED_APPS`
- Install via pip: `pip install -e https://github.com/timmyomahony/cmsplugin-pagedown.git#egg=cmsplugin-pagedown` or `pip install cmsplugin-pagedown`
- Add `cmsplugin_pagedown` to your `INSTALLED_APPS`

#### Usage ####

Simply select `Pagedown Markdown` from the `Available Plugins` dropdown when using a django-cms placeholder. 

#####Screenshot: Example Frontend Output#####

------

![Screenshot of example frontend output](https://github.com/timmyomahony/cmsplugin-pagedown/blob/master/frontend-screenshot.png?raw=true "Screenshot of example frontend output")

#####Screenshot: Plugin#####

------

![Screenshot of a CMS placeholder using pagedown](https://github.com/timmyomahony/cmsplugin-pagedown/blob/master/backend-screenshot.png?raw=true "Screenshot of a CMS placeholder using pagedown")
