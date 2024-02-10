from disnake import Embed
from karaoke.queue_text import *


class EmbedKaraoke(Embed):
    def __init__(self):
        super().__init__(title=QUEUE_TITLE, color=QUEUE_COLOR)
        super().set_footer(text=QUEUE_FOOTER_BEGIN)
        super().add_field(name="", value="", inline=False)
        super().add_field(name="Сейчас", value="", inline=False)
        super().add_field(name="", value="", inline=False)
        super().add_field(name="Следующие", value="", inline=False)
        self.now_pos = 1
        self.next_pos = 3

    def update(self, queue_list):
        if len(queue_list) == 0:
            super().set_field_at(
                self.now_pos,
                name=super().fields[self.now_pos].name,
                value="",
                inline=False,
            )
            super().set_field_at(
                self.next_pos,
                name=super().fields[self.next_pos].name,
                value="",
                inline=False,
            )
            return
        super().set_field_at(
            self.now_pos,
            name=super().fields[self.now_pos].name,
            value=f"> {DOT_EMOJI} <@{queue_list[0]}>",
            inline=False,
        )
        description = ""
        for i in range(1, len(queue_list)):
            if i == 1:
                description += ">>> "
            description += f"{DOT_EMOJI} <@{queue_list[i]}>\n"
        super().set_field_at(self.next_pos, name=super().fields[self.next_pos].name, value=description, inline=False)
        return

    def start(self):
        super().set_footer(text=QUEUE_FOOTER_BEGIN)

    def end(self):
        super().set_footer(text=QUEUE_FOOTER_END)

    def close(self):
        super().set_footer(text=QUEUE_FOOTER_CLOSE)