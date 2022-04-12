# https://pynative.com/python-convert-seconds-to-hhmmss/
# Format accepted:
# HH:MM:SS
# MM:SS
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


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
    return parse_lines(lines)


def parse_lines(lines: list) -> list:
    new_list = []
    for line in lines:
        stripped_line = line.strip()

        # Continue in case line start with a letter
        if not stripped_line[:1].isdigit():
            continue

        colon_position = stripped_line.find(':')
        # Continue in case there is no colon : in the line
        if colon_position < 1:
            continue

        # Continue in case colon : is not in the right position (second or third position)
        if colon_position > 3:
            continue

        # Continue in case first char after colon is not a digit
        if not stripped_line[colon_position+1].isdigit():
            continue

        # Continue in case second char after colon is not a digit
        if not stripped_line[colon_position+2].isdigit():
            continue

        # If line is in the chapter format we have a space
        splitted_line = stripped_line.split()
        if len(splitted_line) > 1:
            new_list.append([splitted_line[0]])
            continue

        new_list.append(stripped_line.split(','))

    return new_list


def convert_chapter_format_to_start_end_format(format_to_convert: list) -> list:
    converted = []
    actual_length = len(format_to_convert) - 1
    for i in range(actual_length):
        format_to_convert[i].append(format_to_convert[i + 1][0])
        converted.append(format_to_convert[i])

    return converted


def generate_clips(file_path: str, list_of_time_ranges: list[list], clip_name='clip'):
    total_clips: int = len(list_of_time_ranges)
    for i in range(total_clips):
        ffmpeg_extract_subclip(
            file_path,
            get_seconds(list_of_time_ranges[i][0]),
            get_seconds(list_of_time_ranges[i][1]),
            targetname=f'{clip_name}-{i}.mp4'
        )
