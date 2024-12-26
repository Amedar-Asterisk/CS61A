# Sequences

### Q1: Shuffle
Implement `shuffle`, which takes a sequence `s` (such as a list or range) with an even number of elements. It returns a new list that interleaves the elements of the first half of s with the elements of the second half. It does not modify `s`.

To interleave two sequences `s0` and `s1` is to create a new list containing the first element of `s0`, the first element of `s1`, the second element of `s0`, the second element of `s1`, and so on. For example, if `s0 = [1, 2, 3]` and `s1 = [4, 5, 6]`, then interleaving `s0` and `s1` would result in `[1, 4, 2, 5, 3, 6]`.

`python ok -q shuffle`

### Q2: Deep Map
**Definition:** A nested list of numbers is a list that contains numbers and lists. It may contain only numbers, only lists, or a mixture of both. The lists must also be nested lists of numbers. For example: `[1, [2, [3]], 4]`, `[1, 2, 3]`, and `[[1, 2], [3, 4]]` are all nested lists of numbers.

Write a function `deep_map` that takes two arguments: a nested list of numbers `s` and a one-argument function `f`. It modifies `s` in place by applying f to each number within s and replacing the number with the result of calling `f` on that number.

`deep_map` returns `None` and should not create any new lists.

**Hint:** `type(a) == list` will evaluate to `True` if `a` is a list.

`python ok -q deep_map`

# Data Abstraction

## Mobiles

We are making a planetarium mobile. A mobile is a type of hanging sculpture. A binary mobile consists of two arms. Each arm is a rod of a certain length, from which hangs either a planet or another mobile. For example, the below diagram shows the left and right arms of Mobile A, and what hangs at the ends of each of those arms.

We will represent a binary mobile using the data abstractions below.

- A `mobile` must have both a left `arm` and a right `arm`.
- An `arm` has a positive length and must have something hanging at the end, either a `mobile` or `planet`.
- A `planet` has a positive mass, and nothing hanging from it.

Below are the various constructors and selectors for the `mobile` and `arm` data abstraction. They have already been implemented for you, though the code is not shown here. As with any data abstraction, you should focus on what the function does rather than its specific implementation. You are free to use any of their constructor and selector functions in the Mobiles coding exercises.

### Q3: Mass
Implement the `planet` data abstraction by completing the `planet` constructor and the `mass` selector. A planet should be represented using a two-element list where the first element is the string `'planet'` and the second element is the planet's mass. The `mass` function should return the mass of the `planet` object that is passed as a parameter.

The `total_mass` function demonstrates the use of the mobile, arm, and planet abstractions. It has been implemented for you. *You may use the `total_mass` function in the following questions*.

`python ok -q total_mass`

### Q4: Balanced
Implement the `balanced` function, which returns whether `m` is a *balanced* mobile. A mobile is balanced if **both** of the following conditions are met:

1. The *torque* applied by its left arm is equal to the *torque* applied by its right arm. The torque of the left arm is the length of the left rod multiplied by the total mass hanging from that rod. Likewise for the right. For example, if the left arm has a length of `5`, and there is a `mobile` hanging at the end of the left arm of total mass `10`, the torque on the left side of our mobile is `50`.
2. Each of the mobiles hanging at the end of its arms is itself *balanced*.

Planets themselves are balanced, as there is nothing hanging off of them.

**Reminder:** You may use the `total_mass` function above. Don't **violate abstraction barriers**. Instead, use the selector functions that have been defined.

`python ok -q balanced`

# Trees

### Q5: Finding Berries!
The squirrels on campus need your help! There are a lot of trees on campus and the squirrels would like to know which ones contain berries. Define the function `berry_finder`, which takes in a tree and returns `True` if the tree contains a node with the value `'berry'` and `False` otherwise.

**Hint:** To iterate through each of the branches of a particular tree, you can consider using a `for` loop to get each branch.

`python ok -q berry_finder`

### Q6: Maximum Path Sum
Write a function that takes in a tree and returns the maximum sum of the values along any *root-to-leaf* path in the tree. A *root-to-leaf* path is a sequence of nodes starting at the root and proceeding to some leaf of the tree. You can assume the tree will have positive numbers for its labels.

`python ok -q max_path_sum`