import disnake
from disnake.ext import commands

from karaoke.KaraokeObject import Karaoke

from karaoke.ID_SETUP import ALLOWED_GUILDS_ID, ALLOWED_CHANNELS_ID, NEEDED_ROLES_ID

last_message = None

karaoke = Karaoke()


async def refresh_queue(channel, flag=None):
    if flag == "start":
        message = await channel.send(embed=karaoke.embed)
        karaoke.set_new_message_object(message)
        return
    await karaoke.message_object.delete()
    message = await channel.send(embed=karaoke.embed)
    karaoke.set_new_message_object(message)


async def delete_message(message: disnake.Message):
    await message.delete()


def check_if_it_is_allowed_channel(ctx: commands.Context):
    return ctx.channel.id in ALLOWED_CHANNELS_ID


def check_if_karaoke_is_started(ctx: commands.Context):
    return karaoke.is_started()


def reg_karaoke_commands(bot: commands.Bot):
    # adding all needed commands
    @bot.command(name="queue",
                 aliases=["Queue", "очередь", "Очередь"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.check(check_if_karaoke_is_started)
    async def queue_command(ctx: commands.Context):
        await refresh_queue(ctx.channel)
        await delete_message(ctx.message)

    @bot.command(name="now",
                 aliases=["Now"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    @commands.check(check_if_karaoke_is_started)
    async def now_command(ctx: commands.Context):
        descr = f"<@{karaoke.first()}> твоя очередь петь! Ждём тебя!"
        await ctx.channel.send(descr)
        await delete_message(ctx.message)

    @bot.command(name="next",
                 aliases=["Next"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    @commands.check(check_if_karaoke_is_started)
    async def next_command(ctx: commands.Context):
        karaoke.next()
        await refresh_queue(ctx.channel)
        await delete_message(ctx.message)

    @bot.command(name="delete",
                 aliases=["Delete"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    @commands.check(check_if_karaoke_is_started)
    async def delete_command(ctx: commands.Context, user_id):
        user_id = int(user_id)
        karaoke.remove_user(user_id)
        await refresh_queue(ctx.channel)
        await delete_message(ctx.message)

    # @bot.command(name="skip")
    # @commands.check(check_if_it_is_allowed_channel)
    # @commands.has_any_role(*NEEDED_ROLES_ID)
    # @commands.check(check_if_karaoke_is_started)
    # async def skip_command(ctx: commands.Context):
    #     karaoke.next()
    #     await delete_message(ctx.message)

    @bot.command(name="start",
                 aliases=["Start"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    async def start_command(ctx: commands.Context):
        global karaoke
        karaoke.start()
        await refresh_queue(ctx.channel, flag="start")
        await delete_message(ctx.message)

    @bot.command(name="close",
                 aliases=["Close"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    @commands.check(check_if_karaoke_is_started)
    async def close_command(ctx: commands.Context):
        karaoke.close()
        await refresh_queue(ctx.channel)
        await delete_message(ctx.message)

    @bot.command(name="end",
                 aliases=["End"])
    @commands.check(check_if_it_is_allowed_channel)
    @commands.has_any_role(*NEEDED_ROLES_ID)
    @commands.check(check_if_karaoke_is_started)
    async def end_command(ctx: commands.Context):
        karaoke.end()
        await refresh_queue(ctx.channel)
        await delete_message(ctx.message)


async def proceed_karaoke_text_interactions(message: disnake.Message):
    if message.channel.id not in ALLOWED_CHANNELS_ID:
        return
    if not check_if_karaoke_is_started(None):
        return
    global karaoke
    # adding (+) and removing (-) person to/from the queue
    if message.content == "+" and karaoke.is_ongoing():
        if not karaoke.contains(message.author.id):
            karaoke.add_user(message.author.id)
            await refresh_queue(message.channel)
            await delete_message(message)

    if message.content == "-":
        if karaoke.contains(message.author.id):
            karaoke.remove_user(message.author.id)
            await refresh_queue(message.channel)
            await delete_message(message)