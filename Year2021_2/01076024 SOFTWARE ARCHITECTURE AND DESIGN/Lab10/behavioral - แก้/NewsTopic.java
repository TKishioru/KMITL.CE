package edu.parinya.softarchdesign.behavioral;

public enum NewsTopic {
    ECONOMIC("ECONOMIC"),
    POLITICAL("POLITICAL"),
    TECHNOLOGY("TECHNOLOGY");

    public final String value;

    NewsTopic(String value) {
        this.value = value;
    }
}
