//หลีกเลี่ยงปัญหา Liskov Substitution Principle (LSP)

package com.solid.lsp;


public class Main {

    private static final int width = 4;
    private static final int height = 5;
    private static final int side = 7;
    
    public static void main(String[] args) {
        Rectangle reg1 = new Rectangle(width, height);
        System.out.println("==== Rectangle ====");
        System.out.println("Width = " + width);
        System.out.println("Height = " + height);
        System.out.println("Area = " + reg1.getArea());

        //เน้นเลขที่กรอกที่ side
        Rectangle reg2 = new Square(side);
        reg2.setWidth(width);
        reg2.setHeight(height);
        System.out.println("====   Square  ====");
        System.out.println("Width = " + reg2.getWidth());
        System.out.println("Height = " + reg2.getHeight());
        System.out.println("Area = " + reg2.getArea());
    }
    
}
