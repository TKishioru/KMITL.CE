package edu.parinya.softarchdesign.behavioral;

import java.util.concurrent.Flow.Subscriber;
import java.util.concurrent.Flow.Subscription;

public class NewsSubscriber implements Subscriber<News> {
    // You need to implement this class
    
    private final String reader;
    
    NewsSubscriber(String reader) {
        this.reader = reader;
    }

    @Override
    public void onSubscribe(Subscription subscription) {
        System.out.println("Subscribe in NewsSubscriber");
        System.out.println(reader + " subscribed to " + subscription.getClass().getName());
    }

    @Override
    public void onNext(News item) {
        //System.out.println("Next in NewsSubscriber");
        System.out.println(reader + " get the news : " + item.getContent());
    }

    @Override
    public void onError(Throwable throwable) {
        System.out.println("Error in NewsSubscriber");
    }

    @Override
    public void onComplete() {
        System.out.println("Complete in NewsSubscriber");
    }

    

   
    
}
