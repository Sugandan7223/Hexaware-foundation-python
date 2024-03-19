


from abc import ABC, abstractmethod
import pyodbc

def connect_to_sql_server():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-A08GADU\SQLEXPRESS01;'
                              'Database=Courier;'
                              'Trusted_Connection=yes;')
        print("Connected Successfully")
        return conn
    except pyodbc.Error as ex:
        print(f"Error: {ex}")


def close_connection(conn):
    conn.close()
    print("Connection closed.")




class TrackingNumberNotFoundException(Exception):
    pass

class InvalidEmployeeIdException(Exception):
    pass


class CourierServiceDb:
    connection =connect_to_sql_server()

    def __init__(self):
        self.connection = connect_to_sql_server()

    def cancelOrder(self, tracking_number):
        try:
            cursor = self.connection.cursor()

            
            sql_query = """UPDATE Couriers 
                              SET Status = 'Cancelled'
                              WHERE TrackingNumber = ?"""

            
            cursor.execute(sql_query, (tracking_number,))

    
            self.connection.commit()

            print("Order cancelled successfully.")
        except Exception as ex:
            print(f"Error cancelling order: {ex}")
        finally:
            cursor.close()
    def getCouriersByEmployee(self, employee_id):
        try:
            cursor = self.connection.cursor()

                sql_query = """SELECT *
                             FROM Couriers
                             WHERE EmployeeID = ?"""

              cursor.execute(sql_query, (employee_id,))

              couriers = cursor.fetchall()

            print("Couriers retrieved successfully.")
            return couriers
        except InvalidEmployeeIdException as ex:
            print(f"Error retrieving assigned orders: {ex}")
        except Exception as ex:
            print(f"Error retrieving assigned orders: {ex}")
        finally:
            cursor.close()
    def addCourierStaff(self,empID ,name, email, contact_number, role, salary):
        try:
            cursor = self.connection.cursor()

           
            sql_query = """INSERT INTO Employees (EmployeeID,Name, Email, ContactNumber, Role, Salary)
                             VALUES (?,?, ?, ?, ?, ?)"""

           
            cursor.execute(sql_query, (empID,name, email, contact_number, role, salary))

          
            self.connection.commit()

            print("Courier staff added successfully.")
        except Exception as ex:
            print(f"Error adding courier staff: {ex}")
        finally:
            cursor.close()

    def insertOrder(self, courierID, sender_name, sender_address, receiver_name, receiver_address, weight, status,
                    tracking_number, delivery_date, location_id, employee_id, service_id):
        try:
            cursor = self.connection.cursor()

            
            sql_query = """INSERT INTO Couriers (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, LocationID, EmployeeID, ServiceID)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

           
            cursor.execute(sql_query,
                           (courierID, sender_name, sender_address, receiver_name, receiver_address, weight, status,
                            tracking_number, delivery_date, location_id, employee_id, service_id))

            
            self.connection.commit()

            print("Order inserted successfully.")
        except Exception as ex:
            print(f"Error inserting order: {ex}")
        finally:
            cursor.close()

    def updateCourierStatus(self, trackingNumber, newStatus):
        try:
            cursor = self.connection.cursor()

           
            sql_query = """UPDATE Couriers 
                           SET Status = ?
                           WHERE TrackingNumber = ?"""

           
            cursor.execute(sql_query, (newStatus, trackingNumber))

            
            self.connection.commit()

            print("Order cancelled successfully.")
        except TrackingNumberNotFoundException as ex:
            print(f"Error cancelling order: {ex}")
        except Exception as ex:
            print(f"Error cancelling order: {ex}")
        finally:
            cursor.close()

    def retrieveDeliveryHistory(self, trackingNumber):
        try:
            cursor = self.connection.cursor()

           
            sql_query = """SELECT *
                           FROM Couriers
                           WHERE TrackingNumber = ?"""

           
            cursor.execute(sql_query, (trackingNumber,))

           
            delivery_history = cursor.fetchall()

            print("Delivery history retrieved successfully.")
            return delivery_history
        except Exception as ex:
            print(f"Error retrieving delivery history: {ex}")
        finally:
            cursor.close()

    def generateShipmentStatusReport(self):
        try:
            cursor = self.connection.cursor()

           
            sql_query = """SELECT TrackingNumber, Status
                           FROM Couriers"""

         
            cursor.execute(sql_query)

           
            shipment_status_report = cursor.fetchall()

            print("Shipment status report generated successfully.")
            return shipment_status_report
        except Exception as ex:
            print(f"Error generating shipment status report: {ex}")
        finally:
            cursor.close()

    def generateRevenueReport(self):
        try:
            cursor = self.connection.cursor()

           
            sql_query = """SELECT SUM(Amount) as TotalRevenue
                           FROM Payments"""

          
            cursor.execute(sql_query)

           
            total_revenue = cursor.fetchone()[0]

            print("Revenue report generated successfully.")
            return total_revenue
        except Exception as ex:
            print(f"Error generating revenue report: {ex}")
        finally:
            cursor.close()


class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass

class ICourierAdminService(ABC):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass


class User:
    def __init__(self, userID, userName, email, password, contactNumber, address):
        self.__userID = userID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

    def get_userID(self):
        return self.__userID

    def set_userID(self, userID):
        self.__userID = userID

    def get_userName(self):
        return self.__userName

    def set_userName(self, userName):
        self.__userName = userName

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_contactNumber(self):
        return self.__contactNumber

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"UserID: {self.__userID}, UserName: {self.__userName}, Email: {self.__email}, Password: {self.__password}, ContactNumber: {self.__contactNumber}, Address: {self.__address}"


class Courier:
    def __init__(self, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber, deliveryDate, userId):
        self.__courierID = courierID
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = trackingNumber
        self.__deliveryDate = deliveryDate
        self.__userId = userId

    def get_courierID(self):
        return self.__courierID

    def set_courierID(self, courierID):
        self.__courierID = courierID

    def get_senderName(self):
        return self.__senderName

    def set_senderName(self, senderName):
        self.__senderName = senderName

    def get_senderAddress(self):
        return self.__senderAddress

    def set_senderAddress(self, senderAddress):
        self.__senderAddress = senderAddress

    def get_receiverName(self):
        return self.__receiverName

    def set_receiverName(self, receiverName):
        self.__receiverName = receiverName

    def get_receiverAddress(self):
        return self.__receiverAddress

    def set_receiverAddress(self, receiverAddress):
        self.__receiverAddress = receiverAddress

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_trackingNumber(self):
        return self.__trackingNumber

    def set_trackingNumber(self, trackingNumber):
        self.__trackingNumber = trackingNumber

    def get_deliveryDate(self):
        return self.__deliveryDate

    def set_deliveryDate(self, deliveryDate):
        self.__deliveryDate = deliveryDate

    def get_userId(self):
        return self.__userId

    def set_userId(self, userId):
        self.__userId = userId

    def __str__(self):
        return f"CourierID: {self.__courierID}, SenderName: {self.__senderName}, SenderAddress: {self.__senderAddress}, ReceiverName: {self.__receiverName}, ReceiverAddress: {self.__receiverAddress}, Weight: {self.__weight}, Status: {self.__status}, TrackingNumber: {self.__trackingNumber}, DeliveryDate: {self.__deliveryDate}, UserID: {self.__userId}"


class Employee:
    def __init__(self, employeeID, employeeName, email, contactNumber, role, salary):
        self.__employeeID = employeeID
        self.__employeeName = employeeName
        self.__email = email
        self.__contactNumber = contactNumber
        self.__role = role
        self.__salary = salary

    def get_employeeID(self):
        return self.__employeeID

    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

    def get_employeeName(self):
        return self.__employeeName

    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_contactNumber(self):
        return self.__contactNumber

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f"EmployeeID: {self.__employeeID}, EmployeeName: {self.__employeeName}, Email: {self.__email}, ContactNumber: {self.__contactNumber}, Role: {self.__role}, Salary: {self.__salary}"


class Location:
    def __init__(self, LocationID, LocationName, Address):
        self.__LocationID = LocationID
        self.__LocationName = LocationName
        self.__Address = Address

    def get_LocationID(self):
        return self.__LocationID

    def set_LocationID(self, LocationID):
        self.__LocationID = LocationID

    def get_LocationName(self):
        return self.__LocationName

    def set_LocationName(self, LocationName):
        self.__LocationName = LocationName

    def get_Address(self):
        return self.__Address

    def set_Address(self, Address):
        self.__Address = Address

    def __str__(self):
        return f"LocationID: {self.__LocationID}, LocationName: {self.__LocationName}, Address: {self.__Address}"


class CourierCompany:
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__courierDetails = []
        self.__employeeDetails = []
        self.__locationDetails = []

    def get_companyName(self):
        return self.__companyName

    def set_companyName(self, companyName):
        self.__companyName = companyName

    def add_courier(self, courier):
        self.__courierDetails.append(courier)

    def remove_courier(self, courier):
        self.__courierDetails.remove(courier)

    def add_employee(self, employee):
        self.__employeeDetails.append(employee)

    def remove_employee(self, employee):
        self.__employeeDetails.remove(employee)

    def add_location(self, location):
        self.__locationDetails.append(location)

    def remove_location(self, location):
        self.__locationDetails.remove(location)

    def __str__(self):
        return f"CompanyName: {self.__companyName}, CourierDetails: {self.__courierDetails}, EmployeeDetails: {self.__employeeDetails}, LocationDetails: {self.__locationDetails}"


class Payment:
    def __init__(self, PaymentID, CourierID, LocationID, Amount, PaymentDate, EmployeeID):
        self.__PaymentID = PaymentID
        self.__CourierID = CourierID
        self.__LocationID = LocationID
        self.__Amount = Amount
        self.__PaymentDate = PaymentDate
        self.__EmployeeID = EmployeeID

    def get_PaymentID(self):
        return self.__PaymentID

    def set_PaymentID(self, PaymentID):
        self.__PaymentID = PaymentID

    def get_CourierID(self):
        return self.__CourierID

    def set_CourierID(self, CourierID):
        self.__CourierID = CourierID

    def get_LocationID(self):
        return self.__LocationID

    def set_LocationID(self, LocationID):
        self.__LocationID = LocationID

    def get_Amount(self):
        return self.__Amount

    def set_Amount(self, Amount):
        self.__Amount = Amount

    def get_PaymentDate(self):
        return self.__PaymentDate

    def set_PaymentDate(self, PaymentDate):
        self.__PaymentDate = PaymentDate

    def get_EmployeeID(self):
        return self.__EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def __str__(self):
        return f"PaymentID: {self.__PaymentID}, CourierID: {self.__CourierID}, LocationID: {self.__LocationID}, Amount: {self.__Amount}, PaymentDate: {self.__PaymentDate}, EmployeeID: {self.__EmployeeID}"
def main():
   
    connection = connect_to_sql_server()

  
    courier_service = CourierServiceDb()

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


            empID=int(input("Enter staff ID:"))
            name = input("Enter staff name: ")
            email = input("Enter staff email: ")
            contact_number = input("Enter staff contact number: ")
            role = input("Enter staff role: ")
            salary = float(input("Enter staff salary: "))
            courier_service.addCourierStaff(empID,name, email, contact_number, role, salary)

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

   
    close_connection(connection)

if __name__ == "__main__":
    main()
