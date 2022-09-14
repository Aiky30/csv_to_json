import sys

from filetypes.csv_handler import CsvHandler
from filetypes.json_handler import JsonHandler
from filetypes.yaml_handler import YamlHandler


supported_file_map = {
    "csv": CsvHandler,
    "json": JsonHandler,
    "yaml": YamlHandler,
}
filetypes = [filetype for filetype, options in supported_file_map.items()]


def _get_filetype(filepath):
    for filetype in filetypes:
        if filepath.endswith(filetype):
            return filetype
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SyntaxError("This command requires an input file followed by an output file provided.")

    # Get the filetypes from the files supplied
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    input_filetype = _get_filetype(input_file_path)
    output_filetype = _get_filetype(output_file_path)

    input_reader = supported_file_map[input_filetype]
    output_writer = supported_file_map[output_filetype]

    input_reader_instance = input_reader(input_file_path)
    output_writer_instance = output_writer(output_file_path)

    # Read the file contents to a native python object
    file_contents = input_reader_instance.read_file()
    # Convert and write the contents
    output_writer_instance.write_file(file_contents)
