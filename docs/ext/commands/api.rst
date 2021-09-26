.. currentmodule:: fosscord

API Reference
===============

The following section outlines the API of Pycord's command extension module.

.. _ext_commands_api_bot:

Bots
------

Bot
~~~~

.. attributetable:: fosscord.ext.commands.Bot

.. autoclass:: fosscord.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:
    
    .. automethod:: Bot.event()
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(name=None)
        :decorator:

AutoShardedBot
~~~~~~~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.AutoShardedBot

.. autoclass:: fosscord.ext.commands.AutoShardedBot
    :members:

Prefix Helpers
----------------

.. autofunction:: fosscord.ext.commands.when_mentioned

.. autofunction:: fosscord.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
-----------------

These events function similar to :ref:`the regular events <fosscord-api-events>`, except they
are custom to the command extension module.

.. function:: fosscord.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: fosscord.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: fosscord.ext.commands.on_command_completion(ctx)

    An event that is called when a command has completed its invocation.

    This event is called only if the command succeeded, i.e. all checks have
    passed and the user input it correctly.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. _ext_commands_api_command:

Commands
----------

Decorators
~~~~~~~~~~~~

.. autofunction:: fosscord.ext.commands.command
    :decorator:

.. autofunction:: fosscord.ext.commands.group
    :decorator:

Command
~~~~~~~~~

.. attributetable:: fosscord.ext.commands.Command

.. autoclass:: fosscord.ext.commands.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~~

.. attributetable:: fosscord.ext.commands.Group

.. autoclass:: fosscord.ext.commands.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.GroupMixin

.. autoclass:: fosscord.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

.. _ext_commands_api_cogs:

Cogs
------

Cog
~~~~

.. attributetable:: fosscord.ext.commands.Cog

.. autoclass:: fosscord.ext.commands.Cog
    :members:

CogMeta
~~~~~~~~

.. attributetable:: fosscord.ext.commands.CogMeta

.. autoclass:: fosscord.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
---------------

HelpCommand
~~~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.HelpCommand

.. autoclass:: fosscord.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.DefaultHelpCommand

.. autoclass:: fosscord.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.MinimalHelpCommand

.. autoclass:: fosscord.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~~

.. attributetable:: fosscord.ext.commands.Paginator

.. autoclass:: fosscord.ext.commands.Paginator
    :members:

Enums
------

.. class:: BucketType
    :module: fosscord.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

        .. versionadded:: 1.3


.. _ext_commands_api_checks:

Checks
-------

.. autofunction:: fosscord.ext.commands.check(predicate)
    :decorator:

.. autofunction:: fosscord.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: fosscord.ext.commands.has_role(item)
    :decorator:

.. autofunction:: fosscord.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: fosscord.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: fosscord.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: fosscord.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: fosscord.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: fosscord.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: fosscord.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: fosscord.ext.commands.cooldown(rate, per, type=fosscord.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: fosscord.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: fosscord.ext.commands.max_concurrency(number, per=fosscord.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: fosscord.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: fosscord.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: fosscord.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: fosscord.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: fosscord.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: fosscord.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
---------

.. attributetable:: fosscord.ext.commands.Cooldown

.. autoclass:: fosscord.ext.commands.Cooldown
    :members:

Context
--------

.. attributetable:: fosscord.ext.commands.Context

.. autoclass:: fosscord.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: fosscord.ext.commands.Context.history
        :async-for:

    .. automethod:: fosscord.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
------------

.. autoclass:: fosscord.ext.commands.Converter
    :members:

.. autoclass:: fosscord.ext.commands.ObjectConverter
    :members:

.. autoclass:: fosscord.ext.commands.MemberConverter
    :members:

.. autoclass:: fosscord.ext.commands.UserConverter
    :members:

.. autoclass:: fosscord.ext.commands.MessageConverter
    :members:

.. autoclass:: fosscord.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: fosscord.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.TextChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.StoreChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.StageChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: fosscord.ext.commands.InviteConverter
    :members:

.. autoclass:: fosscord.ext.commands.GuildConverter
    :members:

.. autoclass:: fosscord.ext.commands.RoleConverter
    :members:

.. autoclass:: fosscord.ext.commands.GameConverter
    :members:

.. autoclass:: fosscord.ext.commands.ColourConverter
    :members:

.. autoclass:: fosscord.ext.commands.EmojiConverter
    :members:

.. autoclass:: fosscord.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: fosscord.ext.commands.ThreadConverter
    :members:

.. autoclass:: fosscord.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: fosscord.ext.commands.clean_content
    :members:

.. autoclass:: fosscord.ext.commands.Greedy()

.. autofunction:: fosscord.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~~

.. autoclass:: fosscord.ext.commands.FlagConverter
    :members:

.. autoclass:: fosscord.ext.commands.Flag()
    :members:

.. autofunction:: fosscord.ext.commands.flag

.. _ext_commands_api_errors:

Exceptions
-----------

.. autoexception:: fosscord.ext.commands.CommandError
    :members:

.. autoexception:: fosscord.ext.commands.ConversionError
    :members:

.. autoexception:: fosscord.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: fosscord.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: fosscord.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: fosscord.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: fosscord.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: fosscord.ext.commands.BadArgument
    :members:

.. autoexception:: fosscord.ext.commands.BadUnionArgument
    :members:

.. autoexception:: fosscord.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: fosscord.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: fosscord.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: fosscord.ext.commands.CheckFailure
    :members:

.. autoexception:: fosscord.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: fosscord.ext.commands.CommandNotFound
    :members:

.. autoexception:: fosscord.ext.commands.DisabledCommand
    :members:

.. autoexception:: fosscord.ext.commands.CommandInvokeError
    :members:

.. autoexception:: fosscord.ext.commands.TooManyArguments
    :members:

.. autoexception:: fosscord.ext.commands.UserInputError
    :members:

.. autoexception:: fosscord.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: fosscord.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: fosscord.ext.commands.NotOwner
    :members:

.. autoexception:: fosscord.ext.commands.MessageNotFound
    :members:

.. autoexception:: fosscord.ext.commands.MemberNotFound
    :members:

.. autoexception:: fosscord.ext.commands.GuildNotFound
    :members:

.. autoexception:: fosscord.ext.commands.UserNotFound
    :members:

.. autoexception:: fosscord.ext.commands.ChannelNotFound
    :members:

.. autoexception:: fosscord.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: fosscord.ext.commands.ThreadNotFound
    :members:

.. autoexception:: fosscord.ext.commands.BadColourArgument
    :members:

.. autoexception:: fosscord.ext.commands.RoleNotFound
    :members:

.. autoexception:: fosscord.ext.commands.BadInviteArgument
    :members:

.. autoexception:: fosscord.ext.commands.EmojiNotFound
    :members:

.. autoexception:: fosscord.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: fosscord.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: fosscord.ext.commands.BadBoolArgument
    :members:

.. autoexception:: fosscord.ext.commands.MissingPermissions
    :members:

.. autoexception:: fosscord.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: fosscord.ext.commands.MissingRole
    :members:

.. autoexception:: fosscord.ext.commands.BotMissingRole
    :members:

.. autoexception:: fosscord.ext.commands.MissingAnyRole
    :members:

.. autoexception:: fosscord.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: fosscord.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: fosscord.ext.commands.FlagError
    :members:

.. autoexception:: fosscord.ext.commands.BadFlagArgument
    :members:

.. autoexception:: fosscord.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: fosscord.ext.commands.TooManyFlags
    :members:

.. autoexception:: fosscord.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: fosscord.ext.commands.ExtensionError
    :members:

.. autoexception:: fosscord.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: fosscord.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: fosscord.ext.commands.NoEntryPointError
    :members:

.. autoexception:: fosscord.ext.commands.ExtensionFailed
    :members:

.. autoexception:: fosscord.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: fosscord.ext.commands.CommandRegistrationError
    :members:


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.FosscordException`
        - :exc:`~.commands.CommandError`
            - :exc:`~.commands.ConversionError`
            - :exc:`~.commands.UserInputError`
                - :exc:`~.commands.MissingRequiredArgument`
                - :exc:`~.commands.TooManyArguments`
                - :exc:`~.commands.BadArgument`
                    - :exc:`~.commands.MessageNotFound`
                    - :exc:`~.commands.MemberNotFound`
                    - :exc:`~.commands.GuildNotFound`
                    - :exc:`~.commands.UserNotFound`
                    - :exc:`~.commands.ChannelNotFound`
                    - :exc:`~.commands.ChannelNotReadable`
                    - :exc:`~.commands.BadColourArgument`
                    - :exc:`~.commands.RoleNotFound`
                    - :exc:`~.commands.BadInviteArgument`
                    - :exc:`~.commands.EmojiNotFound`
                    - :exc:`~.commands.GuildStickerNotFound`
                    - :exc:`~.commands.PartialEmojiConversionFailure`
                    - :exc:`~.commands.BadBoolArgument`
                    - :exc:`~.commands.ThreadNotFound`
                    - :exc:`~.commands.FlagError`
                        - :exc:`~.commands.BadFlagArgument`
                        - :exc:`~.commands.MissingFlagArgument`
                        - :exc:`~.commands.TooManyFlags`
                        - :exc:`~.commands.MissingRequiredFlag`
                - :exc:`~.commands.BadUnionArgument`
                - :exc:`~.commands.BadLiteralArgument`
                - :exc:`~.commands.ArgumentParsingError`
                    - :exc:`~.commands.UnexpectedQuoteError`
                    - :exc:`~.commands.InvalidEndOfQuotedStringError`
                    - :exc:`~.commands.ExpectedClosingQuoteError`
            - :exc:`~.commands.CommandNotFound`
            - :exc:`~.commands.CheckFailure`
                - :exc:`~.commands.CheckAnyFailure`
                - :exc:`~.commands.PrivateMessageOnly`
                - :exc:`~.commands.NoPrivateMessage`
                - :exc:`~.commands.NotOwner`
                - :exc:`~.commands.MissingPermissions`
                - :exc:`~.commands.BotMissingPermissions`
                - :exc:`~.commands.MissingRole`
                - :exc:`~.commands.BotMissingRole`
                - :exc:`~.commands.MissingAnyRole`
                - :exc:`~.commands.BotMissingAnyRole`
                - :exc:`~.commands.NSFWChannelRequired`
            - :exc:`~.commands.DisabledCommand`
            - :exc:`~.commands.CommandInvokeError`
            - :exc:`~.commands.CommandOnCooldown`
            - :exc:`~.commands.MaxConcurrencyReached`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`
