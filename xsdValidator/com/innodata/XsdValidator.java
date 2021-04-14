package com.innodata;

import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXParseException;
import java.io.File;
import java.util.Arrays;


public class XsdValidator {

    public static void main(String[] args) throws Exception {

        if (args.length < 2) {
            System.out.println("USAGE: main <xsd1> <xsd2> ... <xsdN> <xml>");
            System.exit(-1);
        }

        String [] xsdFileNames = Arrays.copyOfRange(args, 0, args.length - 1);
        String xmlFileName = args[args.length - 1];

        SchemaFactory sf = SchemaFactory.newInstance("http://www.w3.org/XML/XMLSchema/v1.1");
        StreamSource[] schemaDocuments = new StreamSource[xsdFileNames.length];
        for (int i = 0; i < xsdFileNames.length; i++) {
            schemaDocuments[i] = new StreamSource(new File(xsdFileNames[i]));
        }

        Schema s = sf.newSchema(schemaDocuments);
        Validator v = s.newValidator();
        MyErrorHandler h = new MyErrorHandler();
        v.setErrorHandler(h);
        v.validate(new StreamSource(xmlFileName));

        if (h.errors.length > 0) {
            for (SAXParseException err : h.errors) {
                System.err.println(err);
            }
            System.exit(-1);
        } else if(h.warnings.length > 0) {
            for (SAXParseException err : h.errors) {
                System.err.println(err);
            }
            System.exit(-1);
        } else {
            System.exit(0);
        }
    }
}

class MyErrorHandler implements ErrorHandler {

    public SAXParseException[] errors = {};
    public SAXParseException[] warnings = {};


    public void error(SAXParseException ex) {
        System.out.println(ex);
    }

    public void fatalError(SAXParseException ex) {
        System.err.println(ex);
    }

    public void warning(SAXParseException ex) {
        System.out.println(ex);
    }

}