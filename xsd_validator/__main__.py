from xsd_validator import XsdValidator
import argparse

parser = argparse.ArgumentParser(prog='xsd_validator', description='Validate an XML file againsd XSD schema (supports XSD version 1.1)')

parser.add_argument('xsd', nargs='+', help='XSD files')
parser.add_argument('xml', help='XML file to check')

args = parser.parse_args()

validator = XsdValidator(*args.xsd)

count = 0
for err in validator(args.xml):
    print(err)
    count += 1

if count == 0:
    print('All good')
    parser.exit(0)

parser.exit(-1)