#!~/anaconda/envs/python36/python

from script1 import script1_foo, script1_bar


def script2_baz():
    print("Oi, from script2 baz()")


def script2_foobar():
    print("script2 foobar() says, 'sup...'")


script1_foo()
script1_bar()
script2_baz()
script2_foobar()
