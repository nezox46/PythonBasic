def thesaurus(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(thesaurus("Марк", "Амелия", 'Лола', 'Жека', 'Артем', 'Илья', 'Всеволод', 'Плотон'))
