# object to work easily with te queue


class QueueKaraoke:
    def __init__(self):
        self.queue = []

    def __getitem__(self, item):
        return self.queue[item]

    def __len__(self):
        return len(self.queue)

    def add_user(self, user_id):
        self.queue.append(user_id)

    def remove_user(self, user_id):
        try:
            self.queue.remove(user_id)
        finally:
            pass

    def next_user(self):
        try:
            self.queue.pop(0)
        finally:
            pass

    def contains(self, user_id):
        return user_id in self.queue

    def first(self):
        return self.queue[0]
