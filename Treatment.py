class Treatments:
	# Function: Constructor for treatment objects
    # Description: Initializes the attributes of the class
    # Parameters: self, animalID, treat_surgery, surgery_date, medication, med_start, med_end, responsible_abuse,
    #            responsible_abandoned
    # Returns: none
    def __init__(self, animalID, treat_surgery, surgery_date, medication, med_start, med_end, responsible_abuse,
                 responsible_abandoned):
        self.animalID = animalID
        self.treat_surgery = treat_surgery
        self.surgery_date = surgery_date
        self.medication = medication
        self.med_start = med_start
        self.med_end = med_end
        self.responsible_abuse = responsible_abuse
        self.responsible_abandoned = responsible_abandoned

		
	# Function: String representation for treatment objects
    # Description: Creates the string representation for treatment objects
    # Parameters: self
    # Returns: return_str
    def __str__(self):
        return_str = "Sanctuary Identification: " + self.animalID + "  |  "
        return_str += "Surgery: " + self.treat_surgery + "  |  "
        return_str += "Surgery date: " + self.surgery_date + "  |  "
        return_str += "Medication: " + self.medication + "  |  "
        return_str += "Medication start: " + self.med_start + "  |  "
        return_str += "Medication end: " + self.med_end + "  |  "
        return_str += "Responsible for abuse: " + self.responsible_abuse + "  |  "
        return_str += "Responsible for abandoned: " + self.responsible_abandoned + "  |  "
        return return_str

    
    # Function: Comparison/operator function
    # Description: Allows us to compare objects' IDs.
    # Parameters: the object it self, and the inputted object
    # Returns: whether it is smaller or larger than the inputted object
    def __lt__(self, other):
        return self.animalID < other.animalID

    def __gt__(self, other):
        return self.animalID > other.animalID