package edu.parinya.softarchdesign.government;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<Voter> usRepresentatives = Collections.nCopies(538, new Voter("Elector"));
        List<Person> potusCandidates = new LinkedList<>();
        potusCandidates.add(new Person("Biden"));
        potusCandidates.add(new Person("Trump"));
        DemocraticGovernment usGov = new DemocraticGovernment(usRepresentatives, potusCandidates);
        Person potus = usGov.getHead();
        System.out.println("======== US ========");
        System.out.println("The head of US government is " + potus.getName());
        System.out.println("Was " + potus.getName() + " a POTUS candidate?: " + potusCandidates.contains(potus));

        List<Voter> representatives = Collections.nCopies(500, new Voter("Member of Parliament"));
        List<Person> pmCandidates = new LinkedList<>();
        pmCandidates.add(new Person("Takky"));
        pmCandidates.add(new Person("Mark"));
        pmCandidates.add(new Person("Pu"));
        pmCandidates.add(new Person("Thanon"));
        DemocraticGovernment thGov = new ThDemocraticGovernment(representatives, pmCandidates);
        Person pm = thGov.getHead();
        System.out.println("======== TH ========");
        System.out.println("The head of government is " + pm.getName());
        System.out.println("Was " + pm.getName() + " a PM candidate?: " + pmCandidates.contains(pm));
    }
}
