"""
A CLI for adding `_brand.yml` to a project.
"""

import os
from argparse import ArgumentParser
from importlib import resources
from pathlib import Path


def main(folder_path: Path, overwrite: bool) -> Path | None:
    """
    Main function to add a `_brand.yml` to the project.

    Parameters
    ----------
    folder_path : Path
        Path to the folder folder to add the file to.
    overwrite : bool
        Whether to overwrite the file if it exists.

    Returns
    -------
    Path | None
        Path to the file if it has been created/overwritten. Otherwise, returns None.
    """
    if not folder_path.exists():
        raise FileNotFoundError(f"{folder_path} path does not exist.")
    if not folder_path.is_dir():
        raise NotADirectoryError("`folder_path` must be a directory.")
    file_path = folder_path.joinpath("_brand.yml")
    if os.path.exists(file_path):
        if not overwrite:
            print(
                "`_brand.yml` already exists at the project location."
                " No action will be taken."
                " Use `overwrite` flag to force an overwrite."
            )
            return None
        print(f"{file_path} already exists. Overwriting...")
    data = resources.files().joinpath("_brand.yml").read_bytes()
    with open(file_path, "wb") as file:
        file.write(data)
    print(f"Created {file_path}.")
    return file_path


if __name__ == "__main__":
    parser = ArgumentParser(description="A CLI for adding `_brand.yml` to a project.")
    parser.add_argument(
        "path",
        nargs="?",  # make it optional
        default=os.curdir,
        type=Path,
        help="Project path. If not provided, the current directory will be used.",
    )
    parser.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="Use this flag to overwrite a file if it exists.",
    )
    args = parser.parse_args()
    main(args.path, args.overwrite)
