# Command design pattern

* [What is the Command design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Command%20Design%20Pattern#what-is-the-command-design-pattern)
* [Why would we want to use it?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Command%20Design%20Pattern#why-would-we-want-to-use-it)
* [How can we use the Command design pattern to solve this issue?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Command%20Design%20Pattern#how-can-we-use-the-command-design-pattern-to-solve-this)
* [What have we accomplished?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Command%20Design%20Pattern#what-have-we-accomplished)
## What is the Command design pattern?
The Command design pattern is a behavioral design pattern that creates behavior of an Object(s) by delegating it to a separate class.

## Why would we want to use it?
Suppose we have a Turtle class, and all it can do is ```pointLeft()```, ```pointRight()```, ```pointUp()```, and ```pointDown()```. This is the class definition for Turtle:
```java
class Turtle {
    void pointLeft() {
        ...
    }
    void pointRight() {
        ...
    }
    void pointUp() {
        ...
    }
    void pointDown() {
        ...
    }
}
```

This interface comes with an controller, which serves as a way for the user to make commands to a Turtle: 
```java
public class Controller {
    public void control(String command) {
        Turtle turtle = new Turtle();
        if (command.equals("RIGHT")) {
            turtle.pointRight();
        } else if (command.equals("LEFT")) {
            turtle.pointLeft();
        } else if (command.equals("UP")) {
            turtle.pointUp();
        } else if (command.equals("DOWN")) {
            turtle.pointDown();
        }
    }
}
```

Now let's say that we want to be able to make this Turtle point top-right. The easiest thing to do would be to add a new method to the interface called ```pointTopRight()```. We can do the same thing for top-left, bottom-left, etc. But this presents a problem.

### ***The issue***: 
If we keep adding more and more methods directly to the ```Turtle``` class, the class definition becomes very long and un-wieldy. In fact, if methods and behavior are added in this way at this rate, this class alone can be tens of thousands of lines long. This is bad practice, and it makes it much harder for multiple developers to work on adding more behavior to the Turtle class at the same time:

```java
class Turtle {
    void pointLeft() {
        ...
    }
    void pointRight() {
        ...
    }
    void pointUp() {
        ...
    }
    void pointDown() {
        ...
    }
    void pointTopRight() {
        ...
    }
    void pointTopLeft() {
        ...
    }
    ...
    ...
    ...
    // Imagine if we have this one class with a thousand methods, that's not really easy to manage for hundereds of developers
}
```
In short, if we keep things as is, our codebase is __not extensible or useable__ by other developers
## How can we use the Command design pattern to solve this issue?
In order to fix this, we just employ the Command design pattern.

The first step is to create a ```TurtleCommand``` interface, which basically serves as a way to "encapsulate" a command that a turtle will execute:
```java
interface TurtleCommand {
    void execute(Turtle turtle);
}
```

And then we just create classes that encapsulate commands of a Turtle:
```java
// point right
class PointRight implements TurtleCommand {
    void execute(Turtle turtle) {
        turtle.pointRight();
    }
}

// point left
class PointLeft implements TurtleCommand {
    void execute(Turtle turtle) {
        turtle.pointLeft();
    }
}

// point up
class PointUp implements TurtleCommand {
    void execute(Turtle turtle) {
        turtle.pointUp();
    }
}

// point down
class PointDown implements TurtleCommand {
    void execute(Turtle turtle) {
        turtle.pointDown();
    }
}

// point top-right
class PointTopRight implements TurtleCommand {
    void execute(Turtle turtle) {
        // this is the code to make the turtle point top right
        ...
    }
}
```

Now these classes can be used in the controller:
```java
public class Controller {
    public void control(String command) {
        Turtle turtle = new Turtle();
        TurtleCommand command;
        if (command.equals("RIGHT")) {
            command = new PointRight()
        } else if (command.equals("LEFT")) {
            command = new PointLeft()
        } else if (command.equals("UP")) {
            command = new PointUp()
        } else if (command.equals("DOWN")) {
            command = new PointDown()
        }
        else if (command.equals("TOPRIGHT")) {
            command = new PointTopRight()
        }
        ...
        ...
        ...
        }
        command.execute(turtle);
    }
}
```

## What have we accomplished?
By using the Command design pattern, we have made the entire Turtle codebase more flexible and easy to manage. The way we did this was that instead of having all of our code in just two classes (The Turtle class and the Controller class), we now have all of our code in different classes (The Turtle class, the Controller class, the PointRight class, the PointLeft class etc.). This makes it easier to manage for developers as each of these classes represents one "command" (or one behaviour, or one feature).

The Command desing pattern is widely used in many different applications, and altohugh it is one that is difficult to wrap around, it is oen of the most powerful design patterns in this guide.