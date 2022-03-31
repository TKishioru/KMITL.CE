// Please DO NOT MODIFY THIS FILE
package edu.parinya.softarchdesign.structural;

public abstract class HealthcareWorker implements HealthcareServiceable {
    private String name;
    private double price;

    public HealthcareWorker(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public HealthcareWorker(HealthcareWorker worker) {
        this.name = worker.getName();
        this.price = worker.getPrice();
    }

    public String getName() {
        return name;
    }

    public abstract void service();

    public double getPrice() {
        return this.price;
    }
}
