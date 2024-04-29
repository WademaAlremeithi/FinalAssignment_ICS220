#Import required modules to perform the requirements of the code
from enum import Enum
import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
#create Partner class (the super class)
class Partner:
    def __init__(self, name, address, contactDetails ): #Use constructor function with the relevant attributes
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    #Setters and Getters method
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails
    def getContactDetails(self):
        return self.contactDetails
    #override __str__ method to print the details if we print the object of Partner class
    def __str__(self):
        return f"Name: {self.getName()}, Address: {self.getAddress()}, Contact Details:{self.getContactDetails()}"

# Creating Client class to inherit from Partner
class Client(Partner):#This showcases Inhertance relationship
    def __init__(self, name, address, contactDetails, clientID, budget):
        Partner.__init__(self, name, address, contactDetails)
        self.clientID = clientID
        self.budget = budget

    #Setters and Getters of Client attributes
    def setClientID(self, clientID):
        self.clientID = clientID
    def getClientID(self):
        return self.clientID

    def setBudget(self, budget):
        self.budget = budget
    def getBudget(self):
        return self.budget
    #Overrides teh string method to display info of the client object
    def __str__(self):
        return Partner.__str__(self) + f"Client ID: {self.getClientID()},Budget: {self.getBudget()}"
#Create Guest class to inherit from Partner
class Guest(Partner):
    def __init__(self, name, address, contactDetails, guestID):
        Partner.__init__(self, name, address, contactDetails) #Calls the parent class constructor
        self.guestID = guestID
    #Setter and getter for Guest attributes
    def setGuestID(self, guestID):
        self.guestID = guestID
    def getGuestID(self):
        return self.guestID

    def __str__(self):
        return Partner.__str__(self) + f", Guest ID: {self.getGuestID()}"
#Create Caterer class to inherit from Partner class
class Caterer(Partner):
    def __init__(self, catererID, name, address, contactDetails, menu, minGuest, maxGuest):
        # Call the superclass/parent constructor and its attributes
        Partner.__init__(self, name, address, contactDetails)
        self.catererID = catererID
        self.menu = menu
        self.minGuest = minGuest
        self.maxGuest = maxGuest
    #Setters and Getters of Caterer class
    def setCatererID(self, catererID):
        self.catererID = catererID
    def getCatererID(self):
        return self.catererID

    def setMenu(self, menu):
        self.menu = menu
    def getMenu(self):
        return self.menu

    def setMinGuest(self, minGuest):
        self.minGuest = minGuest
    def getMinGuest(self):
        return self.minGuest

    def setMaxGuest(self, maxGuest):
        self.maxGuest = maxGuest
    def getMaxGuest(self):
        return self.maxGuest

    def __str__(self):
        # call the parent class __str__ function to display all the information
        return Partner.__str__(self) + f", Caterer ID: {self.getCatererID()}, Menu: {self.getMenu()}, Minimum Number of Guests: {self.getMinGuest()}, Maximum Number of Guests: {self.getMaxGuest()}"
#Create Venue class to inherit from Partner
class Venue(Partner):
    def __init__(self, name, address, contactDetails,venueID, minGuest, maxGuest):
        # Call the superclass constructor
        Partner.__init__(self, name, address, contactDetails)
        self.venueID = venueID
        self.minGuest = minGuest
        self.maxGuest = maxGuest
    #Setters and Getters for venue attributes
    def setVenueID(self, venueID):
        self.venueID = venueID
    def getVenueID(self):
        return self.venueID

    def setMinGuest(self, minGuest):
        self.minGuest = minGuest
    def getMinGuest(self):
        return self.minGuest

    def setMaxGuest(self, maxGuest):
        self.maxGuest = maxGuest
    def getMaxGuest(self):
        return self.maxGuest

    def __str__(self):
        # Include the superclass __str__ representation
        return Partner.__str__(self) + f", Venue ID: {self.getVenueID()}, Minimum Guests: {self.getMinGuest()}, Maximum Guests: {self.getMaxGuest()}"

#Enum class for event type options
class EventType(Enum):
    Weddings = "Weddings"
    Birthdays = "Birthdays"
    ThemedParties = "Themed Parties"
    Graduations = "Graduations"
#creating Event class with the specfied attributes
class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venue, client, guestList, catering, cleaning, decorating, entertainment, furnitureSupp, invoice):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue #This stores the information from Venue Class which shows aggregation relationship
        self.client = client #This represents the aggregation relationship with Client class
        self.guestList = guestList
        self.catering = catering #This represents the aggregation relationship with Caterer class
        self.cleaning = cleaning
        self.decorating = decorating
        self.entertainment = entertainment
        self.furnitureSupp = furnitureSupp
        self.invoice = invoice
    #setters and getters for all the attributes
    def setEventID(self, eventID):
        self.eventID = eventID
    def getEventID(self):
        return self.eventID

    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type

    def setTheme(self, theme):
        self.theme = theme
    def getTheme(self):
        return self.theme

    def setDate(self, date):
        self.date = date
    def getDate(self):
        return self.date

    def setTime(self, time):
        self.time = time
    def getTime(self):
        return self.time

    def setDuration(self, duration):
        self.duration = duration
    def getDuration(self):
        return self.duration

    def getVenue(self):
        return self.venue

    def getClient(self):
        return self.client

    def setGuestList(self, guestList):
        self.guestList = guestList
    def getGuestList(self):
        for i in self.guestList:
            return i
        return

    def setCatering(self, catering):
        self.catering = catering
    def getCatering(self):
        return self.catering

    def setCleaning(self, cleaning):
        self.cleaning = cleaning
    def getCleaning(self):
        return self.cleaning

    def setDecorating(self, decorating):
        self.decorating = decorating
    def getDecorating(self):
        return self.decorating

    def setEntertainment(self, entertainment):
        self.entertainment = entertainment
    def getEntertainment(self):
        return self.entertainment

    def setFurnitureSupp(self, furnitureSupp):
        self.furnitureSupp = furnitureSupp
    def getFurnitureSupp(self):
        return self.furnitureSupp

    def setInvoice(self, invoice):
        self.invoice = invoice
    def getInvoice(self):
        return self.invoice

    #Create a function to add guest to the list
    #This is used to create objects of the guest class rather than using the class directly
    #Represnts the composition relationship
    def addGuest(self, name, address, contactDetails, guestID):
        guest = Guest(name, address, contactDetails, guestID)
        self.guestList.append(guest)
        print("Guest Added Successfully!")

    #override str method to display the infromation of the object of Event class
    def __str__(self):
        return f"Event ID: {self.getEventID()}, Type: {self.getType()}, Theme: {self.getTheme()}, Date: {self.getDate()}, Time: {self.getTime()}, Duration: {self.getDuration()}, Venue : {self.getVenue()}, Client : {self.getClient()}, Guest List: {self.getGuestList()}, Catering: {self.getCatering()}, Cleaning: {self.getCleaning()}, Decorating: {self.getDecorating()}, Entertainment: {self.getEntertainment()}, Furniture Supply: {self.getFurnitureSupp()}, Invoice: {self.getInvoice()}"

#Enum classs foe Employee Type
class EmployeeType(Enum):
    salesManager = "Sales Manager"
    salesPerson = "Salesperson"
    marketingManager = "Marketing Manager"
    marketer = "Marketer"
    accountant = "Accountant"
    designer = "Designer"
    handyman = "Handyman"

#Creating Employee Class
class Employee:
    def __init__(self, name, employeeID, employeeType, department, jobTitle, basicSalary, age, dateOfBirth, passport, managerID):
        self.name = name
        self.employeeID = employeeID
        self.employeeType = employeeType
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passport = passport
        self.managerID = managerID

    #setters and getters for all attributes of the class
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID
    def getEmployeeID(self):
        return self.employeeID

    def setEmployeeType(self, employeeType):
        self.employeeType = employeeType
    def getEmployeeType(self):
        return self.employeeType

    def setDepartment(self, department):
        self.department = department
    def getDepartment(self):
        return self.department

    def setJobTitle(self, jobTitle):
        self.jobTitle = jobTitle
    def getJobTitle(self):
        return self.jobTitle

    def setBasicSalary(self, basicSalary):
        self.basicSalary = basicSalary
    def getBasicSalary(self):
        return self.basicSalary

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def getDateOfBirth(self):
        return self.dateOfBirth

    def setPassport(self, passport):
        self.passport = passport
    def getPassport(self):
        return self.passport

    def setManagerID(self, managerID):
        self.managerID = managerID
    def getManagerID(self):
        return self.managerID
    #Overriding __str__ method to display the information of the objects of the class when needed
    def __str__(self):
        return f"Name: {self.getName()}, Employee ID: {self.getEmployeeID()}, Employee Type: {self.getEmployeeType()}, Department: {self.getDepartment()}, Job Title: {self.getJobTitle()}, Basic Salary: {self.getBasicSalary()}, Age: {self.getAge()}, Date of Birth: {self.getDateOfBirth()}, Passport: {self.getPassport()}, Manager ID: {self.getManagerID()}"


class EventManagementForm:
    """class to represent a GUI form to manage events and requirements"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Event Management Form")
        #to make it easier to use we have root window with buttons to add for each class
        self.add_client_button = tk.Button(self.root, text="Add Client", command=self.addClient)#Add button for Client Class
        self.add_client_button.pack()
        self.add_event_button = tk.Button(self.root, text="Add Event", command=self.addEvent)#Add button for Event Class
        self.add_event_button.pack()
        self.add_employee_button = tk.Button(self.root, text="Add Employee", command= self.addEmployee)#Button to add employee
        self.add_employee_button.pack()
        self.add_guest_button = tk.Button(self.root, text= "Add Guest", command=self.addGuest)#Add Guest button
        self.add_guest_button.pack()
        self.add_caterer_button = tk.Button(self.root, text="Add Caterer", command=self.addCaterer)#Add caterer button
        self.add_caterer_button.pack()
        self.add_venue_button = tk.Button(self.root, text="Add Venue", command=self.addVenue)#Add venue button
        self.add_venue_button.pack()


    def addEvent(self):#The function used as command for add event button
        event_window = tk.Toplevel(self.root) #used for a new event window
        event_window.title("Add Event") #creates the title of the window
        event_window.geometry("600x600") #specifies size
        #create label and entry box for the attributes of Event class
        self.event_id_label = tk.Label(event_window, text="Event ID:")
        self.event_id_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.event_id_entry = tk.Entry(event_window)
        self.event_id_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.type_label = tk.Label(event_window, text="Type:")
        self.type_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.type_entry = tk.Entry(event_window)
        self.type_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.theme_label = tk.Label(event_window, text="Theme:")
        self.theme_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.theme_entry = tk.Entry(event_window)
        self.theme_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.date_label = tk.Label(event_window, text="Date:")
        self.date_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.date_entry = tk.Entry(event_window)
        self.date_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.time_label = tk.Label(event_window, text="Time:")
        self.time_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.time_entry = tk.Entry(event_window)
        self.time_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.duration_label = tk.Label(event_window, text="Duratiom:")
        self.duration_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.duration_entry = tk.Entry(event_window)
        self.duration_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.venue_label = tk.Label(event_window, text="Venue:")
        self.venue_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.venue_entry = tk.Entry(event_window)
        self.venue_entry.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        self.client_label = tk.Label(event_window, text="Client:")
        self.client_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.client_entry = tk.Entry(event_window)
        self.client_entry.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

        self.guestlist_label = tk.Label(event_window, text="Guest List:")
        self.guestlist_label.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
        self.guestlist_entry = tk.Entry(event_window)
        self.guestlist_entry.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        self.catering_label = tk.Label(event_window, text="Catering Company:")
        self.catering_label.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
        self.catering_entry = tk.Entry(event_window)
        self.catering_entry.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

        self.cleaning_label = tk.Label(event_window, text="Cleaning Company:")
        self.cleaning_label.grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)
        self.cleaning_entry = tk.Entry(event_window)
        self.cleaning_entry.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)

        self.decorating_label = tk.Label(event_window, text="Decorating Company:")
        self.decorating_label.grid(column=0, row=11, sticky=tk.W, padx=5, pady=5)
        self.decorating_entry = tk.Entry(event_window)
        self.decorating_entry.grid(column=1, row=11, sticky=tk.W, padx=5, pady=5)

        self.entertainment_label = tk.Label(event_window, text="Entertainment Company:")
        self.entertainment_label.grid(column=0, row=12, sticky=tk.W, padx=5, pady=5)
        self.entertainment_entry = tk.Entry(event_window)
        self.entertainment_entry.grid(column=1, row=12, sticky=tk.W, padx=5, pady=5)

        self.furnitureSupp_label = tk.Label(event_window, text="Furniture Supplier:")
        self.furnitureSupp_label.grid(column=0, row=13, sticky=tk.W, padx=5, pady=5)
        self.furnitureSupp_entry = tk.Entry(event_window)
        self.furnitureSupp_entry.grid(column=1, row=13, sticky=tk.W, padx=5, pady=5)

        self.invoice_label = tk.Label(event_window, text="Invoice:")
        self.invoice_label.grid(column=0, row=14, sticky=tk.W, padx=5, pady=5)
        self.invoice_entry = tk.Entry(event_window)
        self.invoice_entry.grid(column=1, row=14, sticky=tk.W, padx=5, pady=5)

        #create a submit event and clear event buttons
        self.submit_event_button = tk.Button(event_window, text="Submit", command=self.submit_event)#refers to submit_event function
        self.submit_event_button.grid(column=1, row=15, sticky=tk.E, padx=5, pady=5)

        self.clear_event_button = tk.Button(event_window,text= "Clear Event", command = self.clear_event_boxes)#refers to clear_event_boxes function
        self.clear_event_button.grid(column=1, row=16, sticky=tk.E, padx=5, pady=5)

    def addClient(self):#The function used as command for add client button
        client_window = tk.Toplevel(self.root)#used for a new client window
        client_window.title("Add Client")#creates the title of the window
        client_window.geometry("600x600")
        #create a title place at the first row
        self.client_label = tk.Label(client_window, text="Add Client Information:")
        self.client_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # create label and entry box for the attributes of Client class
        self.client_name_label = tk.Label(client_window, text="Client Name:")
        self.client_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.client_name_entry = tk.Entry(client_window)
        self.client_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.client_address_label = tk.Label(client_window, text="Client Address:")
        self.client_address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.client_address_entry = tk.Entry(client_window)
        self.client_address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.client_contactDetails_label = tk.Label(client_window, text="Client Contact Details:")
        self.client_contactDetails_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.client_contactDetails_entry = tk.Entry(client_window)
        self.client_contactDetails_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.client_clientID_label = tk.Label(client_window, text="Client ID:")
        self.client_clientID_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.client_clientID_entry = tk.Entry(client_window)
        self.client_clientID_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.client_budget_label = tk.Label(client_window, text="Client Budget:")
        self.client_budget_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.client_budget_entry = tk.Entry(client_window)
        self.client_budget_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        # create a submit client and clear client buttons
        self.submit_client_button = tk.Button(client_window, text="Submit Client", command=self.submit_client)
        self.submit_client_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

        self.clear_client_button = tk.Button(client_window, text="Clear Client", command=self.clear_client_boxes)
        self.clear_client_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

    def addEmployee(self):#The function used as command for add employee button
        employee_window = tk.Toplevel(self.root)#used for a new employee window
        employee_window.title("Add Employee")#creates the title of the window
        employee_window.geometry("600x600")#specifies size
        # create a title label widget placed at the first row
        self.employee_label = tk.Label(employee_window, text="Add Employee Information:")
        self.employee_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # create label and entry box for the attributes of Employee class
        self.employee_name_label = tk.Label(employee_window, text="Employee Name:")
        self.employee_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.employee_name_entry = tk.Entry(employee_window)
        self.employee_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.employee_employeeID_label = tk.Label(employee_window, text="Employee ID:")
        self.employee_employeeID_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.employee_employeeID_entry = tk.Entry(employee_window)
        self.employee_employeeID_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.employee_employeeType_label = tk.Label(employee_window, text="Employee Type:")
        self.employee_employeeType_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.employee_employeeType_entry = tk.Entry(employee_window)
        self.employee_employeeType_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.employee_department_label = tk.Label(employee_window, text="Employee Department:")
        self.employee_department_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.employee_department_entry = tk.Entry(employee_window)
        self.employee_department_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.employee_jobTitle_label = tk.Label(employee_window, text="Employee Job Title:")
        self.employee_jobTitle_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.employee_jobTitle_entry = tk.Entry(employee_window)
        self.employee_jobTitle_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.employee_basicSalary_label = tk.Label(employee_window, text="Employee Basic Salary:")
        self.employee_basicSalary_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.employee_basicSalary_entry = tk.Entry(employee_window)
        self.employee_basicSalary_entry.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

        self.employee_age_label = tk.Label(employee_window, text="Employee Age:")
        self.employee_age_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.employee_age_entry = tk.Entry(employee_window)
        self.employee_age_entry.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

        self.employee_dateOfBirth_label = tk.Label(employee_window, text="Employee Date of Birth:")
        self.employee_dateOfBirth_label.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
        self.employee_dateOfBirth_entry = tk.Entry(employee_window)
        self.employee_dateOfBirth_entry.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

        self.employee_passport_label = tk.Label(employee_window, text="Employee Passport Details:")
        self.employee_passport_label.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
        self.employee_passport_entry = tk.Entry(employee_window)
        self.employee_passport_entry.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)

        self.employee_managerID_label = tk.Label(employee_window, text="Employee Basic Salary:")
        self.employee_managerID_label.grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)
        self.employee_managerID_entry = tk.Entry(employee_window)
        self.employee_managerID_entry.grid(column=1, row=10, sticky=tk.E, padx=5, pady=5)
        # create a submit employee and clear employee buttons
        self.submit_employee_button = tk.Button(employee_window, text="Submit Employee", command=self.submit_employee)
        self.submit_employee_button.grid(column=1, row=11, sticky=tk.E, padx=5, pady=5)

        self.clear_employee_button = tk.Button(employee_window, text="Clear Employee", command=self.clear_employee_boxes)
        self.clear_employee_button.grid(column=1, row=12, sticky=tk.E, padx=5, pady=5)

    def addGuest(self):#The function used as command for add guest button
        guest_window = tk.Toplevel(self.root)#used for a new guest window
        guest_window.title("Add Guest")
        guest_window.geometry("600x600")
        # create a title label widget at the first row
        self.guest_label = tk.Label(guest_window, text="Add Guest Information:")
        self.guest_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # create label and entry box for the attributes of Guest class
        self.guest_name_label = tk.Label(guest_window, text="Guest Name:")
        self.guest_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.guest_name_entry = tk.Entry(guest_window)
        self.guest_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.guest_address_label = tk.Label(guest_window, text="Guest Address:")
        self.guest_address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.guest_address_entry = tk.Entry(guest_window)
        self.guest_address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.guest_contactDetails_label = tk.Label(guest_window, text="Guest Contact Details:")
        self.guest_contactDetails_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.guest_contactDetails_entry = tk.Entry(guest_window)
        self.guest_contactDetails_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.guest_guestID_label = tk.Label(guest_window, text="Guest ID:")
        self.guest_guestID_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.guest_guestID_entry = tk.Entry(guest_window)
        self.guest_guestID_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        # create a submit event and clear guest buttons
        self.submit_guest_button = tk.Button(guest_window, text="Submit Guest", command=self.submit_guest)
        self.submit_guest_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.clear_guest_button = tk.Button(guest_window, text="Clear Guest", command=self.clear_guest_boxes)
        self.clear_guest_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

    def addCaterer(self):#The function used as command for add caterer button
        caterer_window = tk.Toplevel(self.root)
        caterer_window.title("Add Caterer")
        caterer_window.geometry("600x600")

        self.caterer_label = tk.Label(caterer_window, text="Add Caterer Information:")
        self.caterer_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.caterer_name_label = tk.Label(caterer_window, text="Caterer Name:")
        self.caterer_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.caterer_name_entry = tk.Entry(caterer_window)
        self.caterer_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.caterer_address_label = tk.Label(caterer_window, text="Caterer Address:")
        self.caterer_address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.caterer_address_entry = tk.Entry(caterer_window)
        self.caterer_address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.caterer_contactDetails_label = tk.Label(caterer_window, text="Caterer Contact Details:")
        self.caterer_contactDetails_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.caterer_contactDetails_entry = tk.Entry(caterer_window)
        self.caterer_contactDetails_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.caterer_catererID_label = tk.Label(caterer_window, text="Caterer ID:")
        self.caterer_catererID_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.caterer_catererID_entry = tk.Entry(caterer_window)
        self.caterer_catererID_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.caterer_menu_label = tk.Label(caterer_window, text="Caterer Menu :")
        self.caterer_menu_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.caterer_menu_entry = tk.Entry(caterer_window)
        self.caterer_menu_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.caterer_minGuest_label = tk.Label(caterer_window, text="Caterer Min. Guests :")
        self.caterer_minGuest_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.caterer_minGuest_entry = tk.Entry(caterer_window)
        self.caterer_minGuest_entry.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

        self.caterer_maxGuest_label = tk.Label(caterer_window, text="Caterer Max. Guests :")
        self.caterer_maxGuest_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.caterer_maxGuest_entry = tk.Entry(caterer_window)
        self.caterer_maxGuest_entry.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

        self.submit_caterer_button = tk.Button(caterer_window, text="Submit Caterer", command=self.submit_caterer)
        self.submit_caterer_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

        self.clear_caterer_button = tk.Button(caterer_window, text="Clear Caterer", command=self.clear_caterer_boxes)
        self.clear_caterer_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
    def addVenue(self):#The function used as command for add venue button
        venue_window = tk.Toplevel(self.root)
        venue_window.title("Add Venue")
        venue_window.geometry("600x600")

        self.venue_label = tk.Label(venue_window, text="Add Venue Information:")
        self.venue_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.venue_name_label = tk.Label(venue_window, text="Venue Name:")
        self.venue_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.venue_name_entry = tk.Entry(venue_window)
        self.venue_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.venue_address_label = tk.Label(venue_window, text="Venue Address:")
        self.venue_address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.venue_address_entry = tk.Entry(venue_window)
        self.venue_address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.venue_contactDetails_label = tk.Label(venue_window, text="Venue Contact Details:")
        self.venue_contactDetails_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.venue_contactDetails_entry = tk.Entry(venue_window)
        self.venue_contactDetails_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.venue_venueID_label = tk.Label(venue_window, text="Venue ID:")
        self.venue_venueID_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.venue_venueID_entry = tk.Entry(venue_window)
        self.venue_venueID_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.venue_minGuest_label = tk.Label(venue_window, text="Venue Min. Guests :")
        self.venue_minGuest_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.venue_minGuest_entry = tk.Entry(venue_window)
        self.venue_minGuest_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.venue_maxGuest_label = tk.Label(venue_window, text="Venue Max. Guests :")
        self.venue_maxGuest_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.venue_maxGuest_entry = tk.Entry(venue_window)
        self.venue_maxGuest_entry.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

        self.submit_venue_button = tk.Button(venue_window, text="Submit Venue", command=self.submit_venue)
        self.submit_venue_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

        self.clear_venue_button = tk.Button(venue_window, text="Clear Venue", command=self.clear_venue_boxes)
        self.clear_venue_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

    def submit_event(self):#function used for submit event button
        eventID = self.event_id_entry.get()
        type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue = self.venue_entry.get()
        client = self.client_entry.get()
        guestList = self.guestlist_entry.get()
        catering = self.catering_entry.get()
        cleaning = self.cleaning_entry.get()
        decorating = self.decorating_entry.get()
        entertainment = self.entertainment_entry.get()
        furnitureSupp = self.furnitureSupp_entry.get()
        invoice = self.invoice_entry.get()
        #creates event object of class Event
        event = Event(eventID, type, theme, date, time, duration, venue, client, guestList, catering, cleaning, decorating, entertainment, furnitureSupp, invoice)
        self.data_layer.add_event(event)
        tk.messagebox.showinfo("Success", "Event added successfully.")
        self.clear_event_boxes()#clears the entry boxes after adding the event

    def clear_event_boxes(self):
        # Clear the Entry Boxes
        self.event_id_entry.delete(0, tk.END)#from the start to the end of the text
        self.type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.venue_entry.delete(0, tk.END)
        self.client_entry.delete(0, tk.END)
        self.guestlist_entry.delete(0, tk.END)
        self.catering_entry.delete(0, tk.END)
        self.cleaning_entry.delete(0, tk.END)
        self.entertainment_entry.delete(0, tk.END)
        self.furnitureSupp_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)


    def submit_client(self):#function used for submit client button
        name = self.client_name_entry.get()
        address = self.client_address_entry.get()
        contactDetails = self.client_contactDetails_entry.get()
        clientID = self.client_clientID_entry.get()
        budget = self.client_budget_entry.get()

        client = Client(name, address, contactDetails, clientID, budget)#Creates a client object
        self.data_layer.add_client(client)
        tk.messagebox.showinfo("Success", "Client added successfully.")#shows message to indicate success
        self.clear_client_boxes()

    def clear_client_boxes(self):
        # Clear the client Boxes
        self.client_name_entry.delete(0, tk.END)
        self.client_address_entry.delete(0, tk.END)
        self.client_contactDetails_entry.delete(0, tk.END)
        self.client_clientID_entry.delete(0, tk.END)
        self.client_budget_entry.delete(0, tk.END)


    def submit_employee(self):#function used for submit employee button
        name = self.employee_name_entry.get()
        employeeID = self.employee_employeeID_entry.get()
        employeeType = self.employee_employeeType_entry.get()
        department = self.employee_department_entry.get()
        jobTitle = self.employee_jobTitle_entry.get()
        basicSalary = self.employee_basicSalary_entry.get()
        age = self.employee_age_entry.get()
        dateOfBirth = self.employee_dateOfBirth_entry.get()
        passport = self.employee_passport_entry.get()
        managerID = self.employee_managerID_entry.get()

        employee = Employee(name, employeeID, employeeType, department, jobTitle, basicSalary, age, dateOfBirth, passport, managerID)
        self.data_layer.add_employee(employee)
        tk.messagebox.showinfo("Success", "Employee added successfully.")
        self.clear_employee_boxes()

    def clear_employee_boxes(self):
        # Clear the employee Boxes
        self.employee_name_entry.delete(0, tk.END)
        self.employee_employeeID_entry.delete(0, tk.END)
        self.employee_employeeType_entry.delete(0, tk.END)
        self.employee_department_entry.delete(0, tk.END)
        self.employee_jobTitle_entry.delete(0, tk.END)
        self.employee_basicSalary_entry.delete(0, tk.END)
        self.employee_age_entry.delete(0, tk.END)
        self.employee_dateOfBirth_entry.delete(0, tk.END)
        self.employee_passport_entry.delete(0, tk.END)
        self.employee_managerID_entry.delete(0, tk.END)

    def submit_guest(self):#function used for submit guest button
        name = self.client_name_entry.get()
        address = self.client_address_entry.get()
        contactDetails = self.client_contactDetails_entry.get()
        guestID = self.client_clientID_entry.get()

        #cretes guest object
        guest = Guest(name, address, contactDetails, guestID)
        self.data_layer.add_guest(guest)
        tk.messagebox.showinfo("Success", "Guest added successfully.")
        self.clear_guest_boxes()

    def clear_guest_boxes(self):
        # Clear the guest Boxes
        self.guest_name_entry.delete(0, tk.END)
        self.guest_address_entry.delete(0, tk.END)
        self.guest_contactDetails_entry.delete(0, tk.END)
        self.guest_guestID_entry.delete(0, tk.END)

    def submit_caterer(self):#function used for submit caterer button
        name = self.caterer_name_entry.get()
        address = self.caterer_address_entry.get()
        contactDetails = self.caterer_contactDetails_entry.get()
        catererID = self.caterer_catererID_entry.get()
        menu = self.caterer_menu_entry.get()
        minGuest = self.caterer_minGuest_entry.get()
        maxGuest = self.caterer_maxGuest_entry.get()
        #create caterer object
        caterer = Caterer(name, address, contactDetails, catererID, menu, minGuest, maxGuest)
        self.data_layer.add_caterer(caterer)
        tk.messagebox.showinfo("Success", "Caterer added successfully.")
        self.clear_caterer_boxes()

    def clear_caterer_boxes(self):
        # Clear the caterer Boxes
        self.caterer_name_entry.delete(0, tk.END)
        self.caterer_address_entry.delete(0, tk.END)
        self.caterer_contactDetails_entry.delete(0, tk.END)
        self.caterer_catererID_entry.delete(0, tk.END)
        self.caterer_minGuest_entry.delete(0, tk.END)
        self.caterer_maxGuest_entry.delete(0, tk.END)

    def submit_venue(self):#function used for submit venue button
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contactDetails = self.venue_contactDetails_entry.get()
        venueID = self.venue_venueID_entry.get()
        minGuest = self.venue_minGuest_entry.get()
        maxGuest = self.venue_maxGuest_entry.get()
        #create venue object
        venue = Venue(name, address, contactDetails, venueID, minGuest, maxGuest)
        self.data_layer.add_venue(venue)
        tk.messagebox.showinfo("Success", "Venue added successfully.")
        self.clear_venue_boxes()

    def clear_venue_boxes(self):
        # Clear the venue Boxes
        self.venue_name_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.venue_contactDetails_entry.delete(0, tk.END)
        self.venue_venueID_entry.delete(0, tk.END)
        self.venue_minGuest_entry.delete(0, tk.END)
        self.venue_maxGuest_entry.delete(0, tk.END)




class ListEventForm:
    """Class to represent a GUI form to display all events"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('1000x800')
        self.root.title("Event Details")

        self.table = ttk.Treeview(self.root, columns=('Event ID', 'Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue', 'Client', 'Guest List', 'Catering', 'Cleaning', 'Decorating', 'Entertainment', 'Furniture Supplier', 'Invoice'), show='headings')
        #creat headings for teh attributes
        self.table.heading('Event ID', text='Event ID')
        self.table.heading('Type', text='Type')
        self.table.heading('Theme', text='Theme')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Duration', text='Duration')
        self.table.heading('Venue', text='Venue')
        self.table.heading('Client', text='Client')
        self.table.heading('Guest List', text='Guest List')
        self.table.heading('Catering', text='Catering')
        self.table.heading('Cleaning', text='Cleaning')
        self.table.heading('Decorating', text='Decorating')
        self.table.heading('Entertainment', text='Entertainment')
        self.table.heading('Furniture Supplier', text='Furniture Supplier')
        self.table.heading('Invoice', text='Invoice')
        self.table.pack(padx =5,pady=5)

        all_events = self.data_layer.get_all_events()
        for event in all_events:
            self.table.insert('', 'end', values=(event.eventID, event.getType, event.theme, event.date, event.time, event.duration, event.venue, event.client, event.guestList, event.catering, event.cleaning, event.decorating, event.entertainment, event.furnitureSupp, event.invoice))

        self.root.mainloop()

class ListClientForm:
    """Class to represent a GUI form to display all clients"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.title("Client Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Contact Details', 'Client ID', 'Budget'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text= 'Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.heading('Client ID', text='Client ID')
        self.table.heading('Budget', text='Budget')
        self.table.pack(pady=20)

        all_clients = self.data_layer.get_all_clients()
        for client in all_clients:
            self.table.insert('', 'end', values=(client.name, client.address, client.contactDetails, client.clientID, client.budget))

        self.root.mainloop()

class ListEmployeeForm:
    """Class to represent a GUI form to display all the employees"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.title("Employee Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'Employee ID', 'Employee Type', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date Of Birth', 'Passport', 'Manager ID'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Employee ID', text= 'Employee ID')
        self.table.heading('Employee Type', text='Employee Type')
        self.table.heading('Department', text='Department')
        self.table.heading('Job Title', text='Job Title')
        self.table.heading('Basic Salary', text='Basic Salary')
        self.table.heading('Age', text='Age')
        self.table.heading('Date Of Birth', text='Date Of Birth')
        self.table.heading('Passport', text='Passport')
        self.table.heading('Manager ID', text='Manager ID')
        self.table.pack(pady=20)

        all_employees = self.data_layer.get_all_employees()
        for employee in all_employees:
            self.table.insert('', 'end', values=(employee.name, employee.employeeID, employee.employeeType, employee.department, employee.jobTitle, employee.basicSalary, employee.age, employee.dateOfBirth, employee.passport, employee.managerID))

        self.root.mainloop()

class ListGuestForm:
    """Class to represent a GUI form to display all clients"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.title("Guest Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Contact Details', 'Guest ID'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text= 'Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.heading('Guest ID', text='Client ID')
        self.table.pack(pady=20)

        all_guests = self.data_layer.get_all_guests()
        for guest in all_guests:
            self.table.insert('', 'end', values=(guest.name, guest.address, guest.contactDetails, guest.guestID))

        self.root.mainloop()

class ListCatererForm:
    """Class to represent a GUI form to display all caterer"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.title("Caterer Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Contact Details', 'Caterer ID', 'Menu', 'Min Guests', 'Max Guests'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text= 'Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.heading('Caterer ID', text='Caterer ID')
        self.table.heading('Menu', text='Menu')
        self.table.heading('Min Guests', text='MIn Guest')
        self.table.heading('Max Guests', text='Max Guests')
        self.table.pack(pady=20)

        all_caterers = self.data_layer.get_all_caterers()
        for caterer in all_caterers:
            self.table.insert('', 'end', values=(caterer.name, caterer.address, caterer.contactDetails, caterer.catererID, caterer.menu, caterer.minGuest, caterer.maxGuest))

        self.root.mainloop()

class ListVenueForm:
    """Class to represent a GUI form to display all veneues"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x800')
        self.root.title("Venue Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Contact Details', 'Venue ID', 'Min Guests', 'Max Guests'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text= 'Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.heading('Venue ID', text='Venue ID')
        self.table.heading('Min Guests', text='MIn Guest')
        self.table.heading('Max Guests', text='Max Guests')
        self.table.pack(pady=20)

        all_venues = self.data_layer.get_all_venues()
        for venue in all_venues:
            self.table.insert('', 'end', values=(venue.name, venue.address, venue.contactDetails, venue.venueID, venue.minGuest, venue.maxGuest))

        self.root.mainloop()

class DataLayer:
    """Class to handle read and write operations for event data"""

    def __init__(self, filename):
        self.filename = filename

    def add_event(self, event):
        all_events = self.get_all_events()
        all_events.append(event)
        self.write_events_to_file(all_events)
    def add_client(self, client):
        all_clients = self.get_all_clients
        all_clients.append(client)
        self.write_clients_to_file(all_clients)

    def add_employee(self, employee):
        all_employees = self.get_all_employees()
        all_employees.append(employee)
        self.write_employees_to_file(all_employees)

    def add_guest(self, guest):
        all_guests = self.get_all_guests()
        all_guests.append(guest)
        self.write_guests_to_file(all_guests)

    def add_caterer(self, caterer):
        all_caterers = self.get_all_caterers()
        all_caterers.append(caterer)
        self.write_caterers_to_file(all_caterers)

    def add_venue(self, venue):
        all_venues = self.get_all_venues()
        all_venues.append(venue)
        self.write_venues_to_file(all_venues)
    #functions to read from files using pickle load in 'rb' to indicate binary reading
    def get_all_events(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_events = pickle.load(file)
            return all_events
    def get_all_clients(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_clients = pickle.load(file)
                return all_clients

    def get_all_employees(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_employees = pickle.load(file)
            return all_employees

    def get_all_guests(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_guests = pickle.load(file)
            return all_guests

    def get_all_caterers(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_caterers = pickle.load(file)
            return all_caterers

    def get_all_venues(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, 'rb') as file:
                all_venues = pickle.load(file)
            return all_venues
    #seperate functions to write the objects to a file
    def write_events_to_file(self, all_events):
        with open(self.filename, 'wb') as f:#'wb' to indicate binary writing
            pickle.dump(all_events, f)#uses pickle dump method

    def write_clients_to_file(self, all_clients):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_clients, f)

    def write_employees_to_file(self, all_employees):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_employees, f)

    def write_guests_to_file(self, all_guests):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_guests, f)

    def write_caterers_to_file(self, all_caterers):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_caterers, f)

    def write_venues_to_file(self, all_venues):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_venues, f)

filename = "events.pkl"
data_layer = DataLayer(filename)
event_form = EventManagementForm(data_layer)
list_event_form = ListEventForm(data_layer)

filename = "clients.pkl"
data_layer = DataLayer(filename)
client_form = EventManagementForm(data_layer)
list_client_form = ListClientForm(data_layer)

filename = "employees.pkl"
data_layer = DataLayer(filename)
employee_form = EventManagementForm(data_layer)
list_employee_form = ListEmployeeForm(data_layer)

filename = "guests.pkl"
data_layer = DataLayer(filename)
guest_form = EventManagementForm(data_layer)
list_guest_form = ListGuestForm(data_layer)

filename = "caterers.pkl"
data_layer = DataLayer(filename)
caterer_form = EventManagementForm(data_layer)
list_caterer_form = ListCatererForm(data_layer)

filename = "venues.pkl"
data_layer = DataLayer(filename)
venue_form = EventManagementForm(data_layer)
list_venue_form = ListVenueForm(data_layer)

#Test Cases
#Create objects
client = Client("Mohamed", "AL Salam st", "0501234567", "A15978", 800)
guest = Guest("Wadema", "Sheikh Zayed st", "202203112@zu.ac.ae", "G012")
caterer = Caterer("C0182", "Food & Co", "Dubai", "foodandco@company.com", ["Egg", "Greek Salad", "Steack", "Cupcake"], 10, 250)
venue = Venue("Hills venue", "Abu Dhabi", "hillsweddingshall@company.com", "V0120", 50, 300)
event = Event("123", EventType.Weddings, "theme", "10/15/24", 12.30, 60, venue, client, [], caterer, "Cleaning Company #3", "Deco Max", "Entertainmnet by ten", "PAN Emirates", 1200  )
event.addGuest("Mohamed", "Abu Dhabi", "050159753", "G01")
event.addGuest("Maryam", "Dubai", "0502588521", "G45")
print(event)
