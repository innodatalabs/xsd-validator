from xsd_validator import XsdValidator
from . import res


def test_pass():
    validator = XsdValidator(res('schema.xsd'))

    errors = [
        str(err) for err in validator(res('my0.xml'))
    ]

    assert errors == []

    validator.assert_valid(res('my0.xml'))


def test_fail():
    validator = XsdValidator(res('schema.xsd'))

    errors = [
        str(err) for err in validator(res('my1.xml'))
    ]

    assert errors == [
        res('my1.xml') + ': line 7 column 13: cvc-assertion: Assertion evaluation (\'if (./string(@flag)=\'true\') ' +
        'then not( ./components/component/string(@flag)=\'true\' ) else true()\') ' +
        'for element \'component\' on schema type \'#AnonType_component\' did not succeed.'
    ]
