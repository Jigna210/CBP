import time


def sleep_execution(time_seconds: int) -> None:
    """
    Helper function to sleep for given time seconds

    :param int time_seconds: time in seconds for sleep
    :return: None
    """
    time.sleep(time_seconds)


def convert_rgb_to_hex(rgb: str) -> str:
    """ Helper function to convert rgb color code (rgb(245, 245, 245)) to hex (#abcdef) """
    split_rgb = rgb[rgb.find('(') + 1:rgb.find(')')].split(", ")

    return "#{:02x}{:02x}{:02x}".format(int(split_rgb[0]), int(split_rgb[1]), int(split_rgb[2])).upper()
