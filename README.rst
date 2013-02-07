Django Hero Slider 
==================

EARLY ALPHA! DO NOT USE THIS!

A Django application for defining images that should be shown on the frontpage
of your website in a slider. Each image can have a title, description and
a generic foreign key to any object in your database.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install Pillow
    pip install django-filer
    pip install South

If you want to install the latest stable release from PyPi::

    $ pip install django-hero-slider

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-hero-slider.git#egg=hero_slider

Add ``filer``, ``easy_thumbnails``  and ``hero_slider`` to your 
``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'filer',
        'easy_thumbnails'
        'hero_slider',
    )

Run the South migrations::

    ./manage.py migrate


Usage
-----

TODO: Describe usage


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-hero-slider
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
