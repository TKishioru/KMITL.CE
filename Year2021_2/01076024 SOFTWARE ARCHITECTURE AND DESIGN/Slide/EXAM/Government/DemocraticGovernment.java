package edu.parinya.softarchdesign.government;

import java.util.*;

public class DemocraticGovernment extends Government implements DemocraticSystem {
    public DemocraticGovernment(List<Voter> representatives, List<Person> leaderCandidates) {
        this.head = runElection(representatives, leaderCandidates);
    }

    @Override
    public Person runElection(List<Voter> representatives, List<Person> leaderCandidates) {
        HashMap<Person, Integer> voteCounts = new HashMap<>();
        for (Voter representative : representatives) {
            Person candidate = representative.vote(leaderCandidates);
            Integer voteCount = voteCounts.getOrDefault(candidate, 0);
            voteCounts.put(candidate, voteCount + 1);
        }
        return Collections.max(voteCounts.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
    }

    @Override
    public Person getHead() {
        return head;
    }
}
