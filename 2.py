def ruck():
    weigh = int(input("Введдите грузоподъемность: "))
    items = {"вода": 1, "еда": 10, "посуда": 3, "одежда": 10, "фонарь": 0.5, "нож": 0.3, "розжиг": 0.1}
    list = []
    items = dict(sorted(items.items(), key = lambda item: item[1]))
    for item in items :
        if items [item]<weigh:
            list.append(item)
            weigh-=items[item]
    return print(list)
ruck()