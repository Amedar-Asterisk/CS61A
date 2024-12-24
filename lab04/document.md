### Q1: Dictionaries
Use Ok to test your knowledge with the following "What Would Python Display?" questions:

```python ok -q pokemon -u```

### Q2: Divide
Implement ```divide```, which takes two lists of positive integers ```quotients``` and ```divisors```. It returns a dictionary whose keys are the elements of ```quotients```. For each key ```q```, its corresponding value is a list of all the elements of ```divisors``` that can be evenly divided by ```q```.

```python ok -q divide```

### Q3: Buying Fruit
Implement the ```buy``` function that takes three parameters:

1. ```fruits_to_buy```: A list of strings representing the fruits you need to buy. At least one of each fruit must be bought.
2. ```prices```: A dictionary where the keys are fruit names (strings) and the values are positive integers representing the cost of each fruit.
3. ```total_amount```: An integer representing the total money available for purchasing the fruits. Take a look at the docstring for more details on the input structure.

The function should print **all possible ways** to buy the required fruits so that the combined cost equals ```total_amount```. You can only select fruits mentioned in ```fruits_to_buy``` list.

```python ok -q buy```


### Cities
Say we have a data abstraction for cities. A city has a name, a latitude coordinate, and a longitude coordinate.

Our data abstraction has one constructor:

- `make_city(name, lat, lon)`: Creates a city object with the given name, latitude, and longitude.

We also have the following selectors in order to get the information for each city:

- `get_name(city)`: Returns the city's name
- `get_lat(city)`: Returns the city's latitude
- `get_lon(city)`: Returns the city's longitude

### Q4: Distance
We will now implement the function `distance`, which computes the distance between two city objects. Recall that the distance between two coordinate pairs (x1, y1) and (x2, y2) can be found by calculating the `sqrt` of `(x1 - x2)**2 + (y1 - y2)**2`. We have already imported `sqrt` for your convenience. Use the latitude and longitude of a city as its coordinates; you'll need to use the selectors to access this info!

`python ok -q distance`

### Q5: Closer City
Next, implement `closer_city`, a function that takes a latitude, longitude, and two cities, and returns the name of the city that is closer to the provided latitude and longitude.

You may only use the selectors `get_name` `get_lat` `get_lon`, constructors `make_city`, and the `distance` function you just defined for this question.

`python ok -q closer_city`

### Q6: Don't violate the abstraction barrier!

**Note:** this question has no code-writing component (if you implemented the previous two questions correctly).

When writing functions that use a data abstraction, we should use the constructor(s) and selector(s) whenever possible instead of assuming the data abstraction's implementation. Relying on a data abstraction's underlying implementation is known as violating the abstraction barrier.

It's possible that you passed the doctests for the previous questions even if you violated the abstraction barrier. To check whether or not you did so, run the following command:

Use Ok to test your code:

`python ok -q check_city_abstraction`

The `check_city_abstraction` function exists only for the doctest, which swaps out the implementations of the original abstraction with something else, runs the tests from the previous two parts, then restores the original abstraction.

The nature of the abstraction barrier guarantees that changing the implementation of an data abstraction shouldn't affect the functionality of any programs that use that data abstraction, as long as the constructors and selectors were used properly.

If you passed the Ok tests for the previous questions but not this one, the fix is simple! Just replace any code that violates the abstraction barrier with the appropriate constructor or selector.

Make sure that your functions pass the tests with both the first and the second implementations of the data abstraction and that you understand why they should work for both before moving on.