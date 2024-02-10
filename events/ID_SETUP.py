ALLOWED_CHANNELS_ID = [
    1146784174787797055,  # "Креативы->команды" channel id
]

NEEDED_ANY_ROLES_ID = [
    1044492389479350322,  # "Curator" role id
    1044491793615556618,  # "Administrator" role id
]

CREATIVE_ROLE_ID = 1044528217903607849,  # "Creative" role id

CHANNEL_EVENT_ID = {
    "Караоке": 1071109880800354426,
    "Озвучка": 1080056201443823686,
    "Кино": 1070330449714495548,
    "Хоррор": 1070330697585270864,
}

def add_local():
    global CREATIVE_ROLE_ID, CHANNEL_EVENT_ID
    local_guild_id = 1167089038986059857  # local guild id for debug
    local_chanel_id = 1167089041108377661  # local chanel id for debug
    local_role_id = 1167190820097638440  # local role id for debug
    ALLOWED_CHANNELS_ID.append(local_chanel_id)
    CREATIVE_ROLE_ID = 1205595786629484674
    NEEDED_ANY_ROLES_ID.append(1205595834175979551)
    CHANNEL_EVENT_ID["Караоке"] = 1167089041108377663
    CHANNEL_EVENT_ID["Озвучка"] = 1167089041108377664

# add_local()  # Adding my local channel and role for debug; comment this line if go to prod
