//import java.util.Scanner;
//Scanner sc = new Scanner(System.in);

import java.lang.*;

public class RegularPolygon {

    double area;
    double perimeter;
    int length;
    int numberOfSides;
   static int numberOfObject;
    double xOrigin;
    double yOrigin;

    RegularPolygon() {
       // this(5,5);
        numberOfObject++;
    }

    RegularPolygon(int numberOfSides, int length) {
        this.numberOfSides = numberOfSides;
        this.length = length;
        numberOfObject++;
    }

    RegularPolygon(int numberOfSides, int length, double xOrigin, double yOrigin) {
        this.numberOfSides = numberOfSides;
        this.length = length;
        this.xOrigin = xOrigin;
        this.yOrigin = yOrigin;
        numberOfObject++;
    }

     void setArea(double area) {
        this.area = area;
    }

    void setPerimeter(double perimeter) {
        this.perimeter = perimeter;

    }

    double getArea() {
        area = (numberOfSides * Math.pow(length, 2)) / (4 * Math.tan((Math.PI / numberOfSides)));
        return area;
    }

    double getPerimeter() {
        perimeter = length * numberOfSides;
        return perimeter;
    }

}
