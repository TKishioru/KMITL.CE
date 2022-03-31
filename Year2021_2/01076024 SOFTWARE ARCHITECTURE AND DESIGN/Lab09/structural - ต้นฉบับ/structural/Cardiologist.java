// Please DO NOT MODIFY THIS FILE
package edu.parinya.softarchdesign.structural;

public class Cardiologist extends HealthcareWorker {
    public Cardiologist(String name, double price) {
        super(name, price);
    }

    @Override
    public void service() {
        System.out.println(this.getName() + " treats the disorders of the heart.");
    }
}
