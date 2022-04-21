package edu.parinya.softarchdesign.behavior2;

// DO NOT MODIFY ANYTHING BELOW THIS LINE!!
import java.io.PrintStream;

public class Main {

    public static void main(String[] args) {
        Person alice = new Person();
        alice.setName("Alice Henderson");
        alice.setAge(27);
        alice.setHeight(164);
        alice.setWeight(49);

        Person bob = new Person();
        bob.setName("Bob Sanders");
        bob.setAge(34);
        bob.setHeight(171);
        bob.setWeight(67);

        Person carol = new Person();
        carol.setName("Carol Sanders");
        carol.setAge(29);
        carol.setHeight(161);
        carol.setWeight(51);

        Person ted = new Person();
        ted.setName("Ted Henderson");
        ted.setAge(31);
        ted.setHeight(180);
        ted.setWeight(69);

        People people = new People();
        people.addMember(alice);
        people.addMember(bob);
        people.addMember(carol);
        people.addMember(ted);

        PrintStream out = System.out;
        people.print(out);
        people.setSortStrategy(new AgeSortStrategy());
        people.print(out);
        people.setSortStrategy(new HeightSortStrategy());
        people.print(out);
        people.setSortStrategy(new WeightStrategy());
        people.print(out);
    }
}
