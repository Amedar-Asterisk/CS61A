## Mutability

### Q1: WWPD: List-Mutation

**Important:** For all WWPD questions, type `Function` if you believe the answer is `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.

Use Ok to test your knowledge with the following "What Would Python Display?" questions:
`python ok -q list-mutation -u`

### Q2: Insert Items

Write a function that takes in a list `s`, a value `before`, and a value `after`. It modified `s` in place by inserting `after` just after each value equal to `before` in s. It returns `s`.

**Important:** No new lists should be created.

**Note:** If the values passed into before and after are equal, make sure you're not creating an infinitely long list while iterating through it. If you find that your code is taking more than a few seconds to run, the function may be in an infinite loop of inserting new values.

`python ok -q insert_items`

### Q3: Group By

Write a function that takes a list `s` and a function `fn`, and returns a dictionary that groups the elements of `s` based on the result of applying `fn`.

- The dictionary should have one key for each unique result of applying `fn` to elements of `s`.

- The value for each key should be a list of all elements in `s` that, when passed to `fn`, produce that key value.
  
In other words, for each element e in s, determine `fn(e)` and add e to the list corresponding to `fn(e)` in the dictionary.

`python ok -q group_by`

## Iterators

### Q4: WWPD: Iterators

**Important:** Enter `StopIteration` if a `StopIteration` exception occurs, `Error` if you believe a different error occurs, and `Iterator` if the output is an iterator object.

**Important:** Python's built-in function `map`, `filter`, and `zip` return *iterators*, not lists.

`python ok -q iterators-wwpd -u`

### Q5: Count Occurrences

Implement `count_occurrences`, which takes an iterator `t`, an integer `n`, and a value `x`. It returns the number of elements in the first `n` elements of `t` that are equal to `x`.

You can assume that `t` has at least `n` elements.

**Important:** You should call `next` on `t` exactly `n` times. If you need to iterate through more than `n` elements, think about how you can optimize your solution.

`python ok -q count_occurrences`

### Q6: Repeated

Implement `repeated`, which takes in an iterator `t` and an integer `k` greater than 1. It returns the first value in `t` that appears `k` times in a row. You may assume that there is an element of `t` repeated at least `k` times in a row.

**Important:** Call `next` on `t` only the minimum number of times required. If you are receiving a `StopIteration` exception, your `repeated` function is calling `next` too many times.

`python ok -q repeated`

## Check Your Score Locally

`python ok --score`

## Optional Questions

### Q7: Sprout Leaves
Define a function `sprout_leaves` that takes in a tree, `t`, and a list of leaves, `leaves`. It produces a new tree that is identical to `t`, but where each old leaf node has new branches, one for each leaf in `leaves`.

`python ok -q sprout_leaves`

### Q8: Partial Reverse

Partially reversing the list `[1, 2, 3, 4, 5]` starting from index 2 until the end of the list will give `[1, 2, 5, 4, 3]`.

Implement the function `partial_reverse` which reverses a list starting from index `start` until the end of the list. This reversal should be *in-place*, meaning that the original list is modified. Do not create a new list inside your function, even if you do not return it. The `partial_reverse` function returns `None`.

**Hint:** You can swap elements at index `i` and `j` in list s with multiple assignment: `s[i], s[j] = s[j], s[i]`

`python ok -q partial_reverse`