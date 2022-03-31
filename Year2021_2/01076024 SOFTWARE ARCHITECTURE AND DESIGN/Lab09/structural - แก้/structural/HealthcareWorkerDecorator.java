//use Decorator Pattern

package edu.parinya.softarchdesign.structural;

public abstract class HealthcareWorkerDecorator extends HealthcareWorker {

    private final HealthcareWorker worker;

    public HealthcareWorkerDecorator(HealthcareWorker worker) {
        super(worker.getName(), worker.getPrice());
        this.worker = worker;
    }
    
    public void service() {
        worker.service();
    }

    public double getPrice() {
        return worker.getPrice();
    }
    
}