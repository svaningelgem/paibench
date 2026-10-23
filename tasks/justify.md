Write a Python function `justify(text: str, width: int) -> list[str]` that lays `text` out in lines of exactly `width` characters (`width >= 2`).

- A paragraph is a run of lines that are not blank; blank lines (empty or only whitespace) separate paragraphs. A word is a maximal run of non-whitespace characters.
- Fill each paragraph greedily: put as many words on a line as fit with one space between them.
- A word longer than `width` starts a new line. While what is left of it is longer than `width`, its next `width - 1` characters plus `-` form a line of their own; the rest is then placed like a normal word.
- Every line of a paragraph except its last is justified: spaces are added between words until the line is `width` long. When the spaces don't divide evenly, the gaps further right get one more space than the gaps further left.
- The last line of a paragraph, and any line holding a single word, is left-aligned and padded with spaces on the right.
- Paragraphs are separated by one empty string `""` in the result. Text without words gives `[]`.

Reply with only the Python code.
