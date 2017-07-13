#!~/anaconda/envs/python36/bin/python

import script2


def script1_foo():
    print("Hello from script1 foo().")


def script1_bar():
    print("Alo' from script1 bar()")


if __name__ == '__main__':
    print("Running as {} from script1".format(__name__))
    script1_foo()
    script2.script2_baz()
    script1_bar()
    script2.script2_foobar()
