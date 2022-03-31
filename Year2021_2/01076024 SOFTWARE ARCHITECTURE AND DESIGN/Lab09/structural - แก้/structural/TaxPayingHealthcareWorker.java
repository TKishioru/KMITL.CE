package edu.parinya.softarchdesign.structural;

public class TaxPayingHealthcareWorker extends HealthcareWorkerDecorator {
   
    public TaxPayingHealthcareWorker(HealthcareWorker worker) {
        super(worker);
        System.out.printf("Decorate %s with TaxPaying.\n", worker.getName());
    }

    @Override
    public double getPrice() {
        return super.getPrice() * 1.0;
    }

}
