package creational;

import java.io.PrintStream;

public abstract class BookMetadataExporter extends BookCollection {

    public void export(PrintStream stream) throws Exception {
        BookMetadataFormatter formatter = buildbook();
        for(Book n : books){
            formatter.append(n);
        }
        System.out.print(formatter.getMetadataString());        
    }
    
    public abstract BookMetadataFormatter buildbook() throws Exception;
}
