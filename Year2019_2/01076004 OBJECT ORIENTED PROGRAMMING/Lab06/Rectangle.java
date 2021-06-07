
import java.util.Date;


public class Rectangle extends GeometricObject implements Colorable{
    public double width,height;

    @Override
     public double getArea() {
        return width * height;
    }

    @Override
     public double getPerimeter() {
        return (height+width)* 2;
    }

    public Rectangle() {
    }

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public Rectangle(double width, double height, String color, Date deateCreated) {
        super(color, deateCreated);
        this.width = width;
        this.height = height;
    }

    @Override
    public String toString() {
        return "Rectangle{" + "width=" + width + ", height=" + height + '}';
    }

    @Override
    public int compareTo(GeometricObject o) {
               if(getArea()> o.getArea()) return +1;
        else if (getArea()> o.getArea()) return -1;
        else return 0;
    }

    @Override
    public void howtoColor() {
      System.out.println(color);
    }
    
}
