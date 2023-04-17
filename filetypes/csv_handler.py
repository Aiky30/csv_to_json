import csv


class CsvHandler:

    def __init__(self, filename):
        self.file_path = filename

    def read_file(self):
        file_contents = []

        try:
            # Open the file with option 'rU' Enable Universal newline support
            with open(self.file_path, 'rU') as file_instance:
                reader = csv.DictReader(file_instance)

                for row in reader:
                    file_contents.append(row)

                return file_contents

        except IOError as err:
            exit(err)
