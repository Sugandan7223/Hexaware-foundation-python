---Task1
CREATE DATABASE hexaware;
use hexaware

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(20),
    Address TEXT
);


CREATE TABLE CourierServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100),
    Cost DECIMAL(8, 2)
);


CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Role VARCHAR(50),
    Salary DECIMAL(10, 2)
);


CREATE TABLE Locations (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Address TEXT
);

CREATE TABLE Couriers (
    CourierID INT PRIMARY KEY,
    SenderName VARCHAR(255),
    SenderAddress TEXT,
    ReceiverName VARCHAR(255),
    ReceiverAddress TEXT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE
	LocationID INT,
	EmployeeID INT,
	ServiceID INT,
	CONSTRAINT FK_Couriers_Location FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
	CONSTRAINT FK_Couriers_Employee FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
	CONSTRAINT FK_Couriers_Service FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID)
);



CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    CourierID INT,
    LocationID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
	EmployeeID INT,
    FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
	FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
	
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (CustomerID) REFERENCES Users(UserID)
);


CREATE TABLE Parcels (
    ParcelID INT PRIMARY KEY,
    OrderID INT,
    CourierID INT,
    ServiceID INT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE,
	EmployeeID INT,
    CONSTRAINT FK_Parcels_Orders FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    CONSTRAINT FK_Parcels_Couriers FOREIGN KEY (CourierID) REFERENCES Couriers(CourierID),
    CONSTRAINT FK_Parcels_Services FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID),
	CONSTRAINT FK_Parcels_Employee FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);



INSERT INTO Users (UserID, Name, Email, Password, ContactNumber, Address)
VALUES(1, 'Rajesh Kumar', 'rajesh.kumar@email.com', 'password123', '9876543210', '12 Gandhi Nagar, Chennai'),
(2, 'Priya Sharma', 'priya.sharma@email.com', 'password456', '8765432109', '34 Kaveri Street, Bangalore'),
(3, 'Amit Patel', 'amit.patel@email.com', 'password789', '7654321098', '56 Krishna Lane, Hyderabad'),
(4, 'Ananya Singh', 'ananya.singh@email.com', 'passwordabc', '6543210987', '78 Vindhya Nagar, Coimbatore');

INSERT INTO Couriers (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, LocationID,EmployeeID,ServiceID)
VALUES(1, 'Sender1', 'SenderAddress1', 'Receiver1', 'ReceiverAddress1', 2.5, 'In Transit', 'TN123456', '2024-03-01',1,2,1),
(2, 'Sender2', 'SenderAddress2', 'Receiver2', 'ReceiverAddress2', 1.8, 'Delivered', 'TN789012', '2024-03-02',1,2,2),
(3, 'Sender3', 'SenderAddress3', 'Receiver3', 'ReceiverAddress3', 3.0, 'In Transit', 'TN345678', '2024-03-03',2,3,2);

INSERT INTO CourierServices (ServiceID, ServiceName, Cost)
VALUES(1, 'Standard', 10.00),
(2, 'Express', 15.00);

INSERT INTO Employees (EmployeeID, Name, Email, ContactNumber, Role, Salary)
VALUES(1, 'Manager1', 'manager1@email.com', '1112223333', 'Manager', 50000.00),
(2, 'DeliveryPerson1', 'delivery1@email.com', '4445556666', 'Delivery Person', 30000.00),
(3, 'DeliveryPerson2', 'delivery2@email.com', '5556667777', 'Delivery Person', 30000.00);

INSERT INTO Employees (EmployeeID, Name, Email, ContactNumber, Role, Salary)
VALUES(4, 'John cena', 'john.cena@email.com', '1234567890', 'Manager', 60000.00),
(5, 'Authur Johnson', 'authur.johnson@email.com', '9876543210', 'Clerk', 45000.00);


INSERT INTO Locations (LocationID, LocationName, Address)
VALUES(1, 'Warehouse1', '789 Storage St, Chennai'),
(2, 'Warehouse2', '456 Logistics Ave, Bangalore'),
(3, 'Warehouse3', '123 Distribution Rd, Hyderabad');


INSERT INTO Payments (PaymentID, CourierID, LocationID, Amount, PaymentDate,EmployeeID)
VALUES(1, 1, 1, 10.00, '2024-03-03',2),
(2, 2, 2, 15.00, '2024-03-04',2),
(3, 3, 3, 12.50, '2024-03-05',3);



INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES(1, 1, '2024-03-01'),
(2, 2, '2024-03-02'),
(3, 3, '2024-03-03');


INSERT INTO Parcels (ParcelID, OrderID, CourierID, ServiceID, Weight, Status, TrackingNumber, DeliveryDate,EmployeeID)
VALUES(1, 1, 1, 1, 2.5, 'In Transit', 'TN123456', '2024-03-01',2),
(2, 2, 2, 2, 1.8, 'Delivered', 'TN789012', '2024-03-02',2),
(3, 3, 3, 1, 3.0, 'In Transit', 'TN345678', '2024-03-03',3);




---Task2

--1

SELECT * FROM Users;
 --2

 SELECT * FROM Orders WHERE CustomerID = 1;

 --3

 SELECT * FROM Couriers;

 --4

SELECT * FROM Orders WHERE OrderID = 2;

--5


SELECT * FROM Parcels WHERE CourierID = 1;

--6

SELECT * FROM Parcels WHERE Status = 'In Transit';

--7

SELECT * FROM Parcels WHERE CAST(DeliveryDate AS DATE) = CAST(GETDATE() AS DATE);

--8

SELECT * FROM Parcels WHERE Status = 'Delivered';

--9

SELECT CourierID, COUNT(*) AS TotalPackages FROM Parcels GROUP BY CourierID;

--10

SELECT p.CourierID, AVG(DATEDIFF(DAY, o.OrderDate, p.DeliveryDate)) AS AvgDeliveryTime
FROM Parcels p JOIN Orders o ON p.OrderID = o.OrderID WHERE p.Status = 'Delivered' GROUP BY p.CourierID;

--11

SELECT * FROM Parcels WHERE Weight BETWEEN 1.0 AND 2.0; 


--12

SELECT * FROM Employees WHERE Name LIKE '%John%';

--13

SELECT * FROM Payments WHERE Amount > 50.00;

---Task 3

-- 14
SELECT e.EmployeeID, e.Name, COUNT(p.CourierID) AS TotalCouriersHandled FROM Employees e
LEFT JOIN Couriers p ON e.EmployeeID = p.EmployeeID GROUP BY e.EmployeeID, e.Name;

-- 15
SELECT l.LocationID, l.LocationName, SUM(py.Amount) AS TotalRevenue FROM Locations l
LEFT JOIN Payments py ON l.LocationID = py.LocationID GROUP BY l.LocationID, l.LocationName;
 
-- 16
SELECT l.LocationID, l.LocationName, COUNT(p.CourierID) AS TotalCouriersDelivered
FROM Locations l LEFT JOIN Couriers p ON l.LocationID = p.LocationID
WHERE p.Status = 'Delivered' GROUP BY l.LocationID, l.LocationName;

-- 17
SELECT TOP 1 CourierID, AVG(DATEDIFF(DAY, p.DeliveryDate, o.OrderDate)) AS AvgDeliveryTime FROM Parcels p, Orders o 
WHERE Status = 'Delivered'  AND p.OrderID = o.OrderID GROUP BY CourierID ORDER BY AvgDeliveryTime DESC;

-- 18
SELECT LocationID, LocationName FROM Locations WHERE LocationID
IN (SELECT LocationID FROM Payments GROUP BY LocationID HAVING SUM(Amount) < 5000);

-- 19 
SELECT LocationID, SUM(Amount) AS TotalPayments FROM Payments GROUP BY LocationID;

-- 20
SELECT p.CourierID, c.SenderName, c.ReceiverName, p.LocationID, SUM(p.Amount) AS TotalPayments
FROM Payments p JOIN Couriers c ON p.CourierID = c.CourierID WHERE p.LocationID = 1 
GROUP BY p.CourierID, c.SenderName, c.ReceiverName, p.LocationID HAVING SUM(p.Amount) > 1000;

-- 21
SELECT p.CourierID, c.SenderName, c.ReceiverName, SUM(p.Amount) AS TotalPayments
FROM Payments p JOIN Couriers c ON p.CourierID = c.CourierID WHERE p.PaymentDate > '2024-03-01' 
GROUP BY p.CourierID, c.SenderName, c.ReceiverName HAVING SUM(p.Amount) > 1000;

-- 22
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalAmountReceived FROM Locations l 
JOIN Payments p ON l.LocationID = p.LocationID WHERE p.PaymentDate > '2024-03-01'  
GROUP BY l.LocationID, l.LocationName HAVING SUM(p.Amount) > 5000;

---Task 4


--23
SELECT p.*, c.* FROM Payments p INNER JOIN Couriers c ON p.CourierID = c.CourierID;

--24
SELECT p.*, l.* FROM Payments p INNER JOIN Locations l ON p.LocationID = l.LocationID;

--25
SELECT p.*, c.*, l.* FROM Payments p INNER JOIN Couriers c ON p.CourierID = c.CourierID 
INNER JOIN Locations l ON p.LocationID = l.LocationID;

--26
SELECT p.*, c.* FROM Payments p INNER JOIN Couriers c ON p.CourierID = c.CourierID;

--27
SELECT c.CourierID, c.SenderName, c.ReceiverName, SUM(p.Amount) AS TotalPayments
FROM Couriers c LEFT JOIN Payments p ON c.CourierID = p.CourierID GROUP BY c.CourierID, c.SenderName, c.ReceiverName;

--28
SELECT * FROM Payments WHERE PaymentDate = '2024-03-03'; 

--29
SELECT p.*, c.* FROM Payments p LEFT JOIN Couriers c ON p.CourierID = c.CourierID;

--30
SELECT p.*, l.* FROM Payments p LEFT JOIN Locations l ON p.LocationID = l.LocationID;

--31
SELECT c.CourierID, c.SenderName, c.ReceiverName, SUM(p.Amount) AS TotalPayments FROM Couriers c LEFT JOIN Payments p ON c.CourierID = p.CourierID GROUP BY c.CourierID, c.SenderName, c.ReceiverName;

--32
SELECT * FROM Payments WHERE PaymentDate BETWEEN '2024-03-01' AND '2024-03-03';


--33
SELECT u.*, c.* FROM Users u FULL OUTER JOIN Couriers c ON u.name = c.SenderName;

--34
SELECT c.*, cs.* FROM Couriers c FULL OUTER JOIN CourierServices cs ON c.ServiceID = cs.ServiceID;

--35
SELECT e.*, p.*FROM Employees e FULL OUTER JOIN Payments p ON e.EmployeeID = p.EmployeeID;

--36
SELECT u.*, cs.*FROM Users u CROSS JOIN CourierServices cs;

--37
SELECT e.*, l.* FROM Employees e CROSS JOIN Locations l;


--38
SELECT c.*, u.*FROM Couriers c LEFT JOIN Users u ON c.SenderName = u.Name;

--39
SELECT c.*, u.*FROM Couriers c LEFT JOIN Users u ON c.ReceiverName = u.Name;

--40
SELECT c.*, cs.*FROM Couriers c LEFT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID;

--41
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS TotalCouriersAssigned FROM Employees e 
LEFT JOIN Couriers c ON e.EmployeeID = c.EmployeeID GROUP BY e.EmployeeID, e.Name;

--42
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPaymentsReceived
FROM Locations l LEFT JOIN Payments p ON l.LocationID = p.LocationID GROUP BY l.LocationID, l.LocationName;

--43
SELECT c1.*FROM Couriers c1 JOIN Couriers c2 ON c1.SenderName = c2.SenderName WHERE c1.CourierID <> c2.CourierID;

--44
SELECT e1.*FROM Employees e1 JOIN Employees e2 ON e1.Role = e2.Role WHERE e1.EmployeeID <> e2.EmployeeID;

--45
SELECT p1.*FROM Payments p1 JOIN Payments p2 ON p1.LocationID = p2.LocationID WHERE p1.CourierID <> p2.CourierID;

--46
SELECT c1.*FROM Couriers c1 JOIN Couriers c2 ON c1.SenderAddress = c2.SenderAddress WHERE c1.CourierID <> c2.CourierID;

--47
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS TotalCouriersDelivered FROM Employees e
LEFT JOIN Couriers c ON e.EmployeeID = c.EmployeeID WHERE c.Status = 'Delivered' GROUP BY e.EmployeeID, e.Name;


--48
SELECT c.*FROM Couriers c JOIN Payments p ON c.CourierID = p.CourierID
JOIN CourierServices cs ON c.ServiceID = cs.ServiceID WHERE p.Amount > cs.Cost;

--49
SELECT * FROM Couriers WHERE Weight > (SELECT AVG(Weight) FROM Couriers);

--50
SELECT Name FROM Employees WHERE Salary > (SELECT AVG(Salary) FROM Employees);

--51
SELECT SUM(Cost) AS TotalCost FROM CourierServices WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);

--52
SELECT c.*FROM Couriers c WHERE EXISTS (SELECT 1 FROM Payments p WHERE p.CourierID = c.CourierID);

--53
SELECT l.*
FROM Locations l WHERE LocationID = (SELECT TOP 1 LocationID FROM Payments ORDER BY Amount DESC);

--54
SELECT c.*FROM Couriers c WHERE Weight > ALL (SELECT Weight FROM Couriers WHERE SenderName = 'Sender1');

