import yaml

BOT_VERSION = "1.0.0"
BOT_MODULE = "discord.py"

DEBUGMODE = False

# YAML 設定ファイルを読み込む関数
def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config("config.yml")
if DEBUGMODE:
    config = load_config("config_debug.yml")

try:
    token = config["token"]
except Exception:
    token = ""