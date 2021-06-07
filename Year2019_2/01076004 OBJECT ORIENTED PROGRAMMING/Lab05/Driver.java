
import java.util.ArrayList;

public class Driver {

    public static void main(String[] args) {
        Lab lab1 = new Lab("Lab1","Lab1", 12, 12, 18, 00);
        Lab lab2 = new Lab("Lab2","Lab2", 12, 12, 18, 10);
        //String name, int month, int day, int hour, int minute
        Project Pro1 = new Project("Proj", "Proj", "Proj", 12, 12, 18, 20);
        //Project(String specification, String dataFile, String name, int month, int day, int hour, int minute)
        Assignment Assign1 = new Assignment("Assign1", 12, 12, 18, 30);
        Assignment Assign2 = new Assignment("Assign2", 12, 12, 18, 40);
        //Assignment(String name, int month, int day, int hour, int minute)
        AssignmentList AL = new AssignmentList();

        AL.additem(Assign1);
        AL.additem(Assign2);
        AL.additem(Pro1);
        AL.additem(lab1);
        AL.additem(lab2);

        lab1.setScore(3.5);
        lab1.setTotalPoints(1);
        lab1.setTotalWeight(1);

        lab2.setScore(3);
        lab2.setTotalPoints(1);
        lab2.setTotalWeight(1);

        Pro1.setScore(4);
        Pro1.setTotalPoints(1);
        Pro1.setTotalWeight(6);

        Assign1.setScore(2.5);
        Assign1.setTotalPoints(1);
        Assign1.setTotalWeight(3);

        Assign2.setScore(3.5);
        Assign2.setTotalPoints(1);
        Assign2.setTotalWeight(3);

        System.out.println(AL.toString() + "\n");
        System.out.println(Assign1.toString() + "\n");
        System.out.println(Pro1.toString() + "\n");
        System.out.println(lab1.toString() + "\n");
    }
}
