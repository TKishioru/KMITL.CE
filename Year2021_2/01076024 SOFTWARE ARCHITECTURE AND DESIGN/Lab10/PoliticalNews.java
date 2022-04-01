package edu.parinya.softarchdesign.behavioral;

public class PoliticalNews extends News {
    PoliticalNews(String content) {super(content);}

    @Override
    public NewsTopic getTopic() {
        return NewsTopic.POLITICAL;
    }
}
