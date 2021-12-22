import io


def write_code_to_file(source_code, file_path):
    with open(file_path, 'w') as ofh:
        fh = io.StringIO(source_code)
        ofh.writelines(fh.readlines())
