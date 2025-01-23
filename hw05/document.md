### Q1: Infinite Hailstone
Write a generator function that yields the elements of the hailstone sequence starting at number `n`. After reaching the end of the hailstone sequence, the generator should yield the value 1 indefinitely.

Here is a quick reminder of how the hailstone sequence is defined:

- Pick a positive integer `n` as the start.
- If `n` is even, divide it by 2.
- If `n` is odd, multiply it by 3 and add 1.
- Continue this process until `n` is 1.

Try to write this generator function recursively. If you are stuck, you can first try writing it iteratively and then seeing how you can turn that implementation into a recursive one.

**Hint:** Since `hailstone` returns a generator, you can `yield from` a call to `hailstone`!

`python3 ok -q hailstone`

### Q2: Merge
Definition: An *infinite iterator* is a iterator that never stops providing values when `next` is called. For example, ones() evaluates to an infinite iterator:

```
def ones():
    while True:
        yield 1
```

Write a generator function `merge(a, b)` that takes two infinite iterators, `a` and `b`, as inputs. Both iterators yield elements in strictly increasing order with no duplicates. The generator should produce all unique elements from both input iterators in increasing order, ensuring no duplicates.

**Note:** The input iterators do not contain duplicates within themselves, but they may have common elements between them.

`python3 ok -q merge`

### Q3: Stair Ways
Imagine that you want to go up a staircase that has `n` steps, where `n` is a positive integer. You can take either **one** or **two steps** each time you move.

Write a generator function `stair_ways` that yields all the different ways you can climb the staircase.

Each "way" of climbing a staircase can be represented by a list of 1s and 2s, where each number indicates whether you take one step or two steps at a time.

For example, for a staircase with 3 steps, there are three ways to climb it:

- You can take one step each time: `[1, 1, 1]`.
- You can take two steps then one step: `[2, 1]`.
- You can take one step then two steps: `[1, 2].`.

Therefore, `stair_ways(3)` should yield `[1, 1, 1]`, `[2, 1]`, and `[1, 2]`. These can be yielded in any order.

`python3 ok -q stair_ways`

### Q4: Yield Paths
Write a generator function `yield_paths` that takes a tree `t` and a target `value`. It yields each path from the root of `t` to any node with the label `value`.

Each path should be returned as a list of labels from the root to the matching node. The paths can be yielded in any order.

*Hint:* If you are having trouble getting started, think about how you would approach this problem if it was not a generator function. What would the recursive steps look like?

*Hint:* Remember, you can iterate over generator objects because they are a type of iterator!

`python3 ok -q yield_paths`