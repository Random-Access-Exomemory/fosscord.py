fosscord.py
==========

A fork of PyCord. Fosscord.py is a modern, easy to use, feature-rich, and async ready API wrapper for Fosscord written in Python.

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory.

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U fosscord.py

    # Windows
    py -3 -m pip install -U fosscord.py

Otherwise to get voice support you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "fosscord.py[voice]"

    # Windows
    py -3 -m pip install -U fosscord.py[voice]

To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/mugman174/fosscord.py
    $ cd fosscord.py
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Quick Example
--------------

.. code:: py

    import fosscord

    bot = fosscord.Bot()
    
    @bot.slash_command()
    async def hello(ctx, name: str = None):
        name = name or ctx.author.name
        await ctx.respond(f"Hello {name}!")
        
    @bot.user_command(name="Say Hello")
    async def hi(ctx, user):
        await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")
        
    bot.run("token")

Normal Commands Example
~~~~~~~~~~~~~

.. code:: py
    # Note this example is currently non-working
    import fosscord
    from fosscord.ext import commands

    bot = commands.Bot(command_prefix=">")

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    bot.run("token")

You can find more examples in the examples directory.

Links
------

- `Documentation <https://pycord.readthedocs.io/en/latest/index.html>`_
- `Official Fosscord Server <https://fosscord.gg/dK2qkEJ37N>`_
