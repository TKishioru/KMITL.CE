/*import java.util.ArrayList;

public class Test2 {

    public static void main(String[] args) {
//        Object o = new Student(); //implicit casting
//        ((Student) o).m(); //explicit casting
        Person p1 = (Person) new Student(); //implicit casting
        ((Student) p1).m(); //explicit casting
        Person p2 = new GradStudent();
        if (p1 instanceof GradStudent) {
            ((Student) p1).m();
        } else if (p2 instanceof GradStudent) {
            ((GradStudent) p2).m();
        }
        ArrayList<Person> list = new ArrayList<>(); //Keep subclass
        list.add(p1);
        list.add(p2);
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i).m());
            if(list.get(i) instanceof Student)
            ((Student) list.get(i)).m();
            else if(list.get(i) instanceof GradStudent)
            ((GradStudent) list.get(i)).m();
        }
    }
}

class Person {

}

class Student extends Person {

    void m() {
        System.out.println("student");
    }
}

class GradStudent extends Person {

    void m() {
        System.out.println("gradstudent");
    }
}
*/