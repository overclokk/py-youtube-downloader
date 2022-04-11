# https://pynative.com/python-convert-seconds-to-hhmmss/
# Format accepted:
# HH:MM:SS
# MM:SS
def get_seconds(time_str: str) -> int:
    time_elements = time_str.split(':')
    if len(time_elements) == 2:
        time_elements.insert(0, '0')

    # split in hh, mm, ss
    hh, mm, ss = time_elements
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def parse_file(file_path: str) -> list:
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()

    new_list = []
    for line in lines:
        stripped_line = line.strip()

        # Continue in case line start with a string: Es: "Some description 1234"
        if not stripped_line[:1].isdigit():
            continue

        # Continue in case the third char is not a colon: Es "523"
        colon_position = stripped_line.find(':')
        if not colon_position == 2:
            continue

        # Continue in case the fourth char is not a digit: Es "19:0"
        if not stripped_line[3].isdigit():
            continue

        # If line is in the chapter format we have a space
        splitted_line = stripped_line.split()
        if len(splitted_line) > 1:
            new_list.append( [ splitted_line[0] ] )
            continue

        new_list.append(stripped_line.split(','))

    return new_list
