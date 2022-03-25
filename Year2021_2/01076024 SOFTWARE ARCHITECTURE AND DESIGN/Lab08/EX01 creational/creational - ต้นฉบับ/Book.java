package creational;


public class Book {
    public enum Metadata {
        ISBN("ISBN"),
        TITLE("Title"),
        PUBLISHER("Publisher"),
        AUTHORS("Authors");

        public final String value;

        private Metadata(String value) {
            this.value = value;
        }

        public static String getValue(Metadata m) {
            return m.value;
        }
    }

    private String ISBN;
    private String title;
    private String publisher;
    private String[] authors;

    public Book(String isbn, String title, String publisher, String... authors) {
        this.ISBN = isbn;
        this.title = title;
        this.publisher = publisher;
        this.authors = authors;
    }

    public String getISBN() {
        return ISBN;
    }

    public String getTitle() {
        return title;
    }

    public String getPublisher() {
        return publisher;
    }

    public String[] getAuthors() {
        return authors;
    }
}
