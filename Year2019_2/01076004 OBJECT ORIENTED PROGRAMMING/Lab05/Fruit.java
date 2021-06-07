
public class Fruit {
    public static void main(String[] args) {
        Object fruit = new Fruit();
        Apple a1 = (Apple)fruit;
//        Fruit f1 = fruit;
        //f1 may have more attri or method than Object
        Object f2 = a1;
    }
}
class Apple extends Fruit{
    
}
class Orange extends Apple{
    
}