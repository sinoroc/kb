..


***
npm
***

Packages in home directory
==========================

This will let ``npm`` use a custom directory for globally installed package.

.. code-block:: bash
    :caption: ~/.profile

    # ...
    export NPM_PACKAGES="${HOME}/.npm_packages"
    PATH="${NPM_PACKAGES}/bin:${PATH}"
    NODE_PATH="${NPM_PACKAGES}/lib/node_modules:${PATH}"
    # ...


.. code-block:: bash
    :caption: ~/.npmrc

    # ...
    prefix = "${NPM_PACKAGES}"
    # ...


.. code-block:: shell-session
    :caption: shell interactive console

    $ . ~/.profile
    $ npm install --global npm


.. EOF
