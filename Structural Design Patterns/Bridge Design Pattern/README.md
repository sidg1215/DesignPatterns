# Bridge design pattern
* [What is the Bridge design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Structural%20Design%20Patterns/Bridge%20Design%20Pattern#what-is-the-bridge-design-pattern)
* [Why would we want to use it?](https://github.com/sidg1215/DesignPatterns/tree/main/Structural%20Design%20Patterns/Bridge%20Design%20Pattern#why-would-we-want-to-use-it)
* [How can we use the Bridge design pattern to solve this issue?](https://github.com/sidg1215/DesignPatterns/tree/main/Structural%20Design%20Patterns/Bridge%20Design%20Pattern#how-can-we-use-the-bridge-design-pattern-to-solve-this-issue)
* [What have we accomplished?](https://github.com/sidg1215/DesignPatterns/tree/main/Structural%20Design%20Patterns/Bridge%20Design%20Pattern#what-have-we-accomplished)
## What is the Bridge design pattern?
The Bridge design pattern allows for the decoupling of a very large class hierarchy into individual class hierarchies.
## Why would we want to use it?
Imagine that we are trying to create a deli. The deli is going to have different sandwiches, which can be created as classes as such:
```java
class WhiteBreadHam {
    ...
}

class WhiteBreadChicken {
    
}

class WhiteBreadTurkey {
 ...   
}

class BrownBreadHam {
    ...
}

class BrownBreadChicken {
    
}

class BrownBreadTurkey {
 ...   
}
```
### ***The issue***: 
What if we wanted to add sour dough as one of our potential breads: this means that we have to create three more classes, one for each type of meat. And what if we wanted a tuna sandwich: we would have to another three classes, one for each type of bread!

If we follow this structure, adding new ingredients will become a pain. In fact, as more breads and more meats are added, the number of sandwiches that will
be created will grow at an exponential amount. This is very bad design and results in all sorts of loss in productivity, and thus our codebase is __not extensible__ in the long run.
## How can we use the Bridge design pattern to solve this issue?
We notice that rather than simply creating the combinations, let's try and separate the bread type and meat type. This can be done as follows:
```java
interface Bread {
...
}

interface Meat {
...
}
```

Now let's create concrete classes for each of the ```Bread```s and ```Meat```s:
```java
class White implements Bread {
    private Meat meat;
    public White(Meat meat) {
        this.meat = meat;
    }
    ...
}

class Brown implements Bread {
    private Meat meat;
    public Brown(Meat meat) {
        this.meat = meat;
    }
    ...
}

class Chicken implements Meat {
    ...
}

class Turkey implements Meat {
    ...
}

class Ham implements Meat {
    ...
}
```

Now if we wanted to have tuna as an option of a sandwich, all we have to do is the following:
```java
class Tuna implements Meat {
    ...
}
```
And if we wanted sourdough:
```java
class SourDough implements Bread {
    private Meat meat;
    public White(Meat meat) {
        this.meat = meat;
    }
    ...
}
```
## What have we accomplished?
Even though this is just a small example, the power of the Bridge pattern is quite evident. By applying the pattern, we went from
having a potentially exponential number of classes for the deli to a linear number of classes . Instead of having to create a class for
each of the breads when adding a meat, we only have to create one for the meat, the same applies for adding a new bread. The Bridge 
pattern allows for a more streamline structure of a family of classes by splitting the family up into mini families, which allows
for more granularity when trying to combine members of different families together. The Bridge design pattern is very easy to apply,
but its effectivness in saving hours of work should be noted by all developers.