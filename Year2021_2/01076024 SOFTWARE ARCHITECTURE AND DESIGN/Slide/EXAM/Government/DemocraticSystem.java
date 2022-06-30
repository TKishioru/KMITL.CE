package edu.parinya.softarchdesign.government;

import java.util.List;

public interface DemocraticSystem {
    Person runElection(List<Voter> representatives, List<Person> leaderCandidates);
}
