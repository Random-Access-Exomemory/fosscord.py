import fosscord

bot = fosscord.Bot()

# Note: If you want you can use commands.Bot instead of fosscord.Bot
# Use fosscord.Bot if you don't want prefixed message commands

# With fosscord.Bot you can use @bot.command as an alias 
# of @bot.slash_command but this is overriden by commands.Bot


@bot.slash_command(guild_ids=[...])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.send(f"Hello {ctx.author}!")


@bot.slash_command(
    name="hi"
)  # Not passing in guild_ids creates a global slash command (might take an hour to register)
async def global_command(ctx, num: int):  # Takes one integer parameter
    await ctx.send(f"This is a global command, {num}!")


@bot.slash_command(guild_ids=[...])
async def joined(
    ctx, member: fosscord.Member = None
):  # Passing a default value makes the argument optional
    user = member or ctx.author
    await ctx.send(f"{user.name} joined at {fosscord.utils.format_dt(user.joined_at)}")


# To learn how to add descriptions, choices to options check slash_options.py
bot.run("TOKEN")
