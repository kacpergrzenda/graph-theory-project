import re #https://docs.python.org/3/library/re.html
#http://ivanzuzak.info/noam/webapps/fsm_simulator/

myre = re.compile('a+b+')

examples = ['ab', 'aab', 'abb', 'aaabbb', 'ca', 'abab']

for e in examples:
    if myre.match(e):
        ismatch = True # Return True if the examples expression matches myre.
    else:
        ismatch = False
    print(f"{e} -> {ismatch}")