package edu.parinya.softarchdesign.government;

import java.util.List;

public interface Votable {
    Person vote(List<Person> candidates);
}
