TOKEN = ''  # put your token here
ALLOWED_GUILDS_ID = [
    796785634144288849,  # "Moon" guild id
]


def add_local():
    local_guild_id = 1167089038986059857  # local guild id for debug
    ALLOWED_GUILDS_ID.append(local_guild_id)


# add_local()  # Adding my local channel and role for debug; comment this line if go to prod
