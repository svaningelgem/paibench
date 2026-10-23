Write a Python function `satisfies(version: str, rng: str) -> bool` that tells whether `version` satisfies the range `rng`, with the semantics of npm's `semver` package (node-semver) in its default mode: not loose, and without `includePrerelease`.

- `version` is a SemVer 2.0.0 version without a `v` prefix. Raise `ValueError` if it is not valid.
- `rng` is always a valid range: comparator sets joined by `||`, where a set is whitespace-separated comparators (operators `<`, `<=`, `>`, `>=`, `=` or none), hyphen ranges (`1.2.3 - 2.3.4`), tilde ranges (`~1.2.3`), caret ranges (`^1.2.3`) and X-ranges (`*`, `1.x`, `1.2.X`, `1.2`). Versions inside a range may be partial and may carry a prerelease tag.

Use only the standard library. Reply with only the Python code.
