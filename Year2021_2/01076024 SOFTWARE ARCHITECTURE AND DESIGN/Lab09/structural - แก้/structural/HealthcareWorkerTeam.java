//use Composite Pattern

package edu.parinya.softarchdesign.structural;

import java.util.HashSet;
import java.util.Set;

public class HealthcareWorkerTeam implements HealthcareServiceable {

    private Set<HealthcareServiceable> members;

    public HealthcareWorkerTeam() {
        members = new HashSet<>();
    }

    public void addMember(HealthcareServiceable worker) {
        members.add(worker);
    }
    
    public void removeMember(HealthcareServiceable worker) {
        members.remove(worker);
    }
    
    @Override
    public void service() {
        for (HealthcareServiceable worker : members) {
            worker.service();
        }
    }

    @Override
    public double getPrice() {
        double totalPrice = 0;
        for (HealthcareServiceable worker : members) {
            totalPrice += worker.getPrice();
        }
        return totalPrice;
    }

}
