ALLOWED_GUILDS_ID = [
    796785634144288849,  # "Moon" guild id
]


ALLOWED_CHANNELS_ID = [
    1071109880800354426,  # "Творчество" channel id
]

NEEDED_ROLES_ID = [
    1044528217903607849,  # "Creative" role id
]

def add_local():
    local_guild_id = 1167089038986059857  # local guild id for debug
    local_chanel_id = 1167089041108377661  # local chanel id for debug
    local_role_id = 1167190820097638440  # local role id for debug
    ALLOWED_GUILDS_ID.append(local_guild_id)
    ALLOWED_CHANNELS_ID.append(local_chanel_id)
    NEEDED_ROLES_ID.append(local_role_id)


# add_local()  # Adding my local channel and role for debug; comment this line if go to prod
