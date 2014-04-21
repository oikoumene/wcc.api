wcc.api Installation
--------------------

To install wcc.api using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``wcc.api`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        wcc.api

* Re-run buildout, e.g. with:

    $ ./bin/buildout

