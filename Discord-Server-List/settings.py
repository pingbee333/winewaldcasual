import os

CURRECT_DIR = os.path.dirname(os.path.realpath(__file__))

CONFIG = {
    "bot": {
        "token": "NzEzNTc1ODAwOTk3MTUwNzkx.Xsimqw.dieAobR7oWSTec9As5twRpaJS8o",
        "embed_color": 0xaeb8da,
    },

    "lang": "en",

    "refresh_rate": 30,

    "smart_presence": {
        "enable": True,
        "name": False,  # If false will use current map.
    },

    "message_ids": "{}/message_ids.txt".format(CURRECT_DIR),

    "servers": {
        "CSGO": {
            "char_limit": 25,
            "channel": 713504928823377960,
            "servers": {
                "45.235.98.240:27018": "Casul/1v1/+",
                "45.235.98.240:27018": "Casual/1v1/+",
            },
        },
        "CSGO": {
            "char_limit": 25,
            "channel": 713504928823377960,
            "servers": {
                "45.235.98.240:27018": False,
                "45.235.98.240:27018": False,
            },
        },
    },
}