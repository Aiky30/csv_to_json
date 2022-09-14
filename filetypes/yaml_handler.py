import yaml


class YamlHandler:

    def __init__(self, filename):
        self.file_path = filename

    def write_file(self, file_contents):
        try:
            with open(self.file_path, 'w') as file_instance:
                file_instance.write(
                    yaml.dump(file_contents, sort_keys=False, indent=2)
                )
        except IOError as err:
            exit(err)
