def encode(s: str) -> str:
    words = []
    for w, word in enumerate(s.split(" ")):
        sign = 1 if w % 2 == 0 else -1
        k, chars = 0, []
        for ch in word:
            if ch.isascii() and ch.isalpha():
                k += 1
                base = ord("a") if ch.islower() else ord("A")
                chars.append(chr((ord(ch) - base + sign * k) % 26 + base))
            elif ch.isdigit():
                chars.append(str(9 - int(ch)))
            else:
                chars.append(ch)
        words.append("".join(chars))
    return " ".join(reversed(words))
