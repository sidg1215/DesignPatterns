# Adapter Pattern
## What is the Adapter Pattern?
The Adapter pattern allows a developer to use use integerate that has been produced by someone else or another third-party application into their own codebase, without modifying the other developers code.
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
```java
As we are designing the car race, we realize we want to include electric cars. Unfortunately, creating an ```javaElectricCar```java class on our own is way too much effort, and so we decided to use the an ```javaElectricCar```java definition of another developer.
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
```java
This is where we run into a problem: we are not allowed to change the other developer's ```javaElectricCar```java implementation, so how do we use it in our codebase?
## How would we use the Adapter pattern to solve this?
We can simply use the Adapter pattern to create an "adapter" around the other developer's ```javaElectricCar```java class as such:
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
```java
## What have we accomplished?
By using the Adapter pattern, we are saved the headache of not being able to use code from other different codebases that have different implementations. This allows faster production as developers do not have to reinvent the wheel every time an addition to the codebase needs to be made.
