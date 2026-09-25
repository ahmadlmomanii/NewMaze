class bcolors:
    """Define ANSI escape sequences for terminal colors and text styles.

    Attributes:
        RESET: Reset all terminal colors and text styles.
        BOLD: Apply bold text formatting.
        UNDERLINE: Apply underline text formatting.
        DEEP_PURPLE: Display text in deep purple.
        ELECTRIC_PURPLE: Display text in electric purple.
        NEON_BLUE: Display text in neon blue.
        SKY_BLUE: Display text in sky blue.
        CYAN: Display text in cyan.
        AQUA: Display text in aqua.
        NEON_GREEN: Display text in neon green.
        MINT: Display text in mint.
        HOT_PINK: Display text in hot pink.
        PINK: Display text in pink.
        ORANGE: Display text in orange.
        GOLD: Display text in gold.
        RED: Display text in red.
        CORAL: Display text in coral.
        WHITE: Display text in white.
        GREY: Display text in grey.
        GREEN: Display text in green.
    """

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
    GREEN = '\033[32m'


COLOR_CHOICES: list[tuple[str, str, str]] = [
    (bcolors.DEEP_PURPLE, bcolors.HOT_PINK, bcolors.NEON_BLUE),
    (bcolors.NEON_BLUE, bcolors.CYAN, bcolors.AQUA),
    (bcolors.NEON_GREEN, bcolors.MINT, bcolors.NEON_BLUE),
    (bcolors.DEEP_PURPLE, bcolors.HOT_PINK, bcolors.GOLD),
    (bcolors.RED, bcolors.ORANGE, bcolors.GOLD),
    (bcolors.GREEN, bcolors.RED, bcolors.RESET),
]
