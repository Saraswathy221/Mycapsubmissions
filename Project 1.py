##Project 1
#School Administration Program

import csv

def write_into_csv(info_list):
    with open('student_detail.csv','a',newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Name","Age","Contact No.","Email ID"])
            
        writer.writerow(info_list)
        
if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_detail = input("Enter student information for student #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num))
        
        student_detail_list = student_detail.split(' ')
        print("\nThe entered information is =\nName: {}\nAge: {}\nContact_number: {}\nEmail_ID: {}"
                .format(student_detail_list[0], student_detail_list[1], student_detail_list[2], student_detail_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(student_detail_list)

            condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False

        elif choice_check == "no":
            print("\nPlease re-enter the values!")
        

       
