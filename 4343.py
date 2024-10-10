
x = {
    "workers": {
        "Иванов": {
            "должность": "директор",
            "зарплата": 10000
        },
        "sanya": {
            "должность": "idk",
            "зарплата": 52
        }
    }
}
for name,dict_ in x.items():
    print( 'the name of the dictionary is ', name)
    print( 'the dictionary looks like ', dict_)