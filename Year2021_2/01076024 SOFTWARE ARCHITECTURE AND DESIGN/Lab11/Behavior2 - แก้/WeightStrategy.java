package edu.parinya.softarchdesign.behavior2;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class WeightStrategy implements SortStrategy {
    // YOU MAY ADD UP TO 5 LINES OF CODE BELOW THIS COMMENT !! A LINE OF CODE MAY CONTAIN UP TO ONE SEMI-COLON !!
    @Override
    public void customSort(List<Person> people) {
        Comparator<Person> byWeight = Comparator.comparing(Person::getWeight);
        Collections.sort(people, byWeight);
    }    
}
