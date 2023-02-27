# Builder Pattern
## What is the Builder Pattern?
The Builder pattern is used to delegate the creation and modification of an object to a separate class.
## Why would we want to use it?
Suppose we have a Computer class as such:
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
If a Computer object needs to be created, this is how it will be done:
```
Computer comp = new Computer();
comp.setMotherboard("Intel");
comp.setProcessor("Intel");
comp.setMemory("8 GB");
comp.setGraphicsCard("NVIDIA");
comp.setStorage("512 GB");
... <more calls to setters potentially> ...
```
 Notice how just to create and modify one object, several lines of code have to be used and as such, it makes the code look long and unwieldy. Imagine if this class had a thousand fields and thus required thousands of setters to be used.

## How would we use the Builder pattern to solve this?
The Builder pattern uses the idea of "chaining" method calls together in order to make it easier to modify 
## What have we accomplished?