import disnake
from disnake.ext import commands
import datetime
import pytz

from events.ID_SETUP import CHANNEL_EVENT_ID, CREATIVE_ROLE_ID, NEEDED_ANY_ROLES_ID
from events.EVENT_PARAMS import EVENTS_DECRIPTION, EVENTS_IMAGES
from events.SUPPORTING_DATA import MONTHS_NUMBER_TO_NAME, MONTHS_NAME_TO_NUMBER


def reg_event_commands(bot: commands.Bot):
    pass
    # adding all needed commands

    @bot.slash_command(name="create_event", description="создать сообытие")
    @commands.has_any_role(*NEEDED_ANY_ROLES_ID)
    async def event_create(inter: disnake.ApplicationCommandInteraction,
                           event_type: str = commands.Param(
                               name="тип",
                               description="тип событки",
                               choices=["Караоке", "Озвучка", "Кино", "Хоррор"]
                           ),
                           event_name: str = commands.Param(
                               name="название",
                               description="название событки",
                           ),
                           datetime_hour: int = commands.Param(
                               name="часы",
                               description='часы события',
                               choices=[hh for hh in range(24)],
                           ),
                           datetime_minute: int = commands.Param(
                               name="минуты",
                               description='минуты события',
                               choices=[mm for mm in range(0, 60, 5)],
                               default=0,
                           ),
                           datetime_date=commands.Param(
                               name="дата",
                               description='дата события (1 февраля)',
                               default=None
                           ),
                           image: disnake.Attachment = commands.Param(
                               name="картинка",
                               description='Картинка события',
                               default=None,
                           ),
                           ):  # ctx: commands.Context, image: disnake.Attachment):
        try:
            if datetime_date is not None:
                month_for_event = MONTHS_NAME_TO_NUMBER[datetime_date.split(" ")[1]]
                day_for_event = int(datetime_date.split(" ")[0])
            else:
                day_for_event = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3))).day
                month_for_event = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3))).month
            channel_event = CHANNEL_EVENT_ID[event_type]
            time_for_event = datetime.datetime(2024, month_for_event, day_for_event, datetime_hour, datetime_minute, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
            description_for_event = EVENTS_DECRIPTION[event_type]
            if image is None:
                image_for_event = EVENTS_IMAGES[event_type]
            else:
                image_for_event = await image.read()
            await inter.guild.create_scheduled_event(name=event_name,
                                                     channel=bot.get_channel(channel_event),
                                                     scheduled_start_time=time_for_event,
                                                     description=description_for_event,
                                                     image=image_for_event,
                                                     )
            await inter.send(content="Событие успешно создано!")
        except Exception as e:
            await inter.send(content=str(e))

