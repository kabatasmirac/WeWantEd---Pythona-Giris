meyveler = ["elma", "muz", 5, 5.8, True]
print (meyveler)


meyveler.remove("elma")                             #.remove  ==>  parantezde belirtilen elemani siler
print (meyveler)


meyveler.append("visne")                        #.append  ==> listenin sonuna belirtilen elemanı ekler.
print (meyveler)


meyveler.append("visne")
print (meyveler)


print ("\n")
print (meyveler.count("visne"))                 #.count   ==>  listede kac tane oldugunu sayar
print ("\n")


meyveler.insert(1, "karpuz")                    #.insert  ==> (indis, 'eklenecek eleman')
print (meyveler)


print (meyveler.pop(len(meyveler) - 1))         #.pop     ==> listenin sondan 1. elemanini atar.
print (meyveler)
