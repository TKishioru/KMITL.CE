package structural;

public class Anesthesiologist extends HealthcareWorker {
    public Anesthesiologist(String name, double price) {
        super(name, price);
    }

    @Override
    public void service() {
        System.out.println(this.getName() + " takes care of the total perioperative care of patients" +
                " before, during and after surgery.");
    }
}
