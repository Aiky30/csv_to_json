import json


class JsonHandler:

    def __init__(self, filename):
        self.file_path = filename

    def read_file(self):
        with open(self.file_path) as file_instance:
            file_contents = json.load(file_instance)

        return file_contents

    def write_file(self, file_contents):
        try:
            with open(self.file_path, 'w') as file_instance:
                file_instance.write(
                    json.dumps(file_contents, indent=2)
                )
        except IOError as err:
            exit(err)
