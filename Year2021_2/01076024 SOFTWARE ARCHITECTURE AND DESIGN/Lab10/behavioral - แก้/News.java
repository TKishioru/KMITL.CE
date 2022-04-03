package edu.parinya.softarchdesign.behavioral;

public abstract class News {
    private String content;
    private NewsTopic topic;

    public News() {
        this("");
    }

    public News(String content) {
        this.content = content;
        this.topic = getTopic();
    }

    public abstract NewsTopic getTopic();

    public String getContent() {
        return this.content;
    }
}
