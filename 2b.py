def list_operations():
    subjects = ["Math", "Physics", "Chemistry", "Biology", "Python Programming Lab"]

    print("Subjects using for loop:")
    for subject in subjects:
        print(subject)


    print("\n2nd and 5th element of the list:")
    print(subjects[1], subjects[4])

  
    print("\nFirst 4 elements of the list:")
    print(subjects[:4])


    print("\nLast 4 elements of the list:")
    print(subjects[-4:])


    print("\nCheck if 'Python Programming Lab' is in the list:")
    print("Python Programming Lab" in subjects)

  
    subjects.append("Elective")
    subjects.insert(1, "English")
    print("\nList after append and insert operations:")
    print(subjects)


    subjects.remove("English")
    subjects.pop()
    print("\nList after remove and pop operations:")
    print(subjects)

list_operations()