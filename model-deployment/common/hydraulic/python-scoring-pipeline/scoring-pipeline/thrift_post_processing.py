# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-


def strip_rows(auto_generated_file: str, stripped_file: str):
    constructor_keyword = '__init__'
    with open(auto_generated_file) as old_file, open(stripped_file, 'w') as new_file:
        num_rows_skipped = 0
        num_rows_to_delete = 0  # number of rows to be deleted equals the number of elements in the constructor
        delete_rows = False
        for line in old_file:
            if constructor_keyword in line:
                delete_rows = True
                column_names = [x for x in line.split(',')]
                num_rows_to_delete = len(column_names)-2
            elif delete_rows:
                # skip write the next `rows_to_delete` lines to the new file
                num_rows_skipped = num_rows_skipped + 1
                if num_rows_skipped == num_rows_to_delete:
                    delete_rows = False  # stop skipping writing of rows to the new file
                    num_rows_to_delete = 0
            else:
                new_file.write(line)


def main():
    strip_rows('gen-py/h2oai_scoring/ttypes.py','temp_ttypes.py')


if __name__ == "__main__":
    main()
