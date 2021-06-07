
import java.util.ArrayList;
import java.util.Date;

public class TestGeo {

    public static void main(String[] args) {
             Circle c1 = new Circle(25, "Red", new Date());
        Circle c2 = new Circle(45, "None", new Date());
        System.out.println(c1.radius);
        System.out.println(c2.radius);
        System.out.println(GeometricObject.max(c1, c2));

        Rectangle r1 = new Rectangle(5, 6, "Green", new Date());
        Rectangle r2 = new Rectangle(4, 5, "Blue", new Date());
        System.out.print(r1.height);
        System.out.print("    ");
        System.out.println(r1.width);
        System.out.print(r2.height);
        System.out.print("    ");
        System.out.println(r2.width);
        System.out.println(GeometricObject.max(r1, r2));

        Square s1 = new Square(25, "Pink", new Date());
        System.out.println(s1.Lside);

        ArrayList<GeometricObject> list = new  ArrayList<>();
        list.add(c1);
        list.add(c2);
        list.add(r1);
        list.add(r2);
        list.add(s1);
        for (int i = 0; i < list.size(); i++) {
            list.get(i).howtoColor();     
        }
    }
}
