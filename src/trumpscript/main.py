import os
import sys

from trumpscript.compiler import *
from trumpscript.utils import *

__author__ = 'github.com/samshadwell'


def main():
    # TrumpScript only runs in ascii mode. If you don't speak English
    # you can't write TrumpScript.
    sys.setdefaultencoding('ascii')

    if len(sys.argv) != 2:
        print("Invalid usage. Provide a TrumpScript file name to compile and run")
        print("Example: TRUMP trump_file.tr")
        return

    if not os.path.isfile(sys.argv[1]):
        print("Invalid file specified")
        return

    Utils.verify_system()
    Compiler().compile(sys.argv[1])


if __name__ == "__main__":
    main()
