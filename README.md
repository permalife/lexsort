## Description
The class `LexSort` construct a custom comparison operator using the specified order of symbols. It then calls the in-place method `sort` on the given list. Average case time complexity is `O(n)`. Worst case time complexity is `O(n Log(n))`. Worst space complexity is `O(n)`.

## Example usage:
```
from lexsort import LexSort
ls = LexSort()
ls.sort(["aaa", "aa", ""], "a")
```


