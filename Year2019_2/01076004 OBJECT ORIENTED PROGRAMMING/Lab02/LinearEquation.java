
public class LinearEquation {

    double a;
    double b;
    double c;
    double d;
    double e;
    double f;
    double x;
    double y;
    static int numberOfObject;

     LinearEquation() {

    }

     LinearEquation(double a, double b, double c, double d, double e, double f) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.e = e;
        this.f = f;
    }

    boolean isSolvable() {
        double check = (a * d) - (b * c);
        if (check == 0) {
            return false;
        } else {
            return true;
        }
    }

     double getX() {
        x = (e * d - b * f) / (a * d - b * c);
        return x;
    }

    double getY() {
        y = (a * f - e * c) / (a * d - b * c);
        return y;
    }

     void showEquation() {
        System.out.println(a + "x + " + b + "y = " + e);
        System.out.println(c + "x + " + d + "y = " + f);
    }
}
