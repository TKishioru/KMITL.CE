package edu.parinya.softarchdesign.government;

import java.util.List;
import java.util.Random;

public final class ThDemocraticGovernment extends DemocraticGovernment implements OligarchicSystem {
    public ThDemocraticGovernment(List<Voter> representatives, List<Person> leaderCandidates) {
        super(representatives, leaderCandidates);
    }

    public Person coup(Person insurgent) {
        Random random = new Random();
        if (random.nextBoolean()) {
            this.head = insurgent;
        }
        return this.head;
    }

    @Override
    public Person getHead() {
        return coup(new Person("a military junta"));
    }
}
