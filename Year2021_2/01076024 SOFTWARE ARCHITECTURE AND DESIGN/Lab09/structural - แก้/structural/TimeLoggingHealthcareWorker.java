package edu.parinya.softarchdesign.structural;

import java.time.LocalDateTime;  // Import the LocalDateTime class
import java.time.format.DateTimeFormatter;  // Import the DateTimeFormatter class

public class TimeLoggingHealthcareWorker extends HealthcareWorkerDecorator {
    
    public TimeLoggingHealthcareWorker(HealthcareWorker worker) {
        super(worker);
        System.out.printf("Decorate %s with TimeLogging.\n", worker.getName());
    }
    
    @Override
    public void service() {
        LocalDateTime Dtime = LocalDateTime.now();  
        DateTimeFormatter Ftime = DateTimeFormatter.ofPattern("E MMM dd HH:mm:ss" + " ICT " + "yyyy");  
        String formattedDate = Dtime.format(Ftime);  
        System.out.println(formattedDate); 
        
        super.service();
    }
}
