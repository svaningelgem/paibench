Write a Python function `evaluate(cells: dict[str, str]) -> dict[str, float | str]` for a tiny spreadsheet. `cells` maps names such as `A1` or `C12` (one letter `A`-`Z`, then a row `1`-`99`) to what was typed in the cell; cells not in the dict are empty. Return the value of every cell in `cells`.

What was typed is:
- a number if it matches the regex `-?\d+(\.\d+)?`;
- a formula if it starts with `=`;
- otherwise text, whose value is the text itself.

Formula grammar, loosest-binding first. Whitespace between tokens is ignored.
- comparisons `=`, `<>`, `<`, `<=`, `>`, `>=`, which give `1` or `0`;
- `+` and `-`, then `*` and `/`; all binary operators are left-associative;
- unary `-`;
- numbers (`\d+(\.\d+)?`), cell references, parentheses, `IF(cond, then, else)`, and `SUM`, `MIN` and `MAX` with one or more arguments, each an expression or a range such as `A1:C3`.

A formula that does not fit the grammar has the value `#SYNTAX!`.

Evaluation:
- An empty cell reads as `0`. A reference gives the cell's value as it is, so `=A1` can be text.
- Operator operands, `IF` conditions and function arguments are evaluated left to right, stopping at the first value that is an error (the result is that error) or text (the result is `#VALUE!`).
- In `SUM`, `MIN` and `MAX`, an argument written as a lone reference or a range skips empty and text cells, but not errors. Ranges are read row by row, left to right, and `B3:A1` means `A1:B3`. `MIN` or `MAX` of no numbers is `0`.
- `IF` evaluates `cond`, then only one branch: `then` if `cond` is not `0`, otherwise `else`. The result is that branch's value, even if it is text.
- Division by zero gives `#DIV/0!`.
- A cell whose evaluation needs its own value, directly or through other cells, is `#CYCLE!`. Only references that actually get evaluated count.

Use only the standard library. Reply with only the Python code.
