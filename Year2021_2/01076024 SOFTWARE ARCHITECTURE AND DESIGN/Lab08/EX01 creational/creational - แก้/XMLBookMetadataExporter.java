//เพิ่มไฟล์

package creational;

import java.io.IOException;
import javax.xml.parsers.ParserConfigurationException;


public class XMLBookMetadataExporter extends BookMetadataExporter {

    @Override
    public BookMetadataFormatter buildbook() throws IOException, ParserConfigurationException {
        return new XMLBookMetadataFormatter();
    }
}