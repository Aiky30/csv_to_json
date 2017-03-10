import os

import csv
import json

###
#   Config
###


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')

CSV_FILE = os.path.join(DATA_DIR, 'Outbreak.csv')
JSON_FILE = os.path.join(DATA_DIR, 'Outbreak.json')
JS_FILE = os.path.join(DATA_DIR, 'Outbreak.js')

class JSWriter:

    def __init__(self):

        self.file_path = JS_FILE

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


class JSONWriter:

    def __init__(self):

        self.file_path = JSON_FILE

    def write_file(self, master_contents):
        try:

            # Open the file with option 'rU' Enable Universal newline support
            with open(self.file_path, 'w') as file_instance:

                file_instance.write(
                    #json.dumps(master_contents)
                    json.dumps(master_contents, indent=2)
                )

        except IOError as err:
            exit(err)


class CSVReader:

    def __init__(self):

        self.file_path = CSV_FILE

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


def main():

    csv_reader = CSVReader()
    js_writer = JSWriter()

    # Read the CSV file
    file_contents = csv_reader.read_file()

    # Write the contents of the CSV file to the JSON file
    js_writer.write_file(file_contents)

    exit(0)

if __name__ == "__main__":
    main()
