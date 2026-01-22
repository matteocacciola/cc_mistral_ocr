from pydantic import BaseModel
from cat import plugin


# Plugin settings
class PluginSettings(BaseModel):
    mistral_api_key: str
    save_text_to_rabbit_hole: bool = False


# hook to give the cat settings
@plugin
def settings_schema():
    return PluginSettings.model_json_schema()
