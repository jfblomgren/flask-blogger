from app import cache
from app.models import Setting
from app.utils.helpers import get_or_create


class AppSettings(dict):
    def __setitem__(self, key, value):
        setting, created = get_or_create(Setting, name=key)
        setting.value = value
        setting.save()

        # Delete the Setting dictionary cache
        cache.delete_memoized(Setting.get_dict)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __getitem__(self, key):
        return Setting.get_dict()[key]
