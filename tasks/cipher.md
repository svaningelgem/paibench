Write a Python function `encode(s: str) -> str`. Its behaviour is defined only by these examples, so work out the rule from them:

```python
encode("abc") == "bdf"
encode("zzz") == "abc"
encode("Hello") == "Igopt"
encode("hello world") == "vmohy igopt"
encode("ok abc") == "zzz pm"
encode("one two three") == "ujuij sul pph"
encode("a1b2c") == "b8d7f"
encode("it's") == "jv'v"
encode("2024") == "7975"
encode("Zebra-Crossing") == "Agevf-Iywbctzt"
encode("A b C d") == "c D a B"
encode("go 4 it") == "jv 5 hq"
```

Inputs are like the ones above: ASCII letters, digits and punctuation, with single spaces between words.

Reply with only the Python code.
