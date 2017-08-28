import operator


def solution_asc(dic):
    lst1 = sorted(list(dic.items()), key = operator.itemgetter(0))
    return lst1


def solution_desc(dic):
    lst2 = sorted(list(dic.items()), key = operator.itemgetter(0), reverse = True)
    return lst2
