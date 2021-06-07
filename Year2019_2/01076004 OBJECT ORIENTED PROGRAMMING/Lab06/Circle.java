
import java.util.Date;

public class Circle extends GeometricObject implements Colorable {

    double radius;
    static double m = 0;

    @Override
    double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    public Circle() {
    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public Circle(double radius, String color, Date deateCreated) {
        super(color, deateCreated);
        this.radius = radius;
    }

    @Override
    public String toString() {
        return "Circle{" + "radius=" + radius + '}';
    }

    @Override
    public void howtoColor() {
        System.out.println(color);
    }

    @Override
    public int compareTo(GeometricObject o) {
             if(getArea()> o.getArea()) return +1;
        else if (getArea()> o.getArea()) return -1;
        else return 0;
    }

}
