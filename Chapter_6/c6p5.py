favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
people = ['jen','sagar','ruchika','sarah','phil',]
for name in people:
    print(f"\nHi {name}")
    if name in favorite_languages.keys():
        language = favorite_languages[name]
        print(f"I see you love {language}")
    else:
        print(f"{name.title()} please take our poll. ")
