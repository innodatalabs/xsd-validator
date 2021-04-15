To create an executable JAR file do the following:

Unpack Xerces classes
```
jar x xercesImpl.jar
jar x org.eclipse.wst.xml.xpath2.processor_1.2.0.jar
```

Compile
```
javac -target 8 -source 8 -Xlint:-options com/innodata/XsdValidator.java
```

Finally package JAR
```
jar cvfe com.innodata.XsdValidator.jar com.innodata.XsdValidator org com META-INF
```

You can get binary Xerces distribution here: http://xerces.apache.org/mirrors.cgi