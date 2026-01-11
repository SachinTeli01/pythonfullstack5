
#Online Order Summery Generator 1
item_prices = [199, 1299, 299, 799, 198]
total_order_value = sum(item_prices)
average_price = total_order_value / len(item_prices)
print("Item Prices:", item_prices)
print("Total Order Value: ", total_order_value)
print("Average Item Price: ", average_price)

#Product Category Tracker 2
from typing import ValuesView
products={
    "Laptop":"Electronics",
    "Chair":"Furniture",
    "Mobile":"Electronics"
}
for categories in products.keys():
    print("products name:",categories)
for categories in products.values():
    print("categories: ",categories)
print(len(products))

visitors =[120, 250, 180, 300, 90, 210, 160]

highest_traffic = max(visitors)
lowest_traffic = min(visitors)


print("Daily Website Visitors counts for 7 days:", visitors)
print("Highest traffic Day:",highest_traffic)
print("Lowest traffic Day:", lowest_traffic)

#Customer Purchase Validation 4
purchase_amount=float(input("enter puchase amount:"))
if purchase_amount>0:
  print("valid")
else:
  print("invalid",)

# Inventory Stock Comparison 5
opening_stock=[200,156,55,399]
closing_stock=[399,58,77,999]
for i in range(len(opening_stock)):
  if closing_stock[i]>opening_stock[i]:
    print(f"product{i+1}: stock increased")
  elif closing_stock[i]<opening_stock[i]:
    print(f"product{i+1}: stock decreased")
  else:
    print(f"product{i+1}: stock remained same")

# Student Course Mapping 6
Student_Courses={
     "Asha":"Python",
     "Ravi":"Data Analytics",
     "Neha":"AI"
 }
print ("Student Names:")
for Student in Student_Courses.keys():
  print(Student)
print("\nEnrolled Courses:")
for Course in Student_Courses.values():
  print(Course)
student_name=input("Enter student Name:")
if student_name in Student_Courses:
  print(f"\n{student_name} is enrolled in {Student_Courses[student_name]}")
else:
  print(f"\n{student_name} is not enrolled in any courses")

#Delivery Distance Category 7
delivery_distance=int(input(" delivery distance in km:"))
if delivery_distance<=5:
  print("Local")
elif delivery_distance>=6-20 and delivery_distance==20:
  print("Outstation")
else:
  print("City")

#Online Exam Score Analyzer 8
student_scores=[50,88.5,98,63.23]
total_score=sum(student_scores)
average_score=total_score/len(student_scores)
print("Total Score:",total_score)
print("Average Score:",average_score)
count_of_scores_above_average=0
for score in student_scores:
  if score >= average_score:
    count_of_scores_above_average+=1
print("Number of scores above average:", count_of_scores_above_average)

#Online Exam Score Analyzer 8
student_scores=[50,88.5,98,63.23]
total_score=sum(student_scores)
average_score=total_score/len(student_scores)
print("Total Score:",total_score)
print("Average Score:",average_score)
count_of_scores_above_average=0
for score in student_scores:
  if score >= average_score:
    count_of_scores_above_average+=1
print("Number of scores above average:", count_of_scores_above_average)

#product price lock system 9
fixed_product_price= (55,99,199,89,299)
print(fixed_product_price[0])
fixed_product_price[1]=54

#Feedback Count Dashboard 10
feedbacks={
    "Positive":45,
    "Neutral":18,
    "Negative":7,
}
total_feeddback=sum(feedbacks.values())
print("Total Feedbacks:",total_feeddback)
total=max(feedbacks)
print ("Highest Feedback Type:",total)
