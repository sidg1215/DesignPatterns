# Creational Patterns
## What are Creational Patterns?
Object creation and modification seems like a rather trivial task, but imagine what can happen to your entire codebase if for example the name of a class changes, or fields/properties within a class change. Creation is trivial, but it is also a major component in any codebase, and if done incorrectly, it could create a bottleneck for developers when they are trying to expand their codebase.

These are common three creational patterns that show you how you can make your codebase more extensible:
* [Builder Pattern](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Patterns/Builder%20Pattern): When you want to abstract away the creation of an object from itself and make modification of the object easier.
* [Singleton Pattern](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Patterns/Singleton%20Pattern): When you want to make sure that there is only one instance of a class that is used by clients throughout the lifetime of the program