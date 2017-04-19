wagtail-filepreviews
====================

.. image:: https://travis-ci.org/filepreviews/wagtail-filepreviews.svg?branch=master
    :target: https://travis-ci.org/filepreviews/wagtail-filepreviews

.. image:: https://img.shields.io/pypi/v/wagtaildocs_previews.svg
   :target: https://pypi.python.org/pypi/wagtaildocs_previews

Extend Wagtail's Documents with image previews and metadata from `FilePreviews.io`_

Installing
----------

Install with **pip**:

.. code-block:: sh

    $ pip install wagtaildocs_previews

Settings
~~~~~~~~

In your settings file, add ``wagtaildocs_previews`` to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = [
        # ...
        'wagtaildocs_previews',
        # ...
    ]

You'll also need to set ``WAGTAILDOCS_DOCUMENT_MODEL``.

.. code:: python

    WAGTAILDOCS_DOCUMENT_MODEL = 'wagtaildocs_previews.PreviewableDocument'

URL configuration
~~~~~~~~~~~~~~~~~

.. code:: python

    from wagtaildocs_previews import urls as wagtaildocs_urls

    urlpatterns = [
        # ...
        url(r'^documents/', include(wagtaildocs_urls)),
        # ...
    ]

FilePreviews.io API Keys
~~~~~~~~~~~~~~~~~~~~~~~~

For previews to be generated for your documents, you'll need to have a
`FilePreviews.io`_ account and an application's credentials. Once you have
the credentials, add them under the ``FilePreviews`` settings in your
Wagtail admin.

Usage
-----

Since we're extending via ``WAGTAILDOCS_DOCUMENT_MODEL`` you should be using
``get_document_model()`` to reference the correct Document model.

.. code:: python

    from wagtail.wagtailcore.models import Page
    from wagtail.wagtaildocs.models import get_document_model
    from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel


    class BookPage(Page):
        book_file = models.ForeignKey(
            get_document_model(),
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
        )

        content_panels = Page.content_panels + [
            DocumentChooserPanel('book_file'),
        ]


In your template now you'll be able to access the ``preview_data`` field.

.. code:: html

    {% extends "base.html" %}
    {% load wagtailcore_tags %}

    {% block body_class %}resource-page{% endblock %}

    {% block content %}
        <h1>Book</h>
        <h2>{{ page.book_file.title }}</h2>
        <img src="{{ page.book_file.preview_data.preview.url|default:'http://placehold.it/300x300' }}" alt="">
    {% endblock %}

.. _FilePreviews.io: http://filepreviews.io/
