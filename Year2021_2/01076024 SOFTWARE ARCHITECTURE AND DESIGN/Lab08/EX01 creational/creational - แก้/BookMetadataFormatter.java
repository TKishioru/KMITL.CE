//DO NOT MODIFY

package creational;

public interface BookMetadataFormatter {
    BookMetadataFormatter reset();
    BookMetadataFormatter append(Book b);
    String getMetadataString();
}
