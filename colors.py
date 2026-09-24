class bcolors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    DEEP_PURPLE = '\033[38;5;135m'
    ELECTRIC_PURPLE = '\033[38;5;141m'
    NEON_BLUE = '\033[38;5;39m'
    SKY_BLUE = '\033[38;5;81m'
    CYAN = '\033[38;5;51m'
    AQUA = '\033[38;5;87m'
    NEON_GREEN = '\033[38;5;46m'
    MINT = '\033[38;5;121m'
    HOT_PINK = '\033[38;5;201m'
    PINK = '\033[38;5;213m'
    ORANGE = '\033[38;5;208m'
    GOLD = '\033[38;5;220m'
    RED = '\033[38;5;196m'
    CORAL = '\033[38;5;203m'
    WHITE = '\033[38;5;255m'
    GREY = '\033[38;5;245m'
    GREEN = "\033[32m"


COLOR_CHOICES: list[tuple[str, str, str]] = [
    (bcolors.DEEP_PURPLE, bcolors.HOT_PINK, bcolors.NEON_BLUE),
    (bcolors.NEON_BLUE, bcolors.CYAN, bcolors.AQUA),
    (bcolors.NEON_GREEN, bcolors.MINT, bcolors.NEON_BLUE),
    (bcolors.DEEP_PURPLE, bcolors.HOT_PINK, bcolors.GOLD),
    (bcolors.RED, bcolors.ORANGE, bcolors.GOLD),
    (bcolors.GREEN, bcolors.RED, bcolors.RESET),
]
