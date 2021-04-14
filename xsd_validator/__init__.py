import subprocess
import re
import os

_JAR = os.path.join(os.path.dirname(__file__), 'resources', 'com.innodata.XsdValidator.jar')


class XsdValidator:

    def __init__(self, *xsds):
        self.xsds = xsds
        self._checked_java_installed = False

    def check_java_installation(self):
        subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)

    def __call__(self, filename):
        if not self._checked_java_installed:
            try:
                self.check_java_installation()
            except:
                raise RuntimeError('Could not find Java. Please make sure that Java is installed and is available in the PATH.')

            self._checked_java_installed = True

        output = subprocess.check_output([
            'java',
            '-jar',
            _JAR,
            *self.xsds,
            filename
        ])

        lines = [line.strip() for line in output.decode().split('\n') if line.strip()]
        for line in lines:
            mtc = re.search(r'systemId: (.+); lineNumber: (\d+); columnNumber: (\d+); (.+)$', line)
            if mtc is not None:
                line = int(mtc.group(2))
                column = int(mtc.group(3))
                message = mtc.group(4)
                yield XsdValidationErrorWithInfo(filename, line, column, message)
            else:
                yield XsdValidationError(line)

    def assert_valid(self, filename):
        for err in self(filename):
            raise err


class XsdValidationError(RuntimeError): pass


class XsdValidationErrorWithInfo(XsdValidationError):
    def __init__(self, filename, line, column, message):
        self.filename = filename
        self.line = line
        self.column = column
        self.message = message
        super().__init__(f'{filename}: line {line} column {column}: {message}')
