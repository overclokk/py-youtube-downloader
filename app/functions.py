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


def get_timestamp_from_file(file_path: str):
    return True
