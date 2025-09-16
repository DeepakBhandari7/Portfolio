# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]    
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','headache'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','stomach pain'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','fever')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print("The username and password doesn't match the data registered")

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View/Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6-Get Management Report')
        print(' 7-View all the patients')
        print(' 8-View all the patients from same family')
        print(' 9- Relocate Doctor of patients')
        print(' 10 Quit')
    
        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2':

            # 2- View or discharge patients
            print('Choose the operation:')
            print(' 1- view patients')
            print(' 2- Discharge patients')
            opt = int(input('Option: '))
            if opt == 1:
                admin.view_patient(patients)
            elif opt == 2:
                admin.discharge(patients, discharged_patients)
                
        elif op == '3':
            # 3 - view discharged patients            
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
        elif op =='6':
            # get management report 
            admin.get_management_report(doctors,patients)
            
        elif op == '7':
            # View all the patients
            
            admin.view_patient(patients)
        elif op=='8':
            admin.group_patients(patients)
        elif op=='9':
            admin.relocate_doctor(patients,doctors)
        elif op=='10':
            break
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()