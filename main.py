from discord.ext import commands
import config
import helpers

bot = commands.AutoShardedBot(
    command_prefix=config.PREFIX,
    case_insensitive=True,
    description=config.DESCRIPTION,
    owner_ids=config.OWNERS
)

for extension in config.extensions:

    try:
        bot.load_extension(extension)
        helpers.info(f'Loaded {extension}')
    except:
        helpers.warn(f'Failed to load {extension}')

bot.run(config.TOKEN)
