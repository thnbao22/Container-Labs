CREATE DATABASE TestDB;
USE TestDB;
CREATE TABLE tblStudent (
		studentID INT PRIMARY KEY AUTO_INCREMENT,
		studentName NVARCHAR(100),
		age int CHECK(age > 0)
);

SELECT * FROM tblStudent;
INSERT INTO tblStudent(studentName, age)
VALUES('Charles Thien', 19);