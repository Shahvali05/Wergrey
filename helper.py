import json


def load_settings(json_file: str):
    with open(json_file, "r", encoding="utf-8") as file:
        settings = json.load(file)
    return settings


settings = load_settings("settings.json")
# диалоги
glava_1 = load_settings("glava_1.json")


def save_settings(json_file):
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)


def change_language(new_language):
    settings["language"]["current"] = new_language
    save_settings("settings.json")


def change_name(new_name):
    settings["name"] = new_name
    save_settings("settings.json")


def change_sound(new_name):
    settings["sound"] = new_name
    save_settings("settings.json")


def set_default_setings():
    settings["name"] = "NULL"
    save_settings("settings.json")


# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)
BROWN = (165, 42, 42)
