def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    control_character = ['\n', '\t', '\r']
    for char in control_character:
        text = text.replace(char, ' ')
    words = text.split()
    text = ' '.join(words)

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()
    
    return text