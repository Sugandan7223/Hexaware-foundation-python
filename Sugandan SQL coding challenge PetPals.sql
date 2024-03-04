---1

CREATE DATABASE PetPals;


use PetPals

---2,3,4

CREATE TABLE Pets (
    PetID INT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    Breed VARCHAR(255),
    Type VARCHAR(255),
    AvailableForAdoption BIT,
	ShelterName VARCHAR(255),
	OwnerID INT,
	ShelterID INT
	

);



CREATE TABLE Shelters (
    ShelterID INT PRIMARY KEY,
    Name VARCHAR(255),
    Location VARCHAR(255),
	City VARCHAR(255)
);

CREATE TABLE Donations (
    DonationID INT PRIMARY KEY,
    DonorName VARCHAR(255),
    DonationType VARCHAR(255),
    DonationAmount DECIMAL,
    DonationItem VARCHAR(255),
    DonationDate DATETIME
);

CREATE TABLE AdoptionEvents (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(255),
    EventDate DATETIME,
    Location VARCHAR(255),
	City VARCHAR(255),
	OrganizerID INT

);

CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY,
    ParticipantName VARCHAR(255),
    ParticipantType VARCHAR(255),
    EventID INT,
    FOREIGN KEY (EventID) REFERENCES AdoptionEvents(EventID),
	City VARCHAR(255)
);




---5

INSERT INTO Pets (PetID, Name, Age, Breed, Type, AvailableForAdoption,OwnerID,ShelterName,OwnerID,ShelterID)
VALUES(1, 'Raja', 2, 'Labrador Retriever', 'Dog', 1,null,'Saranya Pet Haven',1,1),
    (2, 'Meena', 1, 'Persian', 'Cat', 1,null,'Surya Animal Shelter',2,2),
    (3, 'Krish', 3, 'Dachshund', 'Dog', 0,null,'Saranya Pet Haven',1,1);


INSERT INTO Shelters (ShelterID, Name, Location,City)
VALUES(1, 'Saranya Pet Haven', '789 Green Street','Chennai'),
    (2, 'Surya Animal Shelter', '234 Palm Avenue','Chennai');


INSERT INTO Donations (DonationID, DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
VALUES(1, 'Kiran Kumar', 'Cash', 150.75, NULL, '2024-02-27 09:30:00'),
    (2, 'Aishwarya Raj', 'Item', NULL, 'Pet Toys', '2024-02-28 14:45:00');

INSERT INTO Donations (DonationID, DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
VALUES (3, 'Saranya Pet Haven', 'Cash', 3500, NULL, '2024-02-28 01:30:00'),
	(4, 'Surya Animal Shelter', 'Cash', 1350, NULL, '2024-02-28 02:25:00');


INSERT INTO AdoptionEvents (EventID, EventName, EventDate, Location,City,OrganizerID)
VALUES(1, 'South Paws Adoption Day', '2024-03-15 12:00:00', 'Coconut Grove Park','Chennai',1),
    (2, 'Southern Tails Fair', '2024-04-10 10:00:00', 'Chennai Marina','Chennai',1);


INSERT INTO Participants (ParticipantID, ParticipantName, ParticipantType, EventID,City)
VALUES (1, 'Saranya Pet Haven', 'Shelter', 1,'Chennai'),
    (2, 'Karthik Raja', 'Adopter', 1,'Chennai'),
    (3, 'Surya Animal Shelter', 'Shelter', 2,'Chennai');


SELECT Name, Age, Breed, Type FROM Pets WHERE AvailableForAdoption = 1;

---6
SELECT Participants.ParticipantName, Participants.ParticipantType
FROM Participants
JOIN AdoptionEvents ON Participants.EventID = AdoptionEvents.EventID
WHERE AdoptionEvents.EventName = 'South Paws Adoption Day';

--7


CREATE PROCEDURE UpdateShelterInfo
    @ShelterID INT,
    @NewName VARCHAR(255),
    @NewLocation VARCHAR(255)
AS
BEGIN
    SET NOCOUNT ON;

    
    IF NOT EXISTS (SELECT 1 FROM Shelters WHERE ShelterID = @ShelterID)
    BEGIN
        PRINT 'Error: ShelterID does not exist.';
        RETURN;
    END


    UPDATE Shelters
    SET Name = @NewName,
        Location = @NewLocation
    WHERE ShelterID = @ShelterID;

    PRINT 'Shelter information updated successfully.';
END;



EXEC UpdateShelterInfo @ShelterID = 1, @NewName = 'Updated Shelter', @NewLocation = 'New Location';

---8

SELECT S.Name AS ShelterName, COALESCE(SUM(D.DonationAmount), 0) AS TotalDonationAmount FROM Shelters S LEFT JOIN Donations D ON S.Name = D.DonorName GROUP BY S.Name;

---9



SELECT Name, Age, Breed, Type FROM Pets WHERE OwnerID IS NULL;

---10

SELECT FORMAT(DonationDate, 'MMMM yyyy') AS MonthYear, COALESCE(SUM(DonationAmount), 0) AS TotalDonationAmount FROM Donations GROUP BY FORMAT(DonationDate, 'MMMM yyyy');

---11

SELECT DISTINCT Breed FROM Pets WHERE (Age BETWEEN 1 AND 3) OR (Age > 5);

---12

SELECT P.Name AS PetName, P.Age, P.Breed, P.Type, S.Name AS ShelterName FROM Pets P JOIN Shelters S ON P.ShelterName = S.Name WHERE P.AvailableForAdoption = 1;

---13

SELECT   S.Name AS ShelterName,COUNT(P.ParticipantID) AS TotalParticipants
FROM Participants P JOIN AdoptionEvents AE ON P.EventID = AE.EventID
JOIN Shelters S ON AE.OrganizerID = S.ShelterID WHERE S.City = 'Chennai' GROUP BY S.Name;

---14

SELECT DISTINCT Breed FROM Pets WHERE Age BETWEEN 1 AND 5;


---15

SELECT * FROM Pets WHERE OwnerID IS NULL;

---16

CREATE TABLE Adoptions (
    AdoptionID INT PRIMARY KEY,
    AdopterName VARCHAR(255),
    PetID INT,
    AdoptionDate DATETIME,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateOfBirth DATE,
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT P.Name AS PetName, U.UserName AS AdopterName FROM Adoptions A JOIN Pets P ON A.PetID = P.PetID JOIN Users U ON A.AdoptionID = U.UserID;

---17

SELECT S.Name AS ShelterName, COUNT(P.PetID) AS PetsAvailableForAdoption FROM Shelters S LEFT JOIN Pets P ON S.ShelterID = P.ShelterID AND P.AvailableForAdoption = 1 GROUP BY S.ShelterID, S.Name;

---18

SELECT A.PetID AS Pet1ID, B.PetID AS Pet2ID, A.Breed AS SharedBreed, A.ShelterID AS ShelterID FROM Pets A JOIN Pets B ON A.ShelterID = B.ShelterID AND A.PetID < B.PetID WHERE A.Breed = B.Breed;

---19

SELECT S.ShelterID AS ShelterID, S.Name AS ShelterName, AE.EventID AS EventID, AE.EventName AS EventName FROM Shelters S CROSS JOIN AdoptionEvents AE;

---20

SELECT TOP 1 S.ShelterID, S.Name AS ShelterName, COUNT(A.PetID) AS AdoptedPetsCount FROM Shelters S JOIN Pets A ON S.ShelterID = A.ShelterID  GROUP BY S.ShelterID, S.Name ORDER BY AdoptedPetsCount DESC;

