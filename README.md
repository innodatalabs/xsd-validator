# xsd_validator
![xsd_validator](https://github.com/innodatalabs/xsd-validator/actions/workflows/test.yaml/badge.svg)
![PyPI version](https://badge.fury.io/py/xsd-validator.svg)](https://badge.fury.io/py/xsd-validator)

Validates an XML file against XSDs, supports XSD version 1.1. Requires Java Runtime.

## API

Assert that `my.xml` is valid according to schema `schema.xsd`:
```python
from xsd_validator import XsdValidator

validator = XsdValidator('schema.xsd')
validator.assert_valid('my.xml')
```

A more complex schema may be split between several files, for example: `schema.xsd`, `schema-aux.xsd` and `xml.xsd`.
Just pass them all to the `XsdValidator`:

```python
from xsd_validator import XsdValidator

validator = XsdValidator('schema.xsd', 'schema-aux.xsd', 'xml.xsd')
validator.assert_valid('my.xml')
```

Sometimes you need to get all problems discovered. You can loop through the errors like this:
```python
from xsd_validator import XsdValidator

validator = XsdValidator('schema.xsd', 'schema-aux.xsd', 'xml.xsd')
for err in validator('my.xml'):
    print(err)
```

## CLI

You can use `xsd_validator` module as an executable, like this:
```bash
python -m xsd_validator
```

For example:
```bash
python -m xsd_validator schema.xsd my.xml
```

Help:
```bash
python -m xsd_validator -husage: xsd_validator [-h] xsd [xsd ...] xml

Validate an XML file againsd XSD schema (supports XSD version 1.1)

positional arguments:
  xsd         XSD files
  xml         XML file to check

optional arguments:
  -h, --help  show this help message and exit
```
