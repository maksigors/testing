def by_no_class_old(css_class : str) -> str:
    return f'[not(contains(@class, "{css_class}"))]'

def by_no_class(css_class : str) -> str:
    return f'[not(contains(concat(" ", normalize-space(@class), " "), " {css_class} "))]'

def by_class(css_class : str) -> str:
    return f'[contains(concat(" ", normalize-space(@class), " "), " {css_class} ")]'

def filter_by_class(css_class : str) -> str:
    return f'[contains(concat(" ", normalize-space(@class), " "), " {css_class} ")]'