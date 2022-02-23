#!/usr/bin/env python3
"""Quick little test showing how to get subclasses/use recursion"""

class Abc: pass
class Def(Abc): pass
class Hij(Abc): pass
class Klm(Hij): pass
class Xyz(Klm): pass
class GGG(Klm): pass
class DDD(GGG): pass
class XYZ(Abc): pass
class BBB(XYZ): pass
class CCC(BBB): pass
class JJJ(BBB): pass
class III(DDD): pass


def gimmie_subclasses(aclass):
    class_list = []
    for c in aclass.__subclasses__():
        if len(c.__subclasses__()) > 0: 
            o = gimmie_subclasses(c)
            [ class_list.append(i) for i in o ]
        class_list.append(c.__name__)
    return class_list


subclasses = gimmie_subclasses(Abc)
print(subclasses)

