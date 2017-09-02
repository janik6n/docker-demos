#!/usr/bin/env python

import sys
from libvoikko import Voikko

print('Analysoidaan annetut sanat:\n')

v = Voikko("fi")

# Pass the 1st argument as it is the app name itself.
for a in sys.argv[1:]:
    print(f'Sanan {a} analyysi:')
    print(v.analyze(a))

print('Annetut sanat analysoitu.')
