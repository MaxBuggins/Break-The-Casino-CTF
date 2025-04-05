from CTFd.constants import RawEnum


class Languages(str, RawEnum):
    ENGLISH = "en"
    CHINESE = "zh_CN"


LANGUAGE_NAMES = {
    "en": "English",
    "zh_CN": "简体中文",
}

SELECT_LANGUAGE_LIST = [("", "")] + [
    (str(lang), LANGUAGE_NAMES.get(str(lang))) for lang in Languages
]

Languages.names = LANGUAGE_NAMES
Languages.select_list = SELECT_LANGUAGE_LIST
