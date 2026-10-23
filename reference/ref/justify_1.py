def _fill(words: list[str], width: int) -> str:
    if len(words) == 1:
        return words[0].ljust(width)
    gaps = len(words) - 1
    base, extra = divmod(width - sum(map(len, words)), gaps)
    line = words[0]
    for i, word in enumerate(words[1:]):
        line += " " * (base + (i >= gaps - extra)) + word
    return line


def _paragraph(words: list[str], width: int) -> list[str]:
    lines, current = [], []
    for word in words:
        if len(word) > width and current:
            lines.append(_fill(current, width))
            current = []
        while len(word) > width:
            lines.append(word[: width - 1] + "-")
            word = word[width - 1 :]
        if current and len(" ".join(current)) + 1 + len(word) > width:
            lines.append(_fill(current, width))
            current = []
        current.append(word)
    lines.append(" ".join(current).ljust(width))
    return lines


def justify(text: str, width: int) -> list[str]:
    paragraphs, words = [], []
    for line in [*text.splitlines(), ""]:
        if line.strip():
            words += line.split()
        elif words:
            paragraphs.append(words)
            words = []
    result = []
    for words in paragraphs:
        if result:
            result.append("")
        result += _paragraph(words, width)
    return result
