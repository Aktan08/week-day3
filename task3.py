"""
Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре
различны. Выведите синоним для последнего слова.
"""
dict_ = {"asman":"nebo","aba":"vozduh","pepsi":"kola","net":"internet"}

poslednii_item = {dict_.popitem()}

newdict = {}

newdict.update(poslednii_item)

print(newdict.values())
print(newdict.get("net"))
