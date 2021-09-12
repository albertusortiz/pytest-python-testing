people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def format_data_for_excel(people):

    nombres = ["given,family,title"]
    for field in range(len(people)):
        given_name = people[field]["given_name"]
        family_name = people[field]["family_name"]
        title =  people[field]["title"]
        persona = str(f"\n{given_name},{family_name},{title}")
        nombres.append(persona)
    
    cadena = "".join(nombres)
    return cadena+"\n"


print(format_data_for_excel(people))
print("""given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
""")


def test_format_data_for_excel():
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_excel(people) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""