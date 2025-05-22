import os


def read_all_lines(inputfolder):
    lines = []
    for filename in os.listdir(inputfolder):
        file_path = os.path.join(inputfolder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            lines.extend(file.readlines())
    return lines
