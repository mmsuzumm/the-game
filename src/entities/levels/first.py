from entities.platform import Platform


def load_level():
    platforms = [
        Platform(50, 300, 200, 20),
        Platform(300, 200, 150, 20),
        Platform(500, 100, 100, 20),
    ]
    return platforms
