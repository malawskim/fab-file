#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Fabric==1.10.2','console_scripts','fab'
__requires__ = 'Fabric==1.10.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Fabric==1.10.2', 'console_scripts', 'fab')()
    )
