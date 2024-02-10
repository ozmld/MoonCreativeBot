from karaoke.karaoke_commands import proceed_karaoke_text_interactions

KARAOKE_KEY_WORDS = [
    "+",
    "-",
]

EVENTS_KEY_WORDS = [
]

KEY_WORDS = (
    (KARAOKE_KEY_WORDS, proceed_karaoke_text_interactions),
    (EVENTS_KEY_WORDS, None),
)
