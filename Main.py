import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="hotel"
)

c = con.cursor()


# 1. ADD CUSTOMER
def add_customer():

    print("\n╔══════════════════════════════════════╗")
    print("║          🏨 NEW GUEST ENTRY         ║")
    print("╚══════════════════════════════════════╝")

    cid = int(input("Enter Customer ID       : "))
    name = input("Enter Customer Name     : ")
    phone = input("Enter Phone Number      : ")
    address = input("Enter Address           : ")

    c.execute(
        "INSERT INTO customer VALUES (%s,%s,%s,%s)",
        (cid, name, phone, address)
    )

    con.commit()

    print("\n✓ Guest registration completed successfully!")
    print("  Welcome to our hotel, " + name + "!")


# 2. BOOK ROOM
def book_room():

    print("\n╔══════════════════════════════════════╗")
    print("║          🛎️ ROOM BOOKING            ║")
    print("╚══════════════════════════════════════╝")

    bid = int(input("Enter Booking ID        : "))
    cid = int(input("Enter Customer ID       : "))
    room = int(input("Enter Room Number       : "))
    days = int(input("Enter Number of Days    : "))

    rate = int(input("Enter Room Rate/Day     : "))

    bill = days * rate

    c.execute(
        "INSERT INTO booking VALUES (%s,%s,%s,%s,%s)",
        (bid, cid, room, days, bill)
    )

    c.execute(
        "UPDATE rooms SET status='Booked' WHERE room_no=%s",
        (room,)
    )

    con.commit()

    print("\n✓ Room booking confirmed!")
    print("  Room Number :", room)
    print("  Stay        :", days, "days")
    print("  Total Bill  : ₹", bill)
    print("  Have a pleasant stay! 🌟")


# 3. SEARCH CUSTOMER
def search_customer():

    print("\n🔎 CUSTOMER SEARCH")

    cid = int(input("Enter Customer ID: "))

    c.execute(
        "SELECT * FROM customer WHERE customer_id=%s",
        (cid,)
    )

    data = c.fetchone()

    if data:
        print("\n╔══════════════════════════════════════╗")
        print("║          CUSTOMER PROFILE           ║")
        print("╚══════════════════════════════════════╝")

        print("Customer ID :", data[0])
        print("Name        :", data[1])
        print("Phone       :", data[2])
        print("Address     :", data[3])

        print("\n✓ Record found successfully!")

    else:
        print("\n✗ No customer found with this ID.")


# 4. SEARCH BOOKING
def search_booking():

    print("\n🔎 BOOKING SEARCH")

    bid = int(input("Enter Booking ID: "))

    c.execute(
        "SELECT * FROM booking WHERE booking_id=%s",
        (bid,)
    )

    data = c.fetchone()

    if data:
        print("\n╔══════════════════════════════════════╗")
        print("║           BOOKING DETAILS           ║")
        print("╚══════════════════════════════════════╝")

        print("Booking ID  :", data[0])
        print("Customer ID :", data[1])
        print("Room No.    :", data[2])
        print("Days        :", data[3])
        print("Bill        : ₹", data[4])

        print("\n✓ Booking record found!")

    else:
        print("\n✗ Booking not found.")


# 5. UPDATE CUSTOMER
def update_customer():

    print("\n✏️ UPDATE CUSTOMER DETAILS")

    cid = int(input("Enter Customer ID: "))

    name = input("Enter New Name        : ")
    phone = input("Enter New Phone       : ")
    address = input("Enter New Address     : ")

    c.execute(
        "UPDATE customer SET name=%s, phone=%s, "
        "address=%s WHERE customer_id=%s",
        (name, phone, address, cid)
    )

    con.commit()

    print("\n✓ Customer information updated successfully!")


# 6. CANCEL BOOKING
def cancel_booking():

    print("\n⚠️ BOOKING CANCELLATION")

    bid = int(input("Enter Booking ID  : "))
    room = int(input("Enter Room Number  : "))

    c.execute(
        "DELETE FROM booking WHERE booking_id=%s",
        (bid,)
    )

    c.execute(
        "UPDATE rooms SET status='Available' WHERE room_no=%s",
        (room,)
    )

    con.commit()

    print("\n✓ Booking cancelled successfully.")
    print("  Room", room, "is now available.")


# 7. CALCULATE BILL
def calculate_bill():

    print("\n💰 BILL CALCULATOR")

    days = int(input("Enter Number of Days    : "))
    rate = int(input("Enter Room Rate/Day     : "))

    bill = days * rate

    print("\n════════════════════════════════")
    print("           BILL SUMMARY")
    print("════════════════════════════════")
    print("Number of Days :", days)
    print("Rate Per Day   : ₹", rate)
    print("Total Amount   : ₹", bill)
    print("════════════════════════════════")

    print("✓ Bill calculated successfully!")


# 8. DISPLAY CUSTOMERS
def display_customers():

    print("\n╔══════════════════════════════════════╗")
    print("║        🧑‍💼 ALL GUEST RECORDS        ║")
    print("╚══════════════════════════════════════╝")

    c.execute("SELECT * FROM customer")

    data = c.fetchall()

    if data:

        for row in data:

            print("\n--------------------------------------")
            print("Customer ID :", row[0])
            print("Name        :", row[1])
            print("Phone       :", row[2])
            print("Address     :", row[3])

        print("\n✓ All customer records displayed.")

    else:
        print("No customer records found.")


# 9. DISPLAY BOOKINGS
def display_bookings():

    print("\n╔══════════════════════════════════════╗")
    print("║          📋 ALL BOOKINGS             ║")
    print("╚══════════════════════════════════════╝")

    c.execute("SELECT * FROM booking")

    data = c.fetchall()

    if data:

        for row in data:

            print("\n--------------------------------------")
            print("Booking ID  :", row[0])
            print("Customer ID :", row[1])
            print("Room No.    :", row[2])
            print("Days        :", row[3])
            print("Bill        : ₹", row[4])

        print("\n✓ All booking records displayed.")

    else:
        print("No booking records found.")


# MAIN MENU
while True:

    print("\n")
    print("╔══════════════════════════════════════════╗")
    print("║       🏨 GRAND HOTEL MANAGEMENT 🏨       ║")
    print("║          Smart Booking System            ║")
    print("╚══════════════════════════════════════════╝")

    print("\n        -------- MAIN MENU --------")
    print("        1. 🧑 Add New Customer")
    print("        2. 🛎️  Book a Room")
    print("        3. 🔎 Search Customer")
    print("        4. 🔎 Search Booking")
    print("        5. ✏️  Update Customer")
    print("        6. ❌ Cancel Booking")
    print("        7. 💰 Calculate Bill")
    print("        8. 📋 Display Customers")
    print("        9. 📋 Display Bookings")
    print("        10. 🚪 Exit")

    print("        ----------------------------")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        add_customer()

    elif choice == 2:
        book_room()

    elif choice == 3:
        search_customer()

    elif choice == 4:
        search_booking()

    elif choice == 5:
        update_customer()

    elif choice == 6:
        cancel_booking()

    elif choice == 7:
        calculate_bill()

    elif choice == 8:
        display_customers()

    elif choice == 9:
        display_bookings()

    elif choice == 10:

        print("\n╔══════════════════════════════════════╗")
        print("║        THANK YOU FOR VISITING!      ║")
        print("║       Have a wonderful day! 🌟      ║")
        print("╚══════════════════════════════════════╝")

        break

    else:
        print("\n✗ Invalid Choice! Please select 1-10.")


c.close()
con.close()
