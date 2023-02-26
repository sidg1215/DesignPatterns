# Command Pattern
## What is the Command Pattern?
The Command Design Pattern is a behavioral design pattern that creates behavior of an Object(s) by delegating it to a separate class.

## Why would we want to use it?
Let's suppose that we have a Turtle class, and all it can do is '''pointLeft()''', '''pointRight()''', '''pointUp()''', and '''pointDown()'''. This is the interface:
'''
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
'''

This interface comes with an controller, which serves as a way for the user to make commands to a Turtle: 
'''
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
'''

Now let's say that we want to be able to make this Turtle point top-right. The easiest thing to do would be to add a new method to the interface called '''pointTopRight()'''. We can do the same thing for top-left, bottom-left, etc. But this presents a problem.

If we do this, we make the Turtle class very long and un-wieldy to manage in the long run: 

'''
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
    // Imagine if we have this one class with a thousand methods, that's not really easy to manage for hudnereds of developers
}
'''

## How would we use the Command pattern to solve this?
In order to fix this, we just employ the paradigm of the Command pattern.

The first step is to create a TurtleCommand interface, which basically serves as a way to "encapsulate" a command that a turtle will execute:
'''
interface TurtleCommand {
    void execute(Turtle turtle);
}
'''

And then we just create classes that encapsulate commands of a Turtle:
'''
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
        turtle.pointRight();
        turtle.pointUp();
    }
}
'''

Now these classes can be used in the controller:
'''
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
'''

## What have we accomplished?
By using the Command Patten, we have made the entire Turtle codebase more flexible and easy to manage. The way we did this was that instead of having all of our code in just two classes (The Turtle class and the Controller class), we now have all of our code in multiple different classes (The Turtle class, the Controller class, the PointRight class, the PointLeft class etc.), which makes it easier to manage for developers as each of these classes represents one "command".

The Command pattern is widely used in applications that require users to execute commands (hence the name), and altohugh it is one that is difficult to wrap around, it is oen of the most powerful design patterns in this guide.