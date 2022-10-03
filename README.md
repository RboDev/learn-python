# Inheritance

Python allows __multiple inheritance__.
This is a cool feature that has also some traps.  
Often new Python learners are introduces to multiple inheritance and want to (over)use it.

https://realpython.com/inheritance-composition-python/


__Object composition__ is generally a better choice

<iframe width="560" height="315" src="https://www.youtube.com/embed/0mcP8ZpUR38" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## How to choose between Composition and Inheritance ?
A simple question to ask yourself to select between inheritance and composition is:

* Does my `new class` object __IS__ a `parent class` object ?  
 or 
* Does my new object __HAS__ another object inside ?

## Use cases for inheritance

### Test Adapter Board driver

A Test Adapter Board `TAB` is an hardware device that is used to control different types of devices under test `DUT`.

The `TAB` board is generic and provides basic services to the `DUT` board like DC voltage sources, Digital IO...

