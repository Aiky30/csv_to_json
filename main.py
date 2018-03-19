import os

import csv
import json


class JSWriter:

    def __init__(self, filename):

        self.file_path = filename

    def write_file(self, master_contents):
        try:

            # Open the file with option 'rU' Enable Universal newline support
            with open(self.file_path, 'w') as file_instance:

                file_instance.write('var data = ')

                file_instance.write(
                    #json.dumps(master_contents)
                    json.dumps(master_contents, indent=2)
                )

                file_instance.write(';')

        except IOError as err:
            exit(err)


class CSVReader:

    def __init__(self, filename):

        self.file_path = filename

    def read_file(self):

        file_output = []

        try:

            # Open the file with option 'rU' Enable Universal newline support
            with open(self.file_path, 'rU') as file_instance:

                reader = csv.DictReader(file_instance)

                for row in reader:
                    file_output.append(row)

                return file_output

        except IOError as err:
            exit(err)


def main(config):

    csv_reader = CSVReader(config.input)
    js_writer = JSWriter(config.output)

    # Read the CSV file
    file_contents = csv_reader.read_file()

    # Write the contents of the CSV file to the JSON file
    js_writer.write_file(file_contents)

    exit(0)
