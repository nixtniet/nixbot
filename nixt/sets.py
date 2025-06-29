# This file is placed in the Public Domain.


"sets"


"""
1. Doorsnede (intersectie):
De doorsnede van twee verzamelingen A en B, notatie A ∩ B, is de verzameling die alle elementen bevat die zowel in A als in B zitten. 
2. Vereniging (unie):
De vereniging van twee verzamelingen A en B, notatie A ∪ B, is de verzameling die alle elementen bevat die in A of in B zitten (of in beide). 
3. Verschil:
Het verschil van verzameling A en B, notatie A \ B of A - B, is de verzameling die alle elementen bevat die in A zitten, maar niet in B. 
4. Complement:
Het complement van een verzameling A (ten opzichte van een universele verzameling U), notatie A', of Ac, is de verzameling die alle elementen bevat die niet in A zitten, maar wel in U. 
5. Machtsverzameling:
De machtsverzameling van een verzameling A, notatie P(A) of 2^A, is de verzameling van alle deelverzamelingen van A. 
6. Cartesiaans product:
Het Cartesiaans product van twee verzamelingen A en B, notatie A x B, is de verzameling van alle geordende paren (a, b) waarbij a behoort tot A en b behoort tot B. 
"""

def cartes(obj, other):
    pass


def complement(obj, other):
    pass


def diff(obj, other):
    pass


def power(obj, other):
    pass


def section(obj, other):
    pass


def union(obj, other):
    pass


def __dir__():
    return (
        'cartes',
        'complement',
        'diff',
        'power',
        'section',
        'union'
    )
