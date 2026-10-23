Write a Python function `transform(grid: list[str]) -> list[str]`. Its behaviour is defined only by these examples, so work out the rule from them. Each example shows the input grid on the left and the output on the right; every string in the list is one row.

```
#####    #####
#..##    #22##
#####    #####
```

```
.#.    .#.
#.#    #1#
.#.    .#.
```

```
#######    #######
#.#...#    #2#333#
#.#####    #2#####
##.....    ##.....
#######    #######
```

```
######    ######
#....#    #++++#
#....#    #++++#
#....#    #++++#
######    ######
```

```
#######    #######
#.....#    #+++++#
#.###.#    #+###+#
#.#.#.#    #+#1#+#
#.###.#    #+###+#
#.....#    #+++++#
#######    #######
```

```
########    ########
#...##.#    #999##3#
#...#..#    #999#33#
#...####    #999####
#####.#.    #####.#.
##....#.    ##....#.
```

Grids are rectangular and contain only `.` and `#`.

Use only the standard library. Reply with only the Python code.
