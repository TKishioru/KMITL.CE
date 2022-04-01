package edu.parinya.softarchdesign.structural;

import java.time.LocalDateTime;  // Import the LocalDateTime class
import java.time.format.DateTimeFormatter;  // Import the DateTimeFormatter class

public class TimeLoggingHealthcareWorker extends HealthcareWorkerDecorator {
    
    public TimeLoggingHealthcareWorker(HealthcareWorker worker) {
        super(worker);
        System.out.println("Decorate " + worker.getName() + " with TimeLogging.");
    }
    
    @Override
    public void service() {
        LocalDateTime Dtime = LocalDateTime.now();  
        DateTimeFormatter Ftime = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");  
        String formattedDate = Dtime.format(Ftime);  
        System.out.print(formattedDate + " : "); 
        
        super.service();
    }
}
