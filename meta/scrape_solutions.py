"""
Function to scrape the solved Kata in the `kata` durectory, and write this to a markdown file
which is used to update the README.md file in the root directory of the repository.
"""

import os
import re
from typing import List


def get_kata_files() -> List[str]:
    """
    Get all the files in the `kata` directory
    """
    kata_files = []
    for root, _, files in os.walk("kata"):
        for file in files:
            if file.endswith(".py"):
                kata_files.append(os.path.join(root, file))
    return kata_files


def get_kata_info(file: str) -> tuple[str, str]:
    """
    Get the Kata name and level from the file
    """
    with open(file, "r") as f:
        data = "".join(f.readlines()[:6])
        kata_link = re.search(r"Link: (.*)", data).group(1)
        kata_name = re.search(r"Name: (.*)", data).group(1)
        kata_level = re.search(r"Level: (.*)", data).group(1)
        kata_desc = re.search(r"Desc.: (.*)", data).group(1)
        kata_completed = re.search(r"Finished: (.*)", data).group(1)
    return (kata_link, kata_name, kata_level, kata_desc, kata_completed), file


def write_kata_info(kata_info: tuple[str, str], filename: str, bullet_num: int) -> None:
    """
    Write the Kata information to a markdown file
    """
    kata_info, file = kata_info
    with open(filename, "a") as f:
        f.write(
            f"{bullet_num}. **{kata_info[1]}** [:globe_with_meridians:]({kata_info[0]}) {'(in progress)' if kata_info[4] == 'No' else ''}\n"
        )
        f.write(f"\t- **Kata Level**: {kata_info[2]}\n")
        f.write(f"\t- **Description**: {kata_info[3]}\n")
        f.write(f"\t- **File**: [{file}]({file})\n\n")


def main() -> None:
    kata_files = get_kata_files()

    # check if md exists, if it does, delete it
    if os.path.exists(filename := "meta/solutions.md"):
        os.remove(filename)

    for i, file in enumerate(kata_files):
        kata_info = get_kata_info(file)
        write_kata_info(kata_info, filename, i + 1)


if __name__ == "__main__":
    main()
