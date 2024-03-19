import dao
import exception
import entity
class CourierServiceDb:
    connection = dao.connect_to_sql_server()

    def __init__(self):
        self.connection = dao.connect_to_sql_server()

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
        except exception.InvalidEmployeeIdException as ex:
            print(f"Error retrieving assigned orders: {ex}")
        except Exception as ex:
            print(f"Error retrieving assigned orders: {ex}")
        finally:
            cursor.close()

    def addCourierStaff(self, empID, name, email, contact_number, role, salary):
        try:
            cursor = self.connection.cursor()

          
            sql_query = """INSERT INTO Employees (EmployeeID,Name, Email, ContactNumber, Role, Salary)
                             VALUES (?,?, ?, ?, ?, ?)"""

          
            cursor.execute(sql_query, (empID, name, email, contact_number, role, salary))

       
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
        except exception.TrackingNumberNotFoundException as ex:
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

