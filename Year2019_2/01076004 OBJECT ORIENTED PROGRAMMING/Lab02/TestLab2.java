
import java.util.Scanner;

public class TestLab2 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        RegularPolygon poly0 = new RegularPolygon();
        RegularPolygon poly1 = new RegularPolygon(6, 4);
        RegularPolygon poly2 = new RegularPolygon(10, 4, 5.6, 7.8);
        System.out.println("-------------- REGULAR POLYGON ---------------");
        System.out.println(poly0.getPerimeter());
        System.out.println(poly0.getArea());
        System.out.println(poly1.getPerimeter());
        System.out.println(poly1.getArea());
        System.out.println(poly2.getPerimeter());
        System.out.println(poly2.getArea());
        System.out.println(" ");

        System.out.println("----------- LINER EQUATION --------------");
        System.out.println("Enter a -> f");
        System.out.print("a : ");
        double a = sc.nextDouble();
        System.out.print("b : ");
        double b = sc.nextDouble();
        System.out.print("c : ");
        double c = sc.nextDouble();
        System.out.print("d : ");
        double d = sc.nextDouble();
        System.out.print("e : ");
        double e = sc.nextDouble();
        System.out.print("f : ");
        double f = sc.nextDouble();
        LinearEquation line = new LinearEquation(a, b, c, d, e, f);
        if (line.isSolvable() == false) {
            System.out.println("The equation has no solution.");
        } else {
            System.out.println(line.getX());
            System.out.println(line.getY());
            line.showEquation();
        }

    }
}
