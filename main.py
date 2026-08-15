import random


QUOTES = [
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("Great things are done by a series of small things brought together.", "Vincent van Gogh"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("What you get by achieving your goals is not as important as what you become by achieving your goals.", "Zig Ziglar"),
]


def get_random_quote():
    """Return one random (quote, author) tuple from the quote collection."""
    return random.choice(QUOTES)


def main():
    """Select and display a random inspirational quote."""
    quote, author = get_random_quote()
    print(f'"{quote}" — {author}')


if __name__ == "__main__":
    main()
