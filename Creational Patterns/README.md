# Creational Patterns
## What are Creational Patterns?
Object creation and modification seems like a rather trivial task, but imagine what can happen to your entire codebase if, for example, objects that should not be re-created are created. Creation is trivial, but it is also a major component in any codebase. If objects are created in a naive way, it will make a bottleneck for developers when they are trying to extend their codebase.

Creational design patterns are used to solve the issue of making it easier to create and modify objects in a codebase.

These are two common creational design patterns:
* [Builder Design Pattern](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Patterns/Builder%20Pattern): Use this design pattern to abstract away the creation of an object from itself and make modification of the object easier.
* [Singleton Design Pattern](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Patterns/Singleton%20Pattern): Use this design pattern to make sure that there is only one instance of a class that is used by clients throughout the lifetime of the program