package creational;

import org.apache.commons.lang3.StringUtils;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.StringWriter;

public class XMLBookMetadataFormatter implements BookMetadataFormatter {

    private Document document;
    private Element rootElement;

    public XMLBookMetadataFormatter() throws ParserConfigurationException {
        reset();
    }

    public BookMetadataFormatter reset() {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder;
        try {
            builder = factory.newDocumentBuilder();
            document = builder.newDocument();
            rootElement = document.createElement(Book.class.getSimpleName() + "s");
            document.appendChild(rootElement);
        } catch (ParserConfigurationException e) {
            e.printStackTrace();
        }
        return this;
    }

    @Override
    public BookMetadataFormatter append(Book b) {
        Element e;
        e = document.createElement(Book.class.getSimpleName());
        e.setAttribute("id", b.getISBN());
        e.appendChild(createXmlNode(Book.Metadata.TITLE.value, b.getTitle()));
        e.appendChild(createXmlNode(Book.Metadata.PUBLISHER.value, b.getPublisher()));

        Element authors = document.createElement(Book.Metadata.AUTHORS.value);
        for (String author : b.getAuthors()) {
            authors.appendChild(createXmlNode(StringUtils.chop(Book.Metadata.AUTHORS.value), author));
        }
        e.appendChild(authors);

        rootElement.appendChild(e);
        return this;
    }

    private Node createXmlNode(String name, String value) {
        Element node = document.createElement(name);
        node.appendChild(document.createTextNode(value));
        return node;
    }

    @Override
    public String getMetadataString() {
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        try {
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            DOMSource source = new DOMSource(document);
            StringWriter writer = new StringWriter();
            StreamResult result = new StreamResult(writer);
            transformer.transform(source, result);
            return writer.toString();
        } catch (TransformerConfigurationException e) {
            e.printStackTrace();
            return null;
        } catch (TransformerException e) {
            e.printStackTrace();
            return null;
        }
    }
}
