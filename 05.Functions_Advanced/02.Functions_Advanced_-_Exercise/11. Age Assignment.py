def age_assignment(*names, **all_ages):
    ages = {name: 0 for name in names}

    for first_letter, age in all_ages.items():
        for name in ages:
            if name.startswith(first_letter):
                ages[name] = age

    return ages


print(age_assignment("Peter", "George", G=26, P=19))