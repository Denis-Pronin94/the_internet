from dynaconf import LazySettings

settings = LazySettings(
    SETTINGS_FILE_FOR_DYNACONF='settings.yaml;settings.local.yaml',

)
settings.configure()

NAME = settings['NAME']
PASSWORD = settings['PASSWORD']
