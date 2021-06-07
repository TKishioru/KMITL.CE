
import java.util.Date;

public class Square extends GeometricObject implements Colorable{
double Lside;
    @Override
    double getArea() {
        return Lside * Lside;
    }

    @Override
    double getPerimeter() {
       return Lside * 4;
    }

    public Square() {
    }

    public Square(double Lside) {
        this.Lside = Lside;
    }

    public Square(double Lside, String color, Date deateCreated) {
        super(color, deateCreated);
        this.Lside = Lside;
    }

    @Override
    public void howtoColor() {
        System.out.println(color + " : Color all four side.");
    }

    @Override
    public int compareTo(GeometricObject o) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}