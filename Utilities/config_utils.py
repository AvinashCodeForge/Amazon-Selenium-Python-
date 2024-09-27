import yaml


class ConfigUtilities:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_config(self, key):
        return self.config_data.get(key)

