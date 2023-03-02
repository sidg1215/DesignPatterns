# Adapter design pattern
* [What is the Adapter design pattern?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Adapter%20Design%20Pattern#what-is-the-adapter-design-pattern)
* [Why would we want to use it?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Adapter%20Design%20Pattern#why-would-we-want-to-use-it)
* [How can we use the Adapter design pattern to solve this issue?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Adapter%20Design%20Pattern#how-can-we-use-the-adapter-design-pattern-to-solve-this-issue)
* [What have we accomplished?](https://github.com/sidg1215/DesignPatterns/tree/main/Behavioral%20Design%20Patterns/Adapter%20Design%20Pattern#what-have-we-accomplished)
## What is the Adapter design pattern?
The Adapter design pattern allows a developer to use use integerate that has been produced by someone else or another third-party application into their own codebase, without modifying the other developers code.
## Why would we want to use it?
Suppose that we are desigining a car race. For this, we will need a way to represent cars in our system. This can be done using the following:
```java
interface Car {
    void drive();
}

public class GasCar implements Car {
    public void drive() {
        // code to drive the car
    }
}

public class RaceTrack {
    public void startRace() {
        List<Car> allCars
        Car car1 = new GasCar();
        allCars.add(car1);
        for (Car car : allCars) {
            car.drive();
        }
    }
}
```
As we are designing the car race, we realize we want to include electric cars. Unfortunately, creating an ```ElectricCar``` class on our own is way too much effort, and so we decided to use the an ```ElectricCar``` definition of another developer.
```java
public class RaceTrack {
    public void startRace() {
        List<Car> allCars
        Car car1 = new GasCar();
        allCars.add(car1);
        allCars.add(car2)
        Car car2 = new ElectricCar(); //ERROR: ElectricCar from the other developer does not implement the Car interface
        for (Car car : allCars) {
            car.drive();
        }
    }
}
```
### ***The issue***: 
This is where we run into a problem: we are not allowed to change the other developer's ```ElectricCar``` implementation, so how do we use it in our codebase? If we keep things as is, our codebase is __not useable__ as we are not able to integrate code from other libraries.
## How can we use the Adapter design pattern to solve this issue?
We can simply use the Adapter design pattern to create an "adapter" around the other developer's ```ElectricCar``` class as such:
```java
public class OurElectricCar implements Car {
    ElectricCar otherDeveloperElectricCar;
    public OurElectricCar(ElectricCar otherDeveloperElectricCar) {
        this.otherDeveloperElectricCar = otherDeveloperElectricCar;
    }

    public void drive() {
        this.otherDeveloperElectricCar.drive();
    }
}

public class RaceTrack {
    public void startRace() {
        List<Car> allCars
        Car car1 = new GasCar();
        Car car2 = new OurElectricCar(new ElectricCar()); // This works now because OurElectricCar implements the interface
        allCars.add(car1);
        allCars.add(car2)
        for (Car car : allCars) {
            car.drive();
        }
    }
}
```
## What have we accomplished?
By using the Adapter design pattern, we are saved the headache of not being able to use code from other different codebases that have different implementations. This allows faster production as developers do not have to reinvent the wheel every time an addition to the codebase needs to be made.
