import dao
import entity
import exception
import util
from abc import ABC, abstractmethod




def main():

    connection = dao.connect_to_sql_server()

  
    courier_service = util.CourierServiceDb()

    while True:
        print("\nCourier Service Menu:")
        print("1. Place an order")
        print("2. Get order status")
        print("3. Cancel an order")
        print("4. Get assigned orders")
        print("5. Add courier staff (Admin)")
        print("6. Generate report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
          
            courierID = int(input("Enter your courier ID: "))
            sender_name = input("Enter sender's name: ")
            sender_address = input("Enter sender's address: ")
            receiver_name = input("Enter receiver's name: ")
            receiver_address = input("Enter receiver's address: ")
            weight = float(input("Enter weight: "))
            tracking_number = input("Enter tracking number: ")
            delivery_date = input("Enter delivery date (YYYY-MM-DD): ")
            location_id = int(input("Enter location ID: "))
            employee_id = int(input("Enter employee ID: "))
            service_id = int(input("Enter service ID: "))

          
            courier_service.insertOrder(courierID, sender_name, sender_address, receiver_name, receiver_address, weight,
                                        "Processing", tracking_number, delivery_date, location_id, employee_id,
                                        service_id)


        elif choice == '2':
           
            tracking_number = input("Enter tracking number: ")
            status = courier_service.retrieveDeliveryHistory(tracking_number)
            print(f"Order status for tracking number {tracking_number}: {status}")

        elif choice == '3':
          
            tracking_number = input("Enter tracking number: ")
            courier_service.cancelOrder(tracking_number)

        elif choice == '4':
           
            employee_id = input("Enter employee ID: ")

           
            couriers = courier_service.getCouriersByEmployee(employee_id)

          
            print("Couriers handled by Employee ID:", employee_id)
            for courier in couriers:
                print(courier)




        elif choice == '5':

            empID = int(input("Enter staff ID:"))
            name = input("Enter staff name: ")
            email = input("Enter staff email: ")
            contact_number = input("Enter staff contact number: ")
            role = input("Enter staff role: ")
            salary = float(input("Enter staff salary: "))
            courier_service.addCourierStaff(empID, name, email, contact_number, role, salary)

        elif choice == '6':
            shipment_status_report = courier_service.generateShipmentStatusReport()
            print("Shipment status report:")
            for row in shipment_status_report:
                print(row)

            total_revenue = courier_service.generateRevenueReport()
            print("Total Revenue:", total_revenue)
        elif choice == '7':
           
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

  
    dao.close_connection(connection)


if __name__ == "__main__":
    main()
