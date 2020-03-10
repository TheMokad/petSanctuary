# Author: Mohammed Kadir (18010426)
# Description: A Database system for an animal sanctuary

import csv
from Pets import Pets
from Treatment import Treatments
from Wild import Wild

pet_data = []
wild_data = []
treatment_data = []

def bubblesort(arr):
    n = len(arr)

    # iterate through the whole array
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Function: Main menu
# Description: Prints out options and directs user to other 
#       functions based on option that is picked
# Parameters: none
# Returns: none
def menu():
    print("=========")
    print("|Welcome|")
    print("=========")
    
    print("1. Create a new animal entry ")
    print("2. Search the Database ")
    print("3. Search for person")
    print("4. View list of pets ready for adoption")
    print("5. View list of animals ready to be returned to owner")
    print("6. Edit an animals information")
    print("7. Edit an animals treatment information")
    print("0. Exit Program")


    choose = input("")

    if choose == "0":
        print("Exiting the program")
        exit()

    elif choose == "1":
        print("1. Add a new Pet Entry ")
        print("2. Add a new wild animal Entry ")
        print("3. Add a treatment Entry ")

        option = input()

        if option == "1":
            add_pet()

        elif option == "2":
            add_wild()

        elif option == "3":
            add_treatment()
        else:
            menu()

    elif choose == "2":
        searchID()

    elif choose == "3":
        print("1. List of people who have abused an animal in the past")
        print("2. List of people who have abandoned an animal in the past")
        option = input()

        if option == "1":
            reader_abused()
        elif option == "2":
            reader_abandoned()
        else:
            menu()

    elif choose == "4":
        print("1. List of cats ready for adoption")
        print("2. List of dogs ready for adoption")
        option = input()

        if option == "1":
            ready_for_adoption("Cat")
        elif option == "2":
            ready_for_adoption("Dog")
        else:
            menu()

    elif choose == "5":
        print("List of animals ready to be returned to owner")
        ready_for_return()

    elif choose == "6":
        print("1. Edit a pet's information")
        print("2. Edit a wild animals information")
        option = input()

        if option == "1":
            edit_menu_pet()
        elif option == "2":
            edit_menu_wild()
        else:
            menu()

    elif choose == "7":
        edit_menu_treat()

    else:
        print("Please enter an option from the menu")
        input("Press enter to continue...")
        menu()

    input("\n\nPress Enter to continue...")
    print("\n\n\n\n\n\n\n\n\n\n")
    menu()


# Function: Load pet data
# Description: Loads pet data into the data structure
# Parameters: none
# Returns: none, can print out the contents of the data structure
def load_pet_data():
    with open("DADSA 2019-20 CWK A DATA PETS.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader, None)
        for row in reader:
            pet_data.append(Pets(row[0], row[1], row[2], row[3], row[4], row[5],
                                  row[6], row[7], row[8], row[9], row[10]))
        bubblesort(pet_data)
        # for row in pet_data:
        #     print(row)


# Function: Load wild data
# Description: Loads wild data into the data structure
# Parameters: none
# Returns: none, can print out the contents of the data structure
def load_wild_data():
    with open("DADSA 2019-20 CWK A WILD ANIMALS.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader, None)
        for row in reader:        # Add you wild class underneath
            wild_data.append(Wild(row[0], row[1], row[2], row[3], row[4], row[5],
                                row[6], row[7]))
        bubblesort(wild_data)
        # for row in wild_data:
        #     print(row)


# Function: Load treatment data
# Description: Loads pet data into the data structure
# Parameters: none
# Returns: none, can print out the contents of the data structure
def load_treatment_data():
    with open("DADSA 2019-20 CWK A TREATMENT.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader, None)
        for row in reader:
            treatment_data.append(Treatments(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        bubblesort(treatment_data)
        # for row in treatment_data:
        #     print(row)


# Function: Load all data
# Description: Loads pet data, wild data and treatment data
#       into the data structure
# Parameters: none
# Returns: none
def load_sort_data():
    load_pet_data()
    load_wild_data()
    load_treatment_data()


# Function: Ask user, Yes or No input
# Description: Forces user to choose to enter Yes or No strings
# Parameters: question, this inserts the adjective used to describe the question
#       eg, neutered or vaccinated
# Returns: either Yes, or empty string. This is put into the csv file
def askYesNo(question):
    previousQuestion = question
    print("Is the animal " + question)
    print("1. Yes")
    print("2. No")
    option = input("")
    
    if option == "1":
        outcome = "Yes"
        return outcome
    elif option == "2":
        outcome = ""
        return outcome
    else:
        return askYesNo(previousQuestion)


# Function: add pet
# Description: Takes input from the user, one variable at a time. 
#       Inserts those into a list called row, 
#       which is then appended into the data structure
# Parameters: none
# Returns: none
def add_pet():
    animalID = input("Enter ID: ")
    type_pet = input("Enter type of pet: ")
    breed = input("Enter breed: ")

    vaccinated = askYesNo("vaccinated")
    neutered = askYesNo("neutered")

    micro_chipped = input("What your pet microchip number: ")
    admission = input("Reason for Admission: ")
    arrival = input("Enter Date of Arrival: ")
    departure = input("Enter Date of departure: ")
    destination = input("Please enter destination: ")
    destination_address = input("Please enter destination address: ")

    row = [animalID, type_pet, breed, vaccinated, neutered, micro_chipped, admission,
           arrival, departure, destination, destination_address]

    with open('DADSA 2019-20 CWK A DATA PETS.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)
        pet_data.append(Pets(animalID, type_pet, breed, vaccinated, neutered, micro_chipped, admission,
           arrival, departure, destination, destination_address))
        csv_file.close()
        print("Thank you: ")
        print(row)
    
    load_sort_data()


# Function: add wild animal
# Description: Takes input from the user, one variable at a time. 
#       Inserts those into a list called row, 
#       which is then appended into the data structure
# Parameters: none
# Returns: none
def add_wild():
    animalID = input("Enter ID: ")
    wild_type = input("Enter type of animal: ")
    vaccinated = askYesNo("vaccinated")
    admission_reason = input("Reason for admission: ")
    arrival = input("Enter Date of Arrival")
    departure = input("Enter Date of departure")
    destination = input("Please enter destination")
    destination_address = input("Please enter destination address")

    row = [animalID, wild_type, vaccinated, admission_reason, arrival, departure,
           destination, destination_address]

    with open('DADSA 2019-20 CWK A WILD ANIMALS.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)
        wild_data.append(Wild(animalID, wild_type, vaccinated, admission_reason, arrival, departure,
           destination, destination_address))
        csv_file.close()
        print("Thank you: ")
        print(row)
    
    load_sort_data()


# Function: add treatment information
# Description: Takes input from the user, one variable at a time. 
#       Inserts those into a list called row, 
#       which is then appended into the data structure
# Parameters: none
# Returns: none
def add_treatment():
    animalID = input("Enter treatment ID: ")
    treat_surgery = input("Enter surgery: ")
    surgery_date = input("Enter surgery date: ")
    medication = input("Enter medication: ")
    med_start = input("Enter medication start date: ")
    med_end = input("Enter medication end date: ")
    responsible_abuse = input("Enter person responsible for abuse: ")
    responsible_abandoned = input("Enter person responsible for abandoning: ")

    row = [animalID, treat_surgery, surgery_date, medication, med_start, med_end, responsible_abuse,
                 responsible_abandoned]

    with open('DADSA 2019-20 CWK A TREATMENT.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)
        treatment_data.append(Treatments(animalID, treat_surgery, surgery_date, medication, med_start, med_end, responsible_abuse,
                 responsible_abandoned))
        csv_file.close()
        print("Thank you: ")
        print(row)
    
    load_sort_data()

# Function: Binary Search
# Description: Searches for ID by using divide and conquer techique
#       Allo
# Parameters: lys, any of the three data structures.
#       val, id of animal user is searching for
# Returns: returns the information about the animal. 
#       or returns -1/none if animal is not found
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1

    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid].animalID == val:
            index = mid
            return lys[index]
        else:
            if val < lys[mid].animalID:
                last = mid -  1
            else:
                first = mid + 1

    if index == -1:
        return index


# Function: Search for ID
# Description: Compares the input from the user to the data structures 
#       using the binary search function
# Parameters: none
# Returns: none
def searchID():
    search_id = input("Enter the ID for pet you want to search: ")

    animal = BinarySearch(pet_data, search_id)

    if animal == -1:
        animal = BinarySearch(wild_data, search_id)
    
    if animal != -1:
        print(animal)

        animalTreatment = BinarySearch(treatment_data, search_id)

        if animalTreatment == -1:
            print("")
            print("This animal has no medical information in our system")
        else:
            print(animalTreatment)

    else:
        print("Animal Could not be found.")

        chosen = False
        while chosen == False:
            print("1. Search again")
            print("2. Return to menu")
            choice = input("")
            if choice == "1":
                chosen = True
                searchID()
            elif choice == "2":
                chosen = True
                menu()
    
# Function: Reader Abused
# Description: iterates through data structure to find people who have abused animals
#       making sure not to take same person in twice
# Parameters: none
# Returns: none
def reader_abused():
    abuse_list = []

    print("List of people that have abused animals: ")
    for i in treatment_data:
        if i.responsible_abuse != "" and i.responsible_abuse not in abuse_list:
            abuse_list.append(i.responsible_abuse)
    bubblesort(abuse_list)
    print(abuse_list)


# Function: Reader Abandon
# Description: iterates through data structure to find people who have abandoned animals
#       making sure not to take same person in twice
# Parameters: none
# Returns: none
def reader_abandoned():
    abandon_list = []

    print("List of people that have abandoned animals: ")
    for i in treatment_data:
        if i.responsible_abandoned != "" and i.responsible_abuse not in abandon_list:
            abandon_list.append(i.responsible_abandoned)
    bubblesort(abandon_list)
    print(abandon_list)


# Function: Ready for adoption
# Description: Iterates through pet data to find animals which are ready to be adopted
#       based on whether they are vaccinated, neutered and have a microchip
# Parameters: none
# Returns: none
def ready_for_adoption(type):
    adoption_ready = []

    print("List of " + type + "'s Ready for adoption: ")

    for i in pet_data:
        if i.pet_type == type and i.vaccinated != "" and i.neutered != "" and i.micro_chip != "":
            adoption_ready.append(i.animalID)
    bubblesort(adoption_ready)
    print(adoption_ready)


# Function: Ready for return
# Description: iterates through the data structures to find animals which are ready for return
# Parameters: none
# Returns: none
def ready_for_return():
    return_ready = []

    for i in pet_data:
        if i.destination == "":
            return_ready.append(i.animalID)

    for i in wild_data:
        if i.destination == "":
            return_ready.append(i.animalID)
    bubblesort(return_ready)
    print(return_ready)


# Function: Edit pet object
# Description: Edits the pet that is inserted through the parameter
#       then rewrites the whole csv file
# Parameters: pet_id_to_edit. ID of the pet
# Returns: none
def edit_pet(pet_id_to_edit):
    c = csv.reader(open('DADSA 2019-20 CWK A DATA PETS.csv'))
    lines = list(c)

    for row in lines:
        if row[0] == pet_id_to_edit.animalID:
            row[1] = pet_id_to_edit.pet_type
            row[2] = pet_id_to_edit.breed
            row[3] = pet_id_to_edit.vaccinated
            row[4] = pet_id_to_edit.neutered
            row[5] = pet_id_to_edit.micro_chip
            row[6] = pet_id_to_edit.admission_reason
            row[7] = pet_id_to_edit.arrival
            row[8] = pet_id_to_edit.departure
            row[9] = pet_id_to_edit.destination
            row[10] = pet_id_to_edit.destination_address

    writer = csv.writer(open('DADSA 2019-20 CWK A DATA PETS.csv', 'w', newline=""))
    writer.writerows(lines)
    print(pet_id_to_edit)


# Function: Edit wild object
# Description: Edits the wild animal that is inserted through the parameter
#       then rewrites the whole csv file
# Parameters: wild_id_to_edit. ID of the animal
# Returns: none
def edit_wild(wild_id_to_edit):
    c = csv.reader(open('DADSA 2019-20 CWK A WILD ANIMALS.csv'))
    lines = list(c)

    for row in lines:
        if row[0] == wild_id_to_edit.animalID:
            row[1] = wild_id_to_edit.wild_type
            row[2] = wild_id_to_edit.vaccinated
            row[3] = wild_id_to_edit.admission_reason
            row[4] = wild_id_to_edit.arrival
            row[5] = wild_id_to_edit.departure
            row[6] = wild_id_to_edit.destination
            row[7] = wild_id_to_edit.destination_address

    writer = csv.writer(open('DADSA 2019-20 CWK A WILD ANIMALS.csv', 'w', newline=""))
    writer.writerows(lines)
    print(wild_id_to_edit)


# Function: Edit treat object
# Description: Edits the animal that is inserted through the parameter
#       then rewrites the whole csv file
# Parameters: treat_id_to_edit. ID of the animal
# Returns: none
def edit_treat(treat_id_to_edit):
    c = csv.reader(open('DADSA 2019-20 CWK A TREATMENT.csv'))
    lines = list(c)

    for row in lines:
        if row[0] == treat_id_to_edit.animalID:
            row[1] = treat_id_to_edit.treat_surgery
            row[2] = treat_id_to_edit.surgery_date
            row[3] = treat_id_to_edit.medication
            row[4] = treat_id_to_edit.med_start
            row[5] = treat_id_to_edit.med_end
            row[6] = treat_id_to_edit.responsible_abuse
            row[7] = treat_id_to_edit.responsible_abandoned

    writer = csv.writer(open('DADSA 2019-20 CWK A TREATMENT.csv', 'w', newline=""))
    writer.writerows(lines)
    print(treat_id_to_edit)


# Function: Menu to edit a pet
# Description: Asks user for ID of pet they want to edit, 
#       uses binary search to find it, then calls edit_pet to inser the input
# Parameters: none
# Returns: none
def edit_menu_pet():
    pet_edit = input("Enter Pet ID: ")
    pet = BinarySearch(pet_data, pet_edit)
    if pet == -1:
        print("ID not found, please enter another ID: ")
        edit_menu_pet()
    print(pet)
    print("")

    optionChosen = False

    while not optionChosen:

        print("What would you like to edit? ")
        print("1. Pet type: ")
        print("2. Breed: ")
        print("3. Vaccination: ")
        print("4. Neutered: ")
        print("5. Microchip Number: ")
        print("6. Admission Reason: ")
        print("7. Arrival Date: ")
        print("8. Departure Date: ")
        print("9. Destination: ")
        print("10. Destination Address: ")
        print("0. Return to menu")

        n = input("\n Please choose an option: ")

        if n == "1":
            print("Add your new detail here: ")
            pet_type = input().title()
            pet.pet_type = pet_type
            edit_pet(pet)

        elif n == "2":
            print("Add your new detail here: ")
            breed = input().title()
            pet.breed = breed
            edit_pet(pet)

        elif n == "3":
            print("Add your new detail here: ")
            vaccinated = input().title()
            pet.vaccinated = vaccinated
            edit_pet(pet)

        elif n == "4":
            print("Add your new detail here: ")
            neutered = input().title()
            pet.neutered = neutered
            edit_pet(pet)

        elif n == "5":
            print("Add your new detail here: ")
            micro_chip = input().title()
            pet.micro_chip = micro_chip
            edit_pet(pet)

        elif n == "6":
            print("Add your new detail here: ")
            admission_reason = input().title()
            pet.admission_reason = admission_reason
            edit_pet(pet)

        elif n == "7":
            print("Add your new detail here: ")
            arrival = input().title()
            pet.arrival = arrival
            edit_pet(pet)

        elif n == "8":
            print("Add your new detail here: ")
            departure = input().title()
            pet.departure = departure
            edit_pet(pet)

        elif n == "9":
            print("Add your new detail here: ")
            destination = input().title()
            pet.destination = destination
            edit_pet(pet)

        elif n == "10":
            print("Add your new detail here: ")
            destination_address = input().title()
            pet.destination_address = destination_address
            edit_pet(pet)
        
        elif n == "0":
            menu()
            optionChosen = True


# Function: Menu to edit a wild animal
# Description: Asks user for ID of animal they want to edit, 
#       uses binary search to find it, then calls edit_wild to inser the input
# Parameters: none
# Returns: none
def edit_menu_wild():
    wild_edit = input("Enter Wild Animal ID: ")
    wild = BinarySearch(wild_data, wild_edit)
    if wild == -1:
        print("ID not found, please enter another ID: ")
        edit_menu_wild()
    print(wild)
    print("")

    optionChosen = False

    while not optionChosen:
        print("What would your like to edit? ")
        print("1. Type: ")
        print("2. Vaccination: ")
        print("3. Neutered: ")
        print("4. Arrival Date: ")
        print("5. Departure Date: ")
        print("6. Destination: ")
        print("7. Destination Address: ")
        print("0. Return to menu")

        n = input("\n Please choose an option: ")

        if n == "1":
            print("Add your new detail here: ")
            wild_type = input().title()
            wild.wild_type = wild_type
            edit_wild(wild)

        elif n == "2":
            print("Add your new detail here: ")
            breed = input().title()
            wild.breed = breed
            edit_wild(wild)

        elif n == "3":
            print("Add your new detail here: ")
            vaccinated = input().title()
            wild.vaccinated = vaccinated
            edit_wild(wild)

        elif n == "4":
            print("Add your new detail here: ")
            neutered = input().title()
            wild.neutered = neutered
            edit_wild(wild)

        elif n == "5":
            print("Add your new detail here: ")
            micro_chip = input().title()
            wild.micro_chip = micro_chip
            edit_wild(wild)

        elif n == "6":
            print("Add your new detail here: ")
            admission_reason = input().title()
            wild.admission_reason = admission_reason
            edit_wild(wild)

        elif n == "7":
            print("Add your new detail here: ")
            arrival = input().title()
            wild.arrival = arrival
            edit_wild(wild)

        elif n == "0":
            menu()
            optionChosen = True


# Function: Menu to edit a treatment
# Description: Asks user for ID of animal they want to edit, 
#       uses binary search to find it, then calls edit_treat to inser the input
# Parameters: none
# Returns: none
def edit_menu_treat():
    treat_edit = input("Enter Animal's ID: ")
    treat = BinarySearch(treatment_data, treat_edit)
    if treat == -1:
        print("ID not found, please enter another ID: ")
        edit_menu_treat()
    print(treat)
    print("")

    optionChosen = False

    while not optionChosen:

        print("What would your like to edit? ")
        print("1. Surgery: ")
        print("2. Surgery Date: ")
        print("3. Medication: ")
        print("4. Medication Start Date: ")
        print("5. Medication End Date: ")
        print("6. Responsible for abuse: ")
        print("7. Responsible for abandoned: ")
        print("0. Return to menu")
    
        n = input("\n Please choose an option: ")

        if n == "1":
            print("Add your new detail here: ")
            treat_surgery = input().title()
            treat.treat_surgery = treat_surgery
            edit_treat(treat)

        elif n == "2":
            print("Add your new detail here: ")
            surgery_date = input().title()
            treat.surgery_date = surgery_date
            edit_treat(treat)

        elif n == "3":
            print("Add your new detail here: ")
            medication = input().title()
            treat.medication = medication
            edit_treat(treat)

        elif n == "4":
            print("Add your new detail here: ")
            med_start = input().title()
            treat.med_start = med_start
            edit_treat(treat)

        elif n == "5":
            print("Add your new detail here: ")
            med_end = input().title()
            treat.med_end = med_end
            edit_treat(treat)

        elif n == "6":
            print("Add your new detail here: ")
            responsible_abuse = input().title()
            treat.responsible_abuse = responsible_abuse
            edit_treat(treat)

        elif n == "7":
            print("Add your new detail here: ")
            responsible_abandon = input().title()
            treat.responsible_abandon = responsible_abandon
            edit_treat(treat)
        
        elif n == "0":
            menu()
            optionChosen = True

# Function: main
# Description: Loads data and runs the menu
# Parameters: none
# Returns: none
def main():
    load_sort_data()
    menu()

main()
