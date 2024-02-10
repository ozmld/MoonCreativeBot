from karaoke.queue_embed import EmbedKaraoke
from karaoke.queue_list import QueueKaraoke

# Class for Karaoke. It contains queue itself and some useful objects


class Karaoke:
    stages = {
        "started": 0,
        "ending": 1,
        "ended": 2,
    }

    def __init__(self, stage="ended"):
        self.embed = EmbedKaraoke()  # embed for the queue
        self.message_object = None  # id of the last-sent queue message (it is needed to delete old queue)
        self.queue_list = QueueKaraoke()  # queue itself
        self.stage = self.stages[stage]  # stage of the karaoke

    def __iter__(self):
        return self.queue_list

    def set_new_message_object(self, new_message_object):
        self.message_object = new_message_object

    def update(self):
        self.embed.update(self.queue_list)

    def add_user(self, user_id):
        self.queue_list.add_user(user_id)
        self.update()

    def remove_user(self, user_id):
        self.queue_list.remove_user(user_id)
        self.update()

    def contains(self, user_id):
        return self.queue_list.contains(user_id)

    def first(self):
        return self.queue_list.first()

    def next(self):
        self.queue_list.next_user()
        self.update()

    def is_started(self):
        return self.stage != self.stages["ended"]

    def is_ongoing(self):
        return self.stage == self.stages["started"]

    def start(self):
        self.stage = self.stages["started"]
        self.embed.start()

    def close(self):
        self.stage = self.stages["ending"]
        self.embed.end()

    def end(self):
        self.stage = self.stages["ended"]
        self.embed.close()
