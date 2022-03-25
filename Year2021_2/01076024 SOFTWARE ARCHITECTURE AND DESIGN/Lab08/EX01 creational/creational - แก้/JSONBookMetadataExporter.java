//เพิ่มไฟล์

package creational;

import java.io.IOException;

public class JSONBookMetadataExporter extends BookMetadataExporter {

    @Override
    public BookMetadataFormatter buildbook() throws IOException {
        return new JSONBookMetadataFormatter();
    }

}