
from pathlib import Path


def path(file_name):
    return str(
        (Path(__file__).parents[2] / "tests" / "attachment" / file_name).resolve()
    )
