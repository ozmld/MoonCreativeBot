import disnake
from disnake.ext import commands
import datetime
from KEY_INFO import TOKEN, ALLOWED_GUILDS_ID
from TEXT_KEY_WORDS import KEY_WORDS
from karaoke.karaoke_commands import reg_karaoke_commands, proceed_karaoke_text_interactions
from events.events_commands import reg_event_commands
from events.EVENT_PARAMS import KARAOKE_DESCRIPTION
activity = disnake.Activity(
    name="за очередью на караоке",
    type=disnake.ActivityType.watching
)

bot = commands.Bot(command_prefix='!',
                   help_command=None,
                   intents=disnake.Intents.all(),
                   activity=activity,
                   test_guilds=[1167089038986059857])


def bot_run():
    reg_karaoke_commands(bot)  # Adding commands into bot
    reg_event_commands(bot)

    @bot.event
    async def on_message(message: disnake.Message):
        # checking if message in allowed guild and channel
        if message.guild.id not in ALLOWED_GUILDS_ID:
            return
        is_key_word = False
        for words, name in KEY_WORDS:
            if message.content in words:
                is_key_word = True
                await name(message)
        if not is_key_word:
            await bot.process_commands(message)
    bot.run(TOKEN)
