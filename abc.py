r=float(input("Enter the Radius of circle: "))
area = 3.14*r*r
perimeter = 2*3.14*r
print("Area of Circle: ",area)
print("Perimeter of Circle: ",perimeter)

#taking input of the filename and printing the extension of the filename
fn= input("Enter a Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
