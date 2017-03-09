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


class JSONWriter:

    def __init__(self):

        self.file_path = JSON_FILE

    def write_file(self, master_contents):
        try:

            # Open the file with option 'rU' Enable Universal newline support
            with open(self.file_path, 'w') as file_instance:

                file_instance.write(
                    json.dumps(master_contents, indent=2)
                )

        except IOError as err:
            self.import_logger.file_match_not_found(self.file_path)


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
            self.import_logger.file_match_not_found(self.file_path)


def main():

    csv_reader = CSVReader()
    json_writer = JSONWriter()

    # Read the CSV file
    file_contents = csv_reader.read_file()

    # Write the contents of the CSV file to the JSON file
    json_writer.write_file(file_contents)

    exit(0)

if __name__ == "__main__":
    main()
