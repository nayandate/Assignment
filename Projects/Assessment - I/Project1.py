'''
1. Student Admission
   Enter student name
   Roll number
   Class
   Age
2. Fee Management
   Show total fee
   Enter paid fee
   Calculate remaining fee
   Show fee status
3. Attendance
   Enter total working days
   Enter days present
   Calculate attendance percentage
4. Examination
   Enter marks for 5 subjects
   Calculate total
   Percentage
   Grade
   Pass/Fail
5. Library
   Issue a book
   Return a book
   Calculate fine (if late)
6. Report Card
   Display student details
   Show marks
   Percentage
   Grade
   Attendance
   Fee status
7. Exit
'''

print("=================================")
print("     SCHOOL MANAGEMENT SYSTEM    ")
print("=================================")
print("1. Student Admission")
print("2. Fee Management")
print("3. Attendance")
print("4. Examination")
print("5. Library")
print("6. Report Card")
print("7. Exit")

student_name = ""
roll_number = 0
class_name = 0
age = 0

total_fee = 0
remaining_fee = 0
paid_fee = 0

total_working_days = 0
days_present = 0
attendance_percentage = 0

total_marks = 0
percentage = 0
grade = ""
status = ""

today_date = 0
return_date = 0
issue_date = 0
issue_book_name = ""

fine = 0

while True:
   choice = int(input("Enter your choice (1-7): "))
   match choice:
      case 1:
       #Student Admission
        while True:
          student_name = input("Enter student name: ")
          roll_number = int(input("Enter roll number: "))
          class_name = int(input("Enter class (1-12): "))
          if class_name < 1 or class_name > 12:
              print("Class must be from 1 to 12. Please try again.")
              continue
          age = int(input("Enter age: "))
          if student_name != "" and roll_number > 0 and 1 <= class_name <= 12 and age > 0:
              print("Student admission details saved successfully.")
              break
          else:
              print("Enter full details. Please try again.")

      case 2:
       #Fee Management
        while True:
         if student_name == "" or roll_number == 0 or class_name == 0 or age == 0:
             print("Please complete student admission first.")
             break
         else:
            if class_name >= 1 and class_name <= 3:
                print("Class ",class_name," fee is 50000")
                total_fee = 50000
            elif class_name >= 4 and class_name <= 6:
                print("Class ",class_name," fee is 60000")
                total_fee = 60000
            elif class_name >= 7 and class_name <= 10:
                print("Class ",class_name," fee is 80000")
                total_fee = 80000
            elif class_name >= 11 and class_name <= 12:
                print("Class ",class_name," fee is 100000")
                total_fee = 100000

         paid_fee = int(input("Enter paid fee: "))
         if paid_fee >= 0 and paid_fee <= total_fee:
             remaining_fee = total_fee - paid_fee
             print("Remaining fee: ",remaining_fee,"Rs")
             if remaining_fee == 0:
                 print("Fee status: Paid")
             else:
                 print("Fee status: Pending")
             break
         else:
             print("Invalid input. Please try again.")

      case 3:
      #Attendance
        while True:
         if student_name == "" or roll_number == 0 or class_name == 0 or age == 0:
             print("\nPlease complete student admission first.")
             break
         else:
            total_working_days = 289
            print("Total working days: ",total_working_days)
            days_present = int(input("Enter days present: "))
            if days_present >= 0 and days_present <= total_working_days:
                attendance_percentage = (days_present / total_working_days) * 100
                print("Attendance Percentage:", round(attendance_percentage,2), "%")
                break
            else:
                print("Working days must be from 1 to 289. Please try again.")
                
      case 4:
      #Examination
         while True:
            if student_name == "" or roll_number == 0 or class_name == 0 or age == 0:
                print("\nPlease complete student admission first.")
                break
            else:
             while True:
                sanskrit_marks = int(input("Enter marks for Sanskrit: "))
                if sanskrit_marks < 0 or sanskrit_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                hindi_marks = int(input("Enter marks for Hindi: "))
                if hindi_marks < 0 or hindi_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                english_marks = int(input("Enter marks for English: "))
                if english_marks < 0 or english_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                math_marks = int(input("Enter marks for Math: "))
                if math_marks < 0 or math_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                science_marks = int(input("Enter marks for Science: "))
                if science_marks < 0 or science_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                social_studies_marks = int(input("Enter marks for Social Studies: "))
                if social_studies_marks < 0 or social_studies_marks > 100:
                    print("Marks must be from 0 to 100. Please re-enter all marks.")
                    continue

                if (sanskrit_marks <= hindi_marks) and (sanskrit_marks <= english_marks) and (sanskrit_marks <= math_marks) and (sanskrit_marks <= science_marks) and (sanskrit_marks <= social_studies_marks):
                    total_marks = english_marks + math_marks + science_marks + social_studies_marks + hindi_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")

                elif (hindi_marks <= english_marks) and (hindi_marks <= math_marks) and (hindi_marks <= science_marks) and (hindi_marks <= social_studies_marks):
                    total_marks = english_marks + math_marks + science_marks + social_studies_marks + sanskrit_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")

                elif (english_marks <= math_marks) and (english_marks <= science_marks) and (english_marks <= social_studies_marks):
                    total_marks = hindi_marks + math_marks + science_marks + social_studies_marks + sanskrit_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")

                elif ( math_marks <= science_marks) and (math_marks <= social_studies_marks):
                    total_marks = english_marks + hindi_marks + science_marks + social_studies_marks + sanskrit_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")

                elif (science_marks <= social_studies_marks):
                    total_marks = english_marks + math_marks + sanskrit_marks + social_studies_marks + hindi_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")
                else:
                    total_marks = english_marks + math_marks + science_marks + sanskrit_marks + hindi_marks
                    percentage = float(round(total_marks / 500 * 100, 2))
                    print("Total Marks: ",total_marks)
                    print("Percentage: ",percentage,"%")

                if percentage >= 60:
                    grade = "First Division"
                    status = "Pass"
                elif percentage >= 50:
                    grade = "Second Division"
                    status = "Pass"
                elif percentage >= 33:
                    grade = "Third Division"
                    status = "Pass"
                else:
                    grade = "F"
                    status = "Fail"
                
                print("Grade:", grade)
                print("Status:", status)
                break
            break 

      case 5:
      #Library
         while True:
            if student_name == "" or roll_number == 0 or class_name == 0 or age == 0:
                print("\nPlease complete student admission first.")
                break
            else:
             while True:
               print("1. Issue a book")
               print("2. Return a book")
               print("3. Calculate fine (if late)")
               print("4. Back")
               library_choice = int(input("Enter your choice (1-4): "))
               match library_choice:
                  case 1:
                     issue_book_name = input("Enter book name to issue: ")
                     date = int(input("Enter issue date (1-31): "))
                     month = int(input("Enter month (1-12): "))
                     issue_date = (date+month*30)
                     date = int(input("Enter return date (1-31): "))
                     month = int(input("Enter return month (1-12): "))
                     return_date = (date+month*30)
                     if issue_book_name and issue_date != 0 and return_date != 0:
                         print("Book issued successfully.")
 
                  case 2:
                   if issue_book_name == "":
                     print("No book has been issued.")
                   else:
                     return_book_name = input("Enter book name to return: ")
                     if return_book_name == issue_book_name:
                        today_date = int(input("Enter today's date (1-31): "))
                        month = int(input("Enter today's month (1-12): "))
                        today_date = (today_date+month*30)
                        if return_date >= today_date:
                            print("Book returned on time. No fine.")
                            print("Book returned successfully.")
                            issue_book_name = ""
                        else:
                            print("Fine to pay")
                     else:
                         print("Please enter the book name correctly. Try again.")

                  case 3:
                     print("Calculating fine...")
                     if today_date > return_date:
                        fine = (today_date - return_date) * 10
                     else:
                        fine = 0
                     print("Fine amount: $",fine)

                  case 4:
                     break

                  case _:
                     print("Invalid choice. Please try again.")
            break
      case 6:
      #Report Card
         while True:
            if student_name == "" or roll_number == 0 or class_name == 0 or age == 0:
                print("\nPlease complete student admission first.")
                break
            else:
               print("=================================")
               print("\nReport Card")
               print("=================================")
               while True:
                print("1. Student Details")
                print("2. Marks")
                print("3. Percentage")
                print("4. Grade")
                print("5. Attendance")
                print("6. Fee Status")
                print("7. Back")
                report_choice = int(input("Enter your choice (1-7): "))
                match report_choice:
                  case 1:
            
                     print("Student Name: ",student_name)
                     print("Roll Number: ",roll_number)
                     print("Class: ",class_name)
                     print("Age: ",age)
                  case 2:
                     if total_marks == 0:
                         print("Examination not completed.")
                     else:
                         print("Total Marks:", total_marks)
                  case 3:
                        if total_marks == 0:
                            print("Examination not completed.")
                        else:
                            print("Percentage:", percentage, "%")
                  case 4:
                        if total_marks == 0:
                            print("Examination not completed.")
                        else:
                            print("Grade:", grade)
                            print("Status:", status)
                  case 5:
                        if total_working_days == 0:
                            print("Attendance not recorded.")
                        else:
                            print("Total Working Days: ",total_working_days)
                            print("Days Present: ",days_present)
                            print("Attendance:", round(attendance_percentage, 2), "%")
                  case 6:
                        if total_fee == 0:
                           print("Fee details not entered.")
                        elif remaining_fee == 0:
                           print("Fee Status: Paid")
                        else:
                           print("Fee Status: Pending")
                  case 7:
                        break
                  case _:
                        print("Invalid choice. Please try again.")
            break     

      case 7:
         print("Exiting the program. Goodbye!")
         break

      case _:
         print("Invalid choice. Please try again.")