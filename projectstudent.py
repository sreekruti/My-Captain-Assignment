import csv
def write_into_csv(info_list):
  with open('student_info.csv', 'a' , newline='') as csv_file:
    writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
      writer.writerow(["NAME", "AGE", "CONTACT_NUMBER", "EMAIL_ID"])
    writer.writerow(info_list)
if __name__ == '__main__':
condition=true
student_no = 1
while(condition):
  student_info= input("Enter some student details for student #{}:" format(student_no)
  
   student_info_list = student_info.split(' ')
  print("\n Entered info is- \n NAME: {}\n AGE: {}\n CONTACT_NUMBER: {}\n EMAIL_ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]
  choice_check = input("is the info correct?(yes or no): ")
   if choioce_check == "yes":
      write_into_csv(student_info_list)
      cond_check= input("Enter yes or no if you want to enter another student details:")
      if cond_check == "yes":
      condition= true
      student_no = student_no+1
      else if cond_check == "no"
      condition = false
   else if choice_check == "no":
      print("\n please re enter the details")
