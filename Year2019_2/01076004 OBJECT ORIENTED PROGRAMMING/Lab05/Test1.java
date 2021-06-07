/*
public class Test1 {

    public static void main(String[] args) {
        Geometric g1 = new Circle(); //polymorphism
        Circle g0 = new Circle(); //datatype of g0 is circle
        Geometric g2 = new Rectangle(); //polymorphism
//        g1.display();
//        g0.display();
//        m(g1);
//        m(g2);
        m(g0);
        g0.display(5);
        g0.display();
        g1.display(5); //method matching
    }

    static void m(Circle g) {
        System.out.println(g.toString());
    }

}

class Geometric extends Object {

    int GAttr;

    void display() {
    }

    
    @Override
    public String toString() {
        return "Geometric";
    }
}

class Circle extends Geometric {

    int GAttr;

    void display(int n) {
        System.out.println(n);
    }

    
//        void display() {
//            System.out.println("Thisn is Circle");
//        }
    @Override
    public String toString() {
        return "Circle";
    }
}

class Rectangle extends Geometric {

    void display() {
        System.out.println("Thisn is Rectangle");
    }
}
*/