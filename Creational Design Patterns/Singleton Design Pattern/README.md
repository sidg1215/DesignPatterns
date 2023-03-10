# Singleton design pattern
* [What is the Singleton design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Singleton%20Design%20Pattern#what-is-the-singleton-design-pattern)
* [Why would we want to use this design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Singleton%20Design%20Pattern#why-would-we-want-to-use-this-design-pattern)
* [How can we use the Singleton design pattern to solve this issue?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Singleton%20Design%20Pattern#how-can-we-use-the-singleton-design-pattern-to-solve-this-issue)
* [What have we accomplished?](https://github.com/sidg1215/DesignPatterns/tree/main/Creational%20Design%20Patterns/Singleton%20Design%20Pattern#what-have-we-accomplished)
## What is the Singleton design pattern?
The Singleton design pattern restricts a class from being instantiated more than once, which although seems strange, does have very important applications.
## Why would we want to use this design pattern?
Suppose that we are designing a database-client system, such that clients connect to one singular database. This can be prototyped with the following code:
```java
public class Database {
    private String username;
    private String password;
    
    public Database(String username, String password) {
        this.username = username;
        this.password = password;
    }
    
    public void connect() {
        // this is code that allows you to connect to the database, not relevant
    }
    
    public void disconnect() {
        // this is code that allows you to disconnect to the database, not relevant
    }
}

public class Client {
    public void processData(String data) {
        Database db = new Database("user", "pass");
        db.connect();
        
        // this code processes the data from the database
        
        db.disconnect();
    }
}

```

Let's say now another client (different class) wants to connect to the database:
```java
...
public class Client2 {
    public void processData(String data) {
        Database db = new Database("user", "pass");
        db.connect();
        
        // this code processes the data from the database
        
        db.disconnect();
    }
}
...
```
### ***The issue***: 
This database has already been created and a connection has been initilalized. In the real-world, the cost of "re-estabilishing" a connection over and over again can be very expensive, both in terms of time and money. When a connection to, in this case, a database, has already been created, it must be preserved for the lifetime of the program! In short, in the long run, assuming money and time are of utmost concern, this code is __not useable__.
## How can we use the Singleton design pattern to solve this issue?
The Singleton design pattern prevents the creation of multiple objects of the same class, which allows for a "global" variable in object oriented programming. Although the use of global variables is frowned upon in OOP (Object Oriented Programming), it should be used sparingly as it has very powerful applications.

Applying the Singleton Pattern does not require too many changes:
```java
public class Database {
    private static Database instance = null;
    private String username;
    private String password;
    
    private Database(String username, String password) {
        this.username = username;
        this.password = password;
    }
    
    public static Database getInstance() {
        if (instance == null) {
            instance = new Database("user", "pass");
        }
        return instance;
    }
    
    public void connect() {
        // this is code that allows you to connect to the database, not relevant
    }
    
    public void disconnect() {
        // this is code that allows you to disconnect to the database, not relevant
    }
}

public class Client {
    public void processData(String data) {
        Database db = Database.getInstance();
        db.connect();
        
        // this code processes the data from the database
        
        db.disconnect();
    }
}

public class Client2 {
    public void processData(String data) {
        Database db = Database.getInstance();
        db.connect();
        
        // this code processes the data from the database
        
        db.disconnect();
    }
}

```

The key takeaway from this new code is that the constructor of the ```Database``` class is private, which means that it is impossible to create new ```Database``` objects.

When the ```getInstance``` method is called from the ```Database``` class, if a ```Database``` has not been initialized yet, it creates it. Else, it reuses the inital ```Database``` object that has been created. This allows for the same database to be used throughout the entire program by multiple clients.

## What have we accomplished?
By using the Singleton pattern, reusability of run-time instances has been enforced, which can be beneficial for performance and costs in a lot of codebases. The Singleton design pattern is used in many different places, such as locks for multi-threaded programs, web-scrapers, and even loggers.