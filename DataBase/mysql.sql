/*Create DATABASE*/
CREATE DATABASE `Salaries`;
USE `Salaries`;

/*DROP TABLE  Salaries.Salaries_In_Egypt_at_2024;*/

/*Create table */
CREATE TABLE  IF NOT EXISTS Salaries.Salaries_In_Egypt_at_2024 (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Job_Title VARCHAR(255),
    Years_of_Experiences INT,
    Salary INT,
    Date_of_Salary DATE,
    Work_location VARCHAR(255),
    Work_Type VARCHAR(255),
    Work_Hour VARCHAR(255),
    City_of_Company_site VARCHAR(255)

);

