STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"
MAX_VOLUME = 1_000_000
MAX_DIMENSION = 150
MAX_WEIGHT = 20


def is_bulky(width, height, length):
    volume = width * height * length
    largest_dimension = max(width, height, length)
    return volume >= MAX_VOLUME or largest_dimension >= MAX_DIMENSION


def is_heavy(weight):
    return weight >= MAX_WEIGHT


def classify_package(width, height, length, weight):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(weight)
    if bulky and heavy:
        return REJECTED
    if bulky or heavy:
        return SPECIAL
    return STANDARD
