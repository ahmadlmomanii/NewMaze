from dotenv import load_dotenv
import os


def check_config(
        values: tuple[int, int, tuple[int, int], tuple[int, int],
                      int, bool, str]
        ) -> None:
    """
    Validate the maze configuration values.

    Args:
        values: A tuple containing the maze width, height, entry position,
            exit position, seed, perfect-maze setting, and output filename.

    Raises:
        ValueError: If any configuration value is invalid.

    returns:
        None
    """
    try:
        (width, height, start_position,
            end_position, seed, perfect, output_file) = values
        if height < 1:
            raise ValueError("The height should be more than 1")
        if width < 1:
            raise ValueError("The width should be more than 1")
        if width == 1 and height == 1:
            raise ValueError("The 1*1 will not make a maze")
        if start_position == end_position:
            raise ValueError("The entry and exit should be different")
        if perfect is False:
            if width == 1 or height == 1:
                raise ValueError(
                    "There is just one path and it is not pacman usable")
            if width == 2 and height == 2:
                raise ValueError("2 * 2 in not pacman usable")
        if not (
            0 <= start_position[0] < height and 0 <= start_position[1] < width
        ):
            raise ValueError("Entry is out of the maze")
        if not (
            0 <= end_position[0] < height and 0 <= end_position[1] < width
        ):
            raise ValueError("Exit is out of the maze")
    except Exception as e:
        print(e)


def load_config() -> tuple[int, int, tuple[int, int],
                           tuple[int, int], int, bool, str]:
    """
    Load and validate the maze configuration from the environment.

    Reads the configuration from the config file, converts the values
    to their required types, validates the configuration, and returns
    the resulting maze settings.

    Returns:
        A tuple containing the maze width, height, entry position,
        exit position, random seed, perfect-maze setting, and output
        filename.
    """
    load_dotenv("config.txt")

    try:
        height = int(os.environ["HEIGHT"])
        width = int(os.environ["WIDTH"])
        seed = int(os.environ["SEED"])
    except Exception:
        print("Put a valid number for Hieght/Width/Seed !!")
        exit()
    try:
        start_position = tuple(
                int(x) for x in os.environ["ENTRY"].split(",")
            )
    except Exception:
        print("The Entry is not valid")

    try:
        end_position = tuple(
                int(x) for x in os.environ["EXIT"].split(",")
                )
    except Exception:
        print("The Exit is not valid")
    try:
        if not os.environ["OUTPUT_FILE"]:
            raise ValueError("Put a valid name for output file")
        output_file = str(os.environ["OUTPUT_FILE"])
    except Exception as e:
        print(e)
        exit()
    start_position = start_position[1], start_position[0]
    end_position = end_position[1], end_position[0]
    try:
        perfect = bool(os.environ["PERFECT"])
    except Exception:
        print("Perfect input is not right")
    try:
        seed = int(os.environ["SEED"])
    except Exception:
        print("Seed input is not right")
    check_config((width, height, start_position, end_position, seed, perfect,
                 output_file))

    return (width,
            height, start_position, end_position, seed, perfect, output_file)
