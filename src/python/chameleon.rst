..


*********
Chameleon
*********

.. contents::
    :backlinks: none
    :local:


Introduction
============


* https://pypi.org/project/Chameleon/
* https://chameleon.readthedocs.io/


Macros
======

Omit tag
--------

Tags from the namespace ``tal`` and ``metal`` are omitted. But no specific
tag name is required. So use something like this

.. code::

    <metal: metal:something="whatever">...</metal:>
    <tal: tal:something="whatever">...</tal:>


Same file
---------

Use macro from the same template (same file).

The macros are available under ``template.macros`` or directly under
``macros``.

.. code::

    <metal: metal:define-macro="ping">pong</metal:>

    <metal: metal:use-macro="template.macros['ping']"></metal:>
    <metal: metal:use-macro="macros['ping']"></metal:>


I18N
====

Babel
-----

According to its documentation ``chameleon`` should provide a message extractor
for ``Babel``, but it is not actually the case.

https://github.com/malthe/chameleon/issues/12

Use ``lingua`` instead. It has a message extractor for ``chameleon``.


lingua
------

Even though ``lingua`` claims in its documentation to always extract messages
that do not have a domain, it is not the case for the ``chameleon`` extractor.

Make sure to always specify a ``domain`` in the ``.pt`` file. Otherwise the
messages won't be extracted by ``pot-create``.


.. code::

    <tal: i18n:domain="MyDomain">
        <!-- ... -->
        <span i18n:translate="">message</span>
        <!-- ... -->
    </tal:>


.. EOF
