# Design Patterns Cheat Sheet

## Builder Pattern:
### If your class resembles something like this
```
public class Computer {
    private String motherboard;
    private String processor;
    private String graphicsCard;
    private String memory;
    private String storage;
    ... <more fields potentially> ...
    
    public void setMotherboard(String motherboard) {
        this.motherboard = motherboard;
    }
    
    public void setProcessor(String processor) {
        this.processor = processor;
    }
    
    public void setGraphicsCard(String graphicsCard) {
        this.graphicsCard = graphicsCard;
    }
    
    public void setMemory(String memory) {
        this.memory = memory;
    }
    
    public void setStorage(String storage) {
        this.storage = storage;
    }
    ... <more setters potentially> ...
}

```

### Do this!
```
class Computer {
    private final String motherboard;
    private final String processor;
    private final String graphicsCard;
    private final String memory;
    private final String storage;
    
    private Computer(Builder builder) {
        this.motherboard = builder.motherboard;
        this.processor = builder.processor;
        this.graphicsCard = builder.graphicsCard;
        this.memory = builder.memory;
        this.storage = builder.storage;
    }
    
    public static class Builder {
        private String motherboard;
        private String processor;
        private String graphicsCard;
        private String memory;
        private String storage;
        
        public Builder motherboard(String motherboard) {
            this.motherboard = motherboard;
            return this;
        }
        
        public Builder processor(String processor) {
            this.processor = processor;
            return this;
        }
        
        public Builder graphicsCard(String graphicsCard) {
            this.graphicsCard = graphicsCard;
            return this;
        }
        
        public Builder memory(String memory) {
            this.memory = memory;
            return this;
        }
        
        public Builder storage(String storage) {
            this.storage = storage;
            return this;
        }
        
        public Computer build() {
            return new Computer(this);
        }
    }
}

```

This takes your usage of this class from going like this
```
Computer comp = new Computer();
comp.setMotherboard("Intel");
comp.setProcessor("Intel");
comp.setMemory("8 GB");
comp.setGraphicsCard("NVIDIA");
comp.setStorage("512 GB");
......
```
To this
```
Computer comp = new Builder().comp.motherboard("Intel").processor("Intel").memory("8 GB").graphicsCard("NVIDIA").storage("512 GB").build();
```

## Singleton Pattern:
### If your class resembles something like this
```
public class Lock {
    private static Lock instance;
    private Logger() {}
    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }
    public void unlock() {
        self.lock = false;
    }
    
    public void lock() {
        self.lock = true;
    }
}
```
### Do This
```
class Lock {
    private static Lock instance = new Lock();
    private Lock() {}
    public static Lock getInstance() {
        return instance;
    }
    public void unlock() {
        self.lock = false;
    }
    
    public void lock() {
        self.lock = true;
    }
}
```
This will allow your code from being alot more secure and simple to use, as now your class cannot be instantiated multiple times (only once!)
Usage wise, it will go from looking like this:
```
// makes the lock
Lock lock = new Lock();

//replaces lock with new instance of Lock, which is not what you want! The old instance is now lost
lock = new Lock();
```

```
// gets the Lock instance
Lock lock = Lock.getInstance();

// this line below will throw an error, because there is no such constructor to create a new Lock!
lock = new Lock();
```


## Command Pattern
### If your code resembles something like this
```
public class Car {
    public void turnLeft() {
        System.out.println("Turn left!");
    }
    public void turnRight() {
        System.out.println("Turn right!");
    }
    ....
    public void zigzag() {
            car.turnLeft();
            car.turnRight();
            car.turnLeft();
            car.turnRight();
            car.turnLeft();
            car.turnRight();
    }
}

public class Driver {
    public void execute(String command) {
        Car car = new Car();
        if (command.equals("RIGHT")) {
            car.turnRight();
        } else if (command.equals("LEFT")) {
            car.turnLeft();
        }
        ....
        ....
        } else if (command.equals("ZigZag")) {
            car.zigzag();
        }
    }
}
```
### Apply the command pattern
```
public interface Command {
    void execute();
}

public class LeftCommand implements Command {
    private Car Car;
    public LeftCommand(Car car) {
        this.car = car;
    }
    @Override
    public void execute() {
        car.turnOn();
    }
}

public class RightCommand implements Command {
    private Car car;
    public RightCommand(Car car) {
        this.car = car;
    }
    @Override
    public void execute() {
      car.turnRight();
    }
}

public class ZigZag implements Command {
    private Car car;
    public ZigZag(Car car) {
        this.car = car;
    }
    @Override
    public void execute() {
            car.turnLeft();
            car.turnRight();
            car.turnLeft();
            car.turnRight();
            car.turnLeft();
            car.turnRight();
    }
}

public class Driver {
    public void execute(String command) {
        Car car = new Car();
        if (command.equals("RIGHT")) {
            new RightCommand(car).execute();
        } else if (command.equals("LEFT")) {
            new LeftCommand(car).execute();
        }
        ....
        ....
        } else if (command.equals("ZigZag")) {
            new ZigZagCommand(car).execute();
        }
    }
}
```
By using this pattern, this allows your code from turning into spaghetti code. Instead of your Car class and Driver class becoming incredibly long and unwieldy, the actions are delegated to different classes. The file structure will now look something like this <An image which shows the file structure>.


## Dependency Injection
This is a very common malpractice that a lot of beginners do when first learning about Object Oriented Programming:
```
...

private ArrayList<Integer> list = new ArrayList<Integer>();

....

public void setList(ArrayList<Integer> list) {
  this.list = list;
}

...
```
But what if we want to do this in the codebase:
```
this.setList(new LinkedList<Integer>());
```
This would throw an error, unless we create another method such as that:
```
public void setList(LinkedList<Integer> list) {
  this.list = list;
}
...
```
This is very bad practice, as we would be forced to create multiple methods. Instead however, we can use interfaces to our advantage and re-implement this as such.


```
...

private List<Integer> list = new ArrayList<Integer>();

....

public void setList(List<Integer> list) {
  this.list = list;
}

...
```
Now this change is possible without creating a new method:
```
this.setList(new LinkedList<Integer>());
```

This design pattern is known as Dependency Injection, and it is one of the cornerstone patterns of Object Oriented Programming. There is no excuse for not using dependency injection and should be employed in EVERY SINGLE CODEBASE if allowed by the language being used.

                                                                  
                                                                  
