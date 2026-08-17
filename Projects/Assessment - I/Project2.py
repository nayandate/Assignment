'''
Restaurant Management System
Modules
1. Customer Module
   Enter customer name
   Mobile number
   Table number
   Number of people
2. Table Management
   View available tables
   Book table
   Change table
   Cancel booking
3. Food Menu
   Breakfast
   Lunch
   Dinner
   Beverages
   Desserts
4. Order Management
   View current order
   Clear order
5. Billing System
   Calculate subtotal
   GST (e.g., 5%)
   Discount (if bill > ₹1000)
   Service charge (optional)
   Print final bill
6. Payment Module
   Cash
   UPI
   Card
   Split payment
7. Customer Feedback
   Rate food (1-5)
   Rate service (1-5)
   Add comments
8. Exit
'''

print("==============================")
print("     RESTAURANT MANAGEMENT    ")
print("==============================")


cname=None
table_number=None
total_people=None
table_booked=None
count = 0

idli_unit = 0
dosa_unit = 0
upma_unit = 0
poha_unit = 0
vada_unit = 0

thali_unit = 0
biryani_unit = 0
paneer_unit = 0
dal_unit = 0
roti_unit = 0

chicken_unit = 0
fish_unit = 0
pulao_unit = 0
mixed_veg_unit = 0
raita_unit = 0

tea_unit = 0
coffee_unit = 0
soft_drink_unit = 0
fresh_juice_unit = 0
mineral_water_unit = 0

gulab_jamun_unit = 0
rasgulla_unit = 0
ice_cream_unit = 0
chocolate_brownie_unit = 0
fruit_salad_unit = 0

subtotal = 0
gst = 0
service_charge = 0
discount = 0

while True:
   print("\n1. Customer Registration")
   print("2. Table Management")
   print("3. Food Menu")
   print("4. Order Management")
   print("5. Billing")
   print("6. Payment")
   print("7. Feedback")
   print("8. Exit")
   choice = int(input("\nEnter your choice (1-8): "))
   match choice:
      case 1:
         # Customer Registration
         cname = input("Enter customer name: ")
         mobile_number = int(input("Enter mobile number: "))
         total_people = int(input("Enter number of people: "))
         while True:
            if total_people >= 5 and total_people <= 20:
               print("\nTable (11-25) is available for booking. ")
               table_number = int(input("Enter table number : "))
               if table_number>=11 and table_number<=25:
                  print("Table Booked :")
                  break
               else:
                  print("Table is not available.\nChoose table number between 11-25")
            elif total_people < 5:
               print("Table (1-10) is available for booking.")
               table_number = int(input("Enter table number : "))
               if table_number>=1 and table_number<=10:
                  print("Table is booked :")
                  break
               elif table_number>=11 and table_number<=25:
                  print("\nTable is for above 10 people :\nChoose table number between 1-10")
               else:
                  print("\nTable is not available.")
            else:
               print("\nSorry, we cannot accommodate more than 20 people.")
               total_people = int(input("Enter number of people again: "))
            
         # Printing customer registration details
         print("\n",cname," registered successfully.")
         print("Mobile Number: ",mobile_number)
         print("Total People: ",total_people)
         print("Table Number: ",table_number)

      case 2 :
         if cname is None:
            print("\nPlease register customer first.")
         # Table Management
         if table_number is None:
            print("\nNo customer has booked a table yet.")

         else:
           print("\nTable Management Options:")
           
           while True:
               print("1. Booked table")
               print("2. Change table")
               print("3. Cancel booking")
               table_choice = int(input("\nEnter your choice (1-3): "))
               match table_choice:
                  case 1:
                     print("Booked Table: ",table_number)
                     break

                  case 2:
                     old_table = table_number  
                     if total_people >= 5 and total_people <= 20:
                        print("\nTable (11-25) is available for booking. ")
                        table_number = int(input("Enter table number : "))
                        if table_number>=11 and table_number<=25:
                           print("Table Booked :")
                           print("Table ",table_number," booked successfully.\n")
                           print("Table changed from ",old_table,"to",table_number)
                           break
                        else:
                           print("Table is not available.")
                     elif total_people < 5:
                        print("\nTable (1-10) is available for booking.")
                        table_number = int(input("Enter table number : "))
                        if table_number>=1 and table_number<=10:
                           print("\nTable is booked :")
                           print("Table ",table_number," booked successfully.\n")
                           print("Table changed from ",old_table,"to",table_number)
                           break
                        elif table_number>=11 and table_number<=25:
                           print("\nTable is for above 10 people :\nChoose table number between 1-10")
                     else:
                        print("\nTable is not available.   ")

                  case 3:
                     table_to_cancel = int(input("Enter table number to cancel booking: "))
                     if table_to_cancel == table_number:
                        table_number = None
                        print("Booking for table ",table_to_cancel," canceled.")
                        break
                     else:
                        print("No booking found for table ",table_to_cancel)
      case 3:
         if cname is None:
            print("Please register customer first.")
         # Food Menu
         if table_number is None:
           print("No customer has booked a table yet.")
         else:
           print("Food Menu Options:")
           print("1. Breakfast")
           print("2. Lunch")
           print("3. Dinner")
           print("4. Beverages")
           print("5. Desserts")

           menu_choice = int(input("\nEnter your choice (1-5): "))
           match menu_choice:
               case 1:
                     while True:
                        print("Breakfast Menu:")
                        print("1. Idli - ₹50")
                        print("2. Dosa - ₹80")
                        print("3. Upma - ₹60")
                        print("4. Poha - ₹40")
                        print("5. Vada - ₹30")
                        print("6. Menu Exit")
                     
                        breakfast_choice = int(input("\nEnter your choice (1-6): "))
                        match breakfast_choice:
                           case 1:
                              idli_unit = int(input("\nQuantity : "))
                              count+=50*idli_unit
                              print("\nYou have ordered ",idli_unit," Idli.")
                           case 2:
                              dosa_unit = int(input("\nQuantity : "))
                              count+=80*dosa_unit
                              print("\nYou have ordered ",dosa_unit," Dosa.")
                           case 3:
                              upma_unit = int(input("\nQuantity : "))
                              count+=60*upma_unit
                              print("\nYou have ordered ",upma_unit," Upma.")
                           case 4:
                              poha_unit = int(input("\nQuantity : "))
                              count+=40*poha_unit
                              print("\nYou have ordered ",poha_unit," Poha.")
                           case 5:
                              vada_unit = int(input("\nQuantity : "))
                              count+=30*vada_unit
                              print("\nYou have ordered ",vada_unit," Vada.")
                           case 6:
                              break
                           case _:
                              print("Invalid choice.")

               case 2:
                    while True:
                        print("Lunch Menu:")
                        print("1. Thali - ₹150")
                        print("2. Biryani - ₹120")
                        print("3. Paneer Butter Masala - ₹180")
                        print("4. Dal Makhani - ₹100")
                        print("5. Roti/Naan - ₹20")
                        print("6. Menu Exit")
                     
                        lunch_choice = int(input("\nEnter your choice (1-6): "))
                        match lunch_choice:
                           case 1:
                              thali_unit = int(input("\nQuantity : "))
                              count+=150*thali_unit
                              print("\nYou have ordered ",thali_unit," Thali.")
                           case 2:
                              biryani_unit = int(input("\nQuantity : "))
                              count+=120*biryani_unit
                              print("\nYou have ordered ",biryani_unit," Biryani.")
                           case 3:
                              paneer_unit = int(input("\nQuantity : "))
                              count+=180*paneer_unit
                              print("\nYou have ordered ",paneer_unit," Paneer Butter Masala.")
                           case 4:
                              dal_unit = int(input("\nQuantity : "))
                              count+=100*dal_unit
                              print("\nYou have ordered ",dal_unit," Dal Makhani.")
                           case 5:
                              roti_unit = int(input("\nQuantity : "))
                              count+=20*roti_unit
                              print("\nYou have ordered ",roti_unit," Roti.")
                           case 6:
                              break
                           case _:
                              print("Invalid choice.")
               case 3:
                    while True:
                        print("Dinner Menu:")
                        print("1. Chicken Curry - ₹200")
                        print("2. Fish Fry - ₹250")
                        print("3. Veg Pulao - ₹150")
                        print("4. Mixed Veg Curry - ₹120")
                        print("5. Raita - ₹30")
                        print("6. Menu Exit")
                     
                        dinner_choice = int(input("\nEnter your choice (1-6): "))
                        match dinner_choice:
                           case 1:
                              chicken_unit = int(input("\nQuantity : "))
                              count+=200*chicken_unit
                              print("\nYou have ordered ",chicken_unit," Chicken Curry.")
                           case 2:
                              fish_unit = int(input("\nQuantity : "))
                              count+=250*fish_unit
                              print("\nYou have ordered ",fish_unit," Fish Fry.")
                           case 3:
                              pulao_unit = int(input("\nQuantity : "))
                              count+=150*pulao_unit
                              print("\nYou have ordered ",pulao_unit," Veg Pulao.")
                           case 4:
                              mixed_veg_unit = int(input("\nQuantity : "))
                              count+=120*mixed_veg_unit
                              print("\nYou have ordered ",mixed_veg_unit," Mixed Veg Curry.")
                           case 5:
                              raita_unit = int(input("\nQuantity : "))
                              count+=30*raita_unit
                              print("\nYou have ordered ",raita_unit," Raita.")
                           case 6:
                              break
                           case _:
                              print("Invalid choice.")

               case 4:
                    while True:
                        print("Beverages Menu:")
                        print("1. Tea - ₹20")
                        print("2. Coffee - ₹30")
                        print("3. Soft Drinks - ₹40")
                        print("4. Fresh Juice - ₹60")
                        print("5. Mineral Water - ₹15")
                        print("6. Menu Exit")
                    
                        beverage_choice = int(input("\nEnter your choice (1-6): "))
                        match beverage_choice:
                           case 1:
                              tea_unit = int(input("\nQuantity : "))
                              count+=20*tea_unit
                              print("\nYou have ordered ",tea_unit," Tea.")
                           case 2:
                              coffee_unit = int(input("\nQuantity : "))
                              count+=30*coffee_unit
                              print("\nYou have ordered ",coffee_unit," Coffee.")
                           case 3:
                              soft_drink_unit = int(input("\nQuantity : "))
                              count+=40*soft_drink_unit
                              print("\nYou have ordered ",soft_drink_unit," Soft Drinks.")
                           case 4:
                              fresh_juice_unit = int(input("\nQuantity : "))
                              count+=60*fresh_juice_unit
                              print("\nYou have ordered ",fresh_juice_unit," Fresh Juice.")
                           case 5:
                              mineral_water_unit = int(input("\nQuantity : "))
                              count+=15*mineral_water_unit
                              print("\nYou have ordered ",mineral_water_unit," Mineral Water.")
                           case 6:
                              break
                           case _:
                              print("Invalid choice.")
   
               case 5:
                    while True:
                        print("Desserts Menu:")
                        print("1. Gulab Jamun - ₹50")
                        print("2. Rasgulla - ₹60")
                        print("3. Ice Cream Sundae - ₹80")
                        print("4. Chocolate Brownie - ₹90")
                        print("5. Fruit Salad - ₹70")
                        print("6. Menu Exit")
                        desert_choice = int(input("\nEnter your choice (1-6): "))
                        match desert_choice:
                           case 1:
                              gulab_jamun_unit = int(input("\nQuantity : "))
                              count+=50*gulab_jamun_unit
                              print("\nYou have ordered ",gulab_jamun_unit," Gulab Jamun.")
                           case 2:
                              rasgulla_unit = int(input("\nQuantity : "))
                              count+=60*rasgulla_unit
                              print("\nYou have ordered ",rasgulla_unit," Rasgulla.")
                           case 3:
                              ice_cream_unit = int(input("\nQuantity : "))
                              count+=80*ice_cream_unit
                              print("\nYou have ordered ",ice_cream_unit," Ice Cream Sundae.")
                           case 4:
                              chocolate_brownie_unit = int(input("\nQuantity : "))
                              count+=90*chocolate_brownie_unit
                              print("\nYou have ordered ",chocolate_brownie_unit," Chocolate Brownie.")
                           case 5:
                              fruit_salad_unit = int(input("\nQuantity : "))
                              count+=70*fruit_salad_unit
                              print("\nYou have ordered ",fruit_salad_unit," Fruit Salad.")
                           case 6:
                              break
                           case _:
                              print("Invalid choice.")
      case 4:
         if cname is None:
            print("Please register customer first.")
         else:
           # Order Management
           
           while True:
               print("1. View current order")
               print("2. Clear order")
               print("3. Back")
               order_choice = int(input("\nEnter your choice (1-3): "))
               match order_choice:
                  case 1:
                     if count == 0:
                         print("No items in the current order.")
                     else:
                         print("Current order:")
                         if idli_unit > 0:
                             print("\nIdli x ",idli_unit)
                         if dosa_unit > 0:
                             print("\nDosa x ",dosa_unit)
                         if vada_unit > 0:
                             print("\nVada x ",vada_unit)
                         if upma_unit > 0:
                             print("\nUpma x ",upma_unit)
                         if poha_unit > 0:
                             print("\nPoha x ",poha_unit)
                         if thali_unit > 0:
                             print("\nThali x ",thali_unit)
                         if biryani_unit > 0:
                             print("\nBiryani x ",biryani_unit)
                         if paneer_unit > 0:
                             print("\nPaneer Butter Masala x ",paneer_unit)
                         if dal_unit > 0:
                             print("\nDal Makhani x ",dal_unit)
                         if roti_unit > 0:
                             print("\nRoti x ",roti_unit)
                         if chicken_unit > 0:
                             print("\nChicken Curry x ",chicken_unit)
                         if fish_unit > 0:
                             print("\nFish Fry x ",fish_unit)
                         if pulao_unit > 0:
                             print("\nVeg Pulao x ",pulao_unit)
                         if mixed_veg_unit > 0:
                             print("\nMixed Veg Curry x ",mixed_veg_unit)
                         if raita_unit > 0:
                             print("\nRaita x ",raita_unit)
                         if tea_unit > 0:
                              print("\nTea x ",tea_unit)
                         if coffee_unit > 0:
                              print("\nCoffee x ",coffee_unit)
                         if soft_drink_unit > 0:
                              print("\nSoft Drinks x ",soft_drink_unit)
                         if fresh_juice_unit > 0:
                              print("\nFresh Juice x ",fresh_juice_unit)
                         if mineral_water_unit > 0:
                              print("\nMineral Water x ",mineral_water_unit)
                         if gulab_jamun_unit > 0:
                              print("\nGulab Jamun x ",gulab_jamun_unit)
                         if rasgulla_unit > 0:
                              print("\nRasgulla x ",rasgulla_unit)
                         if ice_cream_unit > 0:
                              print("\nIce Cream Sundae x ",ice_cream_unit)
                         if chocolate_brownie_unit > 0:
                              print("\nChocolate Brownie x ",chocolate_brownie_unit)
                         if fruit_salad_unit > 0:
                              print("\nFruit Salad x ",fruit_salad_unit)
                              
                           
                  case 2:
                     if count == 0:
                         print("\nNo items in the order to clear.")
                     else:
                         count = 0
                         idli_unit = dosa_unit = upma_unit = poha_unit = vada_unit = 0
                         
                         thali_unit = 0
                         biryani_unit = 0
                         paneer_unit = 0
                         dal_unit = 0
                         roti_unit = 0
                         
                         chicken_unit = 0
                         fish_unit = 0
                         pulao_unit = 0
                         mixed_veg_unit = 0
                         raita_unit = 0
                         
                         tea_unit = 0
                         coffee_unit = 0
                         soft_drink_unit = 0
                         fresh_juice_unit = 0
                         mineral_water_unit = 0
                         
                         gulab_jamun_unit = 0
                         rasgulla_unit = 0
                         ice_cream_unit = 0
                         chocolate_brownie_unit = 0
                         fruit_salad_unit = 0

                         subtotal = 0
                         gst = 0
                         discount = 0
                         service_charge = 0
                         total = 0
                         
                         print("Order cleared.")
                  case 3:
                      break
                  case _:
                      print("Invalid choice.") 

      case 5:
       if cname is None:
          print("Please register customer first.")
       else:
        # Billing 
        while True:
         print("1. Subtotal")
         print("2. GST (5%)")
         print("3. Service charge (optional)")
         print("4. Discount (if bill > ₹5000 get 20% discount)")
         print("5. Print final bill")
         print("6. Back")
        
         choice = int(input("\nEnter your choice (1-6): "))
         match choice:
            case 1:
               subtotal = count
               print("Subtotal: ",subtotal)
            case 2:
               gst = subtotal*5//100
               print("GST: ",gst)
            case 3:
               service_charge = int(input("Enter service charge amount: "))
               print("Service charge: ",service_charge)
            case 4:
               if (subtotal+gst+service_charge) > 5000:
                  discount = (subtotal+gst+service_charge)*20//100
                  print("Discount: ",discount)
               else:
                  discount = 0
                  print("No Discount")
            case 5:
               if count == 0:
                  print("No items in the current order.")
               else:
                  print("Customer : ",cname)

                  print("Mobile : ",mobile_number)

                  print("Table : ",table_number)

                  print("People : ",total_people)

                  print("----------------------------")
                  print("            Items           ")
                  print("----------------------------")
                  subtotal = count
                  gst = subtotal * 5 // 100
                  if subtotal + gst + service_charge > 5000:
                      discount = (subtotal + gst + service_charge) * 20 // 100
                  else:
                      discount = 0
                  total = subtotal + gst + service_charge - discount

                  print("\n           Final Bill           ")
                  if idli_unit > 0:
                      print("\nIdli x ",idli_unit," = ",50*idli_unit)
                  if dosa_unit > 0:
                      print("\nDosa x ",dosa_unit," = ",80*dosa_unit)
                  if vada_unit > 0:
                      print("\nVada x ",vada_unit," = ",30*vada_unit)
                  if upma_unit > 0:
                      print("\nUpma x ",upma_unit," = ",60*upma_unit)
                  if poha_unit > 0:
                      print("\nPoha x ",poha_unit," = ",40*poha_unit)
                  if thali_unit > 0:
                      print("\nThali x ",thali_unit," = ",150*thali_unit)
                  if biryani_unit > 0:
                      print("\nBiryani x ",biryani_unit," = ",120*biryani_unit)
                  if paneer_unit > 0:
                      print("\nPaneer Butter Masala x ",paneer_unit," = ",180*paneer_unit)
                  if dal_unit > 0:
                      print("\nDal Makhani x ",dal_unit," = ",100*dal_unit)
                  if roti_unit > 0:
                      print("\nRoti x ",roti_unit," = ",20*roti_unit)
                  if chicken_unit > 0:
                      print("\nChicken Curry x ",chicken_unit," = ",200*chicken_unit)
                  if fish_unit > 0:
                      print("\nFish Fry x ",fish_unit," = ",250*fish_unit)
                  if pulao_unit > 0:
                      print("\nVeg Pulao x ",pulao_unit," = ",150*pulao_unit)
                  if mixed_veg_unit > 0:
                      print("\nMixed Veg Curry x ",mixed_veg_unit," = ",120*mixed_veg_unit)
                  if raita_unit > 0:
                      print("\nRaita x ",raita_unit," = ",30*raita_unit)
                  if tea_unit > 0:
                       print("\nTea x ",tea_unit," = ",20*tea_unit)
                  if coffee_unit > 0:
                       print("\nCoffee x ",coffee_unit," = ",30*coffee_unit)
                  if soft_drink_unit > 0:
                       print("\nSoft Drinks x ",soft_drink_unit," = ",40*soft_drink_unit)
                  if fresh_juice_unit > 0:
                       print("\nFresh Juice x ",fresh_juice_unit," = ",60*fresh_juice_unit)
                  if mineral_water_unit > 0:
                       print("\nMineral Water x ",mineral_water_unit," = ",15*mineral_water_unit)
                  if gulab_jamun_unit > 0:
                       print("\nGulab Jamun x ",gulab_jamun_unit," = ",50*gulab_jamun_unit)
                  if rasgulla_unit > 0:
                       print("\nRasgulla x ",rasgulla_unit," = ",60*rasgulla_unit)
                  if ice_cream_unit > 0:
                       print("\nIce Cream Sundae x ",ice_cream_unit," = ",80*ice_cream_unit)
                  if chocolate_brownie_unit > 0:
                       print("\nChocolate Brownie x ",chocolate_brownie_unit," = ",90*chocolate_brownie_unit)
                  if fruit_salad_unit > 0:
                       print("\nFruit Salad x ",fruit_salad_unit," = ",70*fruit_salad_unit)

                  
                  print("----------------------------")
                  print("Subtotal        :", subtotal)
                  print("GST             :", gst)
                  print("Service Charge  :", service_charge)
                  print("Discount        :", discount)
                  print("----------------------------")
                  print("Final Total     :", total)
                  print("----------------------------")
            case 6:
               break
      case 6:
       if cname is None:
            print("Please register customer first.")
       else:
         
         while True:
           print("Payment Method: ")
           print("1. Cash")
           print("2. UPI")
           print("3. Card")
           print("4. Split Payment")
           if total == 0:
               print("\nPlease generate the bill first.")
               break
           else:
            payment_choice = int(input("\nEnter your choice (1-4): "))
            match payment_choice:
               case 1:
                 cash = float(input("Enter cash amount: "))
                 if cash >= total:
                   print("\nPayment Successful.")
                   print("Balance :", cash-total)
                   count = 0
                   subtotal = 0
                   gst = 0
                   discount = 0
                   service_charge = 0
                   total = 0
                   break
                 else:
                   print("Insufficient Amount.")
                   
               case 2:
                  upi_id = input("Enter UPI ID: ")
                  print("Payment successful via UPI ID:", upi_id)
                  count = 0
                  subtotal = 0
                  gst = 0
                  discount = 0
                  service_charge = 0
                  total = 0
                  break
               case 3:
                  card_number = input("Enter Card Number: ")
                  print("Payment successful via Card Number:", card_number)
                  count = 0
                  subtotal = 0
                  gst = 0
                  discount = 0
                  service_charge = 0
                  total = 0
                  break
               case 4:
                  while True:
                     cash_amount = float(input("Enter cash amount: "))
                     upi_amount = float(input("Enter UPI amount: "))
                     card_amount = float(input("Enter card amount: "))
                     total_payment = cash_amount + upi_amount + card_amount
                     if total_payment == total:
                         print("Split payment successful.")
                         count = 0
                         subtotal = 0
                         gst = 0
                         discount = 0
                         service_charge = 0
                         total = 0
                         break
                     else:
                         print("\nTotal payment does not match the final bill. Please retry.")
               case _:
                  print("Invalid Input")
      case 7:
        while True:
            print("1. Rate food")
            print("2. Rate service")
            print("3. Add comments")
            print("4. Back")
        
            choice = int(input("Enter your choice (1-4)"))
            match choice:
               case 1:
                  rate_food = int(input("Rate Food (1 is low - 5 is high): "))
                  if rate_food >5 or rate_food<1:
                     print("\nPlease rate food between (1-5)")
                  elif rate_food >=4:
                     print("\nThank You for good rating")
                  elif rate_food == 3:
                     print("\nThank You for average rating")
                  else:
                     print("\nSorry for bad experience, we will improve our food quality next time.")

               case 2:
                  rate_service = int(input("Rate Service between (1 is low - 5 is high): "))
                  if rate_service >5 or rate_service<1:
                     print("\nPlease rate service between (1-5)")
                  elif rate_service >=4:
                     print("\nThank You for good rating, see you soon")
                  elif rate_service == 3:
                     print("\nThank You for average rating, we will serve you better next time.")
                  else:
                     print("\nSorry for bad experience, we will improve our service next time.")
               
               case 3:
                  comment = input("Please give some suggestion: ")
                  print("\nThank you for your feedback")
                  break

               case 4:
                  break

               case _:
                  print("Invalid Input")

      case 8:
            print("==============================")
            print(" Thank You for Visiting")
            print(" Please Visit Again")
            print("==============================")
            break

      case _:
         print("Invalid Input")