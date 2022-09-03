def f():
    #raise RuntimeError('not today')
    0/0

def g():
    try:
        f()
    except ZeroDivisionError as re:
        print(repr(re))
        print(f" {re} vyjímka: ojoj")

g()

try:

except: jen když to bouchne

else: jen když to nebouchne

finally: vždy

#breakpoint, kterým říkáme, že když se dostaneme na tento řádek, přeruší se exekuce a můžu se podívat co se tam děje
#potom to můžeme odbrzdit a zastavit to na další breakpoint, krokovat, doknčit
#main thread - stack trace říká v jakém stavu to je
#step over - pokračuje se dál bez zanořování, proběhne to, ale nekrokujeme uvnitř
#step into - opak step over
#step into my code - můžu volat fci kteoru jsem si sama napsala / naimporovala jsem si kod, a toto jde jen do fce jen když jsem ji sama napsala
#step out - vyskočím o uroven výš
#run to cursor - odbrzdím a dojede to až ke kurzoru
