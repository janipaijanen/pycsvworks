#!/usr/bin/env python

__author__ = "Jani Päijänen"
__copyright__ = "Copyright 2015, Jani Päijänen. All rights reserved"
__license__ = "New BSD License"
__version__ = "0.0.1"
__email__ = "jani dot paijanen+testreader at gmail dot com "
__status__ = "Testing"



from blitzdb import Document
from blitzdb import FileBackend
import os



class AdGroup(Document):
    pass

class AdAccount(Document):
    pass

def test1():


    domain_admins = AdGroup({'name': 'domain_admins'})

    marlon_brando = AdAccount({'name':'Marlon Brando', 'sAMAccountName':'mbrando'})
    al_pacino = AdAccount({'name' : 'Al Pacino', 'sAMAccountName':'apacino'})

    backend = FileBackend(os.path.join(os.getcwd(), "blitzdb1"))

    domain_admins.save(backend)
    marlon_brando.save(backend)
    al_pacino.save(backend)

    marlon_brando.member_of = [domain_admins]
    al_pacino.member_of = [domain_admins]

    domain_admins.save(backend)
    marlon_brando.save(backend)
    al_pacino.save(backend)

    backend.create_index(AdAccount, 'member_of')


def main():
    test1()

if __name__ == '__main__':
    main()
