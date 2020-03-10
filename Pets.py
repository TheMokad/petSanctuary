class Pets:
	# Function: Constructor for Pet objects
    # Description: Initializes the attributes of the class
    # Parameters: self, animalID, pet_type, breed, vaccinated, neutered, micro_chip, admission_reason, arrival,
    # 		departure, destination, destination_address
    # Returns: none
    def __init__(self, animalID, pet_type, breed, vaccinated, neutered, micro_chip, admission_reason, arrival,
                 departure, destination, destination_address):
        self.animalID = animalID
        self.pet_type = pet_type
        self.breed = breed
        self.vaccinated = vaccinated
        self.neutered = neutered
        self.micro_chip = micro_chip
        self.admission_reason = admission_reason
        self.arrival = arrival
        self.departure = departure
        self.destination = destination
        self.destination_address = destination_address

		
	# Function: String representation for Pet objects
    # Description: Creates the string representation for pet objects
    # Parameters: self
    # Returns: return_str
    def __str__(self):
        return_str = "Sanctuary Identification: " + self.animalID + "  |  "
        return_str += "Type: " + self.pet_type + "  |  "
        return_str += "Breed: " + self.breed + "  |  "
        return_str += "Vaccinated: " + self.vaccinated + "  |  "
        return_str += "Neutered: " + self.neutered + "  |  "
        return_str += "Microchip Number: " + self.micro_chip + "  |  "
        return_str += "Reason for Admission: " + self.admission_reason + "  |  "
        return_str += "Date of Arrival: " + self.arrival + "  |  "
        return_str += "Date of Departure: " + self.departure + "  |  "
        return_str += "Destination: " + self.destination + "  |  "
        return_str += "Destination Address: " + self.destination_address + "  |  "
        return return_str


    # Function: Comparison/operator function
    # Description: Allows us to compare objects' IDs.
    # Parameters: the object it self, and the inputted object
    # Returns: whether it is smaller or larger than the inputted object
    def __lt__(self, other):
        return self.animalID < other.animalID

    def __gt__(self, other):
        return self.animalID > other.animalID
