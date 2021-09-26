fosscord.py
==========

.. image:: https://img.shields.io/discord/806142446094385153?color=5865f2&label=Discord&logo=discord
   :target: https://discord.gg/Ms5Ev7S6bF
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/py-cord.svg
   :target: https://pypi.python.org/pypi/py-cord
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/py-cord.svg
   :target: https://pypi.python.org/pypi/py-cord
   :alt: PyPI supported Python versions

A fork of PyCord. Fosscord.py is a modern, easy to use, feature-rich, and async ready API wrapper for Fosscord instances written in Python.

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
    python3 -m pip install -U py-cord

    # Windows
    py -3 -m pip install -U py-cord

Otherwise to get voice support you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "py-cord[voice]"

    # Windows
    py -3 -m pip install -U py-cord[voice]


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/mugman174/fosscord
    $ cd fosscord
    $ python3 -m pip install -U .[voice]


Quick Example
--------------

.. code:: py

    import fosscord

    bot = discord.Client()

    @bot.event
    async def on_ready():
        print("Logged on as", bot.user)

    @bot.event
    async def on_message(message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')    
        
    bot.run("token")

You can find more examples in the examples directory.

Links
------

- `Documentation <https://pycord.readthedocs.io/en/latest/index.html>`_
- `Official Discord Server <https://discord.gg/Ms5Ev7S6bF>`_
- `Discord Developers <https://discord.gg/discord-developers>`_
- `Discord API <https://discord.gg/discord-api>`_
