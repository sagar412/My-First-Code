sagar = {
    'first_name':'Shailesh',
    'last_name':'Dwivedi',
    'age': 28,
    'city':'banaras',
}
ruchi = {
    'first_name':'Ruchika',
    'last_name':'Dwivedi',
    'age': 24,
    'city':'mumbai',
}
baby = {
    'first_name':'monty-shonty',
    'last_name':'Dwivedi',
    'age': 0,
    'city':'boston',
}
names = [sagar,ruchi,baby]
for name in names:
    print(f"\nThis person goes by the name of {name['first_name'].title()} {name['last_name'].title()}.He or she is {name['age']} old and lives in {name['city'].title()}." )
