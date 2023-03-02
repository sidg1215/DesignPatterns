# Builder design pattern
* [What is the Builder design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Builder%20Design%20Pattern#what-is-the-builder-design-pattern)
* [Why would we want to use it?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Builder%20Design%20Pattern#why-would-we-want-to-use-it)
* [How can we use the Builder design pattern to solve this issue?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Builder%20Design%20Pattern#how-can-we-use-the-builder-design-pattern-to-solve-this-issue)
* [What have we accomplished?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Builder%20Design%20Pattern#what-have-we-accomplished)
## What is the Builder design pattern?
The Builder design pattern is used to delegate the creation and modification of an object to a separate class.
## Why would we want to use it?
Suppose we have a ```Computer``` class as such:
```java
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
If a ```Computer``` object needs to be created, this is how it will be done:
```java
Computer comp = new Computer();
comp.setMotherboard("Intel");
comp.setProcessor("Intel");
comp.setMemory("8 GB");
comp.setGraphicsCard("NVIDIA");
comp.setStorage("512 GB");
... <more calls to setters potentially> ...
```

### ***The issue***: 
Notice how just to create and modify one object, several lines of code have to be used and as such, it makes the code look long and unwieldy, which in the long run is poor practice because it makes it harder for multiple developers to work on the same file together. Not only that, a larger concern to point out is that because object creation and modification can take up thousands of lines of code in the class itself, that makes the class definition long and unwieldy as well. This is __not extensible__ in the long run when more state is added to the class.

## How can we use the Builder design pattern to solve this issue?
The Builder design pattern uses the idea of "chaining" method calls together in order to make it easier to modify the state of a class. Not only that, by utilizing the Builder pattern, custom constructors do not have to be created, which is a very powerful side-effect of the pattern.

To see this, lets create a ```Computer``` class with a Builder class:
```java
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

With this Builder class, we now have a more robust way of creating ```Computer``` objects, as such:
```java
Computer comp = new Builder().comp.motherboard("Intel").processor("Intel").memory("8 GB").graphicsCard("NVIDIA").storage("512 GB").build();
```
Compared to the long list of ```set{Property}``` calls that had to be made in the previous, bad implementation, this way of creating ```Computer``` objects is a lot cleaner and easier to use.

## What have we accomplished?
Although what has been accomplished is mainly an aesthetic change in the code, by employing the Builder design pattern, you essentially make a way for yourself and other developers using your code to construct objects in many different ways, and also make it easier for developers to construct them, which in the long run, allows for code to be written and integrated faster into the codebase.

The builder design pattern is used by most if not all developers who are writing object-oriented code. Not only that, it is easy to integrate into an existing codebase and makes the creation and modification process of any class more extensible.