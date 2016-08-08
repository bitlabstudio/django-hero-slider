Django Hero Slider
==================

A Django application for defining images that should be shown on the frontpage
of your website in a slider. Each image can have a title, description and
a generic foreign key to any object in your database.


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install django-hero-slider

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-hero-slider.git#egg=hero_slider

Add ``filer``, ``easy_thumbnails``  and ``hero_slider`` to your
``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'filer',
        'easy_thumbnails',
        'hero_slider',
    )

If you have ``sorl-thumbnail`` already in your ``INSTALLED_APPS`` you may run across some errors since ``sorl-thumbnail`` and ``easy_thumbnail`` use the same load template tag syntax ``{% load thumbnail %}``. Please see more details here: http://stackoverflow.com/questions/8174122/django-sorl-thumbnail-and-easy-thumbnail-in-same-project

Include the urls for this app::


    urlpatterns = patterns(
        '',
        url(r'^hero-slider/', include('hero_slider.urls')),
    )

Run the migrations::

    ./manage.py migrate


Usage
-----

Login to the Django admin and create some SliderItem objects. Each SliderItem
should point to some other object (with a generic foreign key).

In your template you can display the slider like this::

    {% load hero_slider_tags %}

    {% render_hero_slider %}

    <script type="text/javascript">
    $(document).ready(function() {
        // put all your jQuery goodness in here.
        $('.carousel').carousel({
            /* interval: 3000 */
        })
    });
    </script>

Alternatively you can use the ``get_slider_items`` assignment tag::

    {% load hero_slider_tags %}

    {% get_slider_items as items %}
    {% include "some_template/slider.html with items=items %}


If you want to change the look and feel of the slider, just override the
``hero_slider/carousel.html`` template.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-hero-slider
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
