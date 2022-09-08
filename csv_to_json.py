import csv
import json
import sys


class JsonWriter:

    def __init__(self, filename):
        self.file_path = filename

    def write_file(self, master_contents):
        try:
            with open(self.file_path, 'w') as file_instance:
                file_instance.write(
                    json.dumps(master_contents, indent=2)
                )
        except IOError as err:
            exit(err)


class CsvReader:

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


def main(input_file_path, output_file_path):
    csv_reader = CsvReader(input_file_path)
    json_writer = JsonWriter(output_file_path)

    # Read the CSV file
    file_contents = csv_reader.read_file()

    # Write the contents of the CSV file to the JSON file
    json_writer.write_file(file_contents)

    exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SyntaxError("This command requires an input file followed by an output file provided.")

    main(sys.argv[1], sys.argv[2])
