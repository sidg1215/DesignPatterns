# Iterator Pattern
## What is the Iterator Pattern?
The Iterator pattern is a design pattern that abstracts away the behavior of iteration, such that the client (code that uses an Iterator) does not have to worry about the underlying way to iterate through a data structure.

## Why would we want to use it?
Iteration is an important part in all codebases. In a high-level point of view, it is the process of going through items in a data structure. Iteration can be performed on many structures, such as arrays, sets, trees, maps etc.

As a toy example, let's say we wanted to add all the numbers in a list:

```
class NumberAdder {
    public int sum(List<Integer> numbers) {
        int sum = 0;
        for (int i = 0; i < numbers.size(); i = i + 1>) {
            sum = sum + numbers.get(i);
        }
    }
}

class NumberPrinterExecutor {
    public static void main(String args) {
        NumberAdder adder = new NumberAdder();
        List<Integer> listOfNumbers = new ArrayList<Integer>();
        listOfNumbers.add(1);
        listOfNumbers.add(2);
        listOfNumbers.add(3);
        listOfNumbers.add(1);

        int sumOfList = adder.sum(listOfNumbers);
    }
}
```

Now what if we wanted to add a set of numbers? Of course, a Set<Integer> and List<Integer> are two different types, so we would have to create a new sum method in our NumberAdder class that takes in a Set<Integer>:

```
class NumberAdder {
    public int sum(List<Integer> numbers) {
        int sum = 0;
        for (int i = 0; i < numbers.size(); i = i + 1>) {
            sum = sum + numbers.get(i);
        }
    }

    public int sum(Set<Integer> numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum = sum + num;
        }
        return sum;
    }
}

class NumberPrinterExecutor {
    public static void main(String args) {
        NumberAdder adder = new NumberAdder();
        List<Integer> listOfNumbers = new ArrayList<Integer>();
        listOfNumbers.add(1);
        listOfNumbers.add(2);
        listOfNumbers.add(3);
        listOfNumbers.add(1);

        int sumOfList = adder.sum(listOfNumbers);

        Set<Integer> setOfNumbers = new Set<Integer>();
        setOfNumbers.add(1);
        setOfNumbers.add(2);
        setOfNumbers.add(3);
        setOfNumbers.add(1);

        int sumOfSet = adder.sum(setOfNumbers);
    }
}
```
If you notice, the only part that is different in the two ```sum``` methods is the way of iterating through its input. Of course, this is just a toy example, but in the real-world, this uses thousands of lines of unnecessary code.
## How would we use the Iterator pattern to solve this?
Since Java is being used, some of the built-in tools and interfaces of the language can be used in employing the Iterator pattern in this example. The ```sum``` method has a simple goal: to calculate the sum of the items in the given structure. It does not care how the structure is implemented, and so it does not need to know how to iterate over the structure. All it needs to know is how to get the ```next``` item in a sturcture and if it ```hasNext``` item (structure has no more items).

All collections in Java (Including the List and Set interfaces) come with an ```iterator``` method, which returns an ```Iterator``` object. The ```Iterator``` interface has two methods: ```next``` and ```hasNext```. ```next``` gets the next item in a collection and ```hasNext``` checks to see if the collection has anymore items.

Using this ```Iterator``` pattern, the code above can be refactored as such:
```
class NumberAdder {
    public int sum(Iterator<Integer> numbersIterator) {
        int sum = 0;
        while (numbersIterator.hasNext()) {
            sum = sum + numbersIterator.next();
        }

        return sum;
    }
}

class NumberPrinterExecutor {
    public static void main(String args) {
        NumberAdder adder = new NumberAdder();
        List<Integer> listOfNumbers = new ArrayList<Integer>();
        listOfNumbers.add(1);
        listOfNumbers.add(2);
        listOfNumbers.add(3);
        listOfNumbers.add(1);

        int sumOfList = adder.sum(listOfNumbers.iterator());

        Set<Integer> setOfNumbers = new Set<Integer>();
        setOfNumbers.add(1);
        setOfNumbers.add(2);
        setOfNumbers.add(3);
        setOfNumbers.add(1);

        int sumOfSet = adder.sum(setOfNumbers.iterator());
    }
}
```
Now, there is no need for two ```sum``` methods that are nearly duplicate.

Custom ```Iterator``` classes can be designed for classes that are designed by a developer, which allow the developer to specify how to iterate through a structure. This makes the ```Iterator``` extremely powerful.

## What have we accomplished?
Even though this example is very, very small, it shows that the act of iteration is something that can be abstracted away, and that is important, because iteration is something that is so common that oftentimes it can occupy a high percentage of a codebase, and it is something that is very easily duplicated. Remember, code duplication is bad, and should be avoided at all costs.

The Iterator pattern is a must-know for anyone who is designing or working with a large codebase.