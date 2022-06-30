package edu.parinya.softarchdesign.government;

import java.util.List;
import java.util.Random;

public class Voter extends Person implements Votable {
    Voter(String name) {
        super(name);
    }

    @Override
    public Person vote(List<Person> candidates) {
        Random random = new Random();
        return candidates.get(random.nextInt(candidates.size()));
    }
}
