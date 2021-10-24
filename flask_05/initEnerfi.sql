/*******************************************************************************
   Enerfi Database - Version 0.1
   Script: initEnerfi.sql
   Description: Creates and populates the Enerfi database.
   DB Server: MySql
   Author: Nicolas Mahnic
   License: 
********************************************************************************/

/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS Enerfi;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE Enerfi;

USE Enerfi;


/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE `User`
(
    `UserID` INT NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(50) NOT NULL,
    `Surname` VARCHAR(50) NOT NULL,
    `UserName` VARCHAR(50) NOT NULL,
    `Password` VARCHAR(50) NOT NULL,
    `Mail` VARCHAR(80) NOT NULL,

    CONSTRAINT `PK_User` PRIMARY KEY  (`UserID`)
);

CREATE TABLE `Meter`
(
    `MeterID` INT NOT NULL AUTO_INCREMENT,
    `MAC_Address` VARCHAR(50),
    `IP` VARCHAR(50),
    `UserID` INT,
    `DUMID` INT,
    CONSTRAINT `PK_Meter` PRIMARY KEY  (`MeterID`)
);

CREATE TABLE `DUM`
(
    `DUMID` INT NOT NULL AUTO_INCREMENT,
    `UserID` INT,
    `Name` VARCHAR(50),
    CONSTRAINT `PK_DUM` PRIMARY KEY  (`DUMID`)
);

CREATE TABLE `Measure`
(
    `MeasureID` INT NOT NULL AUTO_INCREMENT,
    `DUMID` INT,
    `TimeStamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Vrms` FLOAT,
    `Irms` FLOAT,
    `ActivePower` FLOAT,
    `PF` FLOAT,
    `THD` FLOAT,
    `COS_PHI` FLOAT,
    `Freq_1st` FLOAT,
    `Freq_2nd` FLOAT,
    `Freq_3rd` FLOAT,
    `Freq_4th` FLOAT,
    `Freq_5th` FLOAT,
    `Freq_6th` FLOAT,
    `Freq_7th` FLOAT,
    `Freq_8th` FLOAT,
    `Freq_9th` FLOAT,
    `Freq_10th` FLOAT,
    CONSTRAINT `PK_MeasureID` PRIMARY KEY  (`MeasureID`)
);

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
ALTER TABLE `Meter` ADD CONSTRAINT `FK_MeterUserID`
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `Meter` ADD CONSTRAINT `FK_MeterDUMID`
    FOREIGN KEY (`DUMID`) REFERENCES `DUM` (`DUMID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `DUM` ADD CONSTRAINT `FK_DUMUserID`
    FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `Measure` ADD CONSTRAINT `FK_MeasureDUMID`
    FOREIGN KEY (`DUMID`) REFERENCES `DUM` (`DUMID`) ON DELETE NO ACTION ON UPDATE NO ACTION;    

/*******************************************************************************
   Create Primary Key Unique Indexes
********************************************************************************/
                                    /* COMING SOON */

/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO `User` (`Name`,`Surname`,`UserName`,`Password`,`Mail`) VALUES ('Nicolas','Mahnic','Mash','1234','nico.mahnic@gmail.com');
INSERT INTO `User` (`Name`,`Surname`,`UserName`,`Password`,`Mail`) VALUES ('Juan Manuel','Deseta','Juanma','1234','juanmanueldeseta@gmail.com');
INSERT INTO `User` (`Name`,`Surname`,`UserName`,`Password`,`Mail`) VALUES ('Juan Ignacio','Figueiras','Juani','1234','juanifigueiras@gmail.com');
INSERT INTO `User` (`Name`,`Surname`,`UserName`,`Password`,`Mail`) VALUES ('Eric','Ortiz','Ericovich','1234','eric95ortiz@gmail.com');
INSERT INTO `User` (`Name`,`Surname`,`UserName`,`Password`,`Mail`) VALUES ('Tiago','Monteiro','TiagoMedidas','1234','tmonteiro@frba.utn.edu.ar');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (1, 'Heladera');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (1, 'Lavarropas');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (2, 'Lavarropas');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (3, 'Lavarropas');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (4, 'Zapatilla ');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (5, 'Lavarropas');
INSERT INTO `DUM` (`UserID`,`Name`) VALUES (5, 'Computadora');
INSERT INTO `Meter` (`MAC_Address`,`IP`,`UserID`,`DUMID`) VALUES ('84-D8-1B-0C-5B-C1','192.168.0.2',1,1);
INSERT INTO `Meter` (`MAC_Address`,`IP`,`UserID`,`DUMID`) VALUES ('B0-B2-8F-1D-4D-02','192.168.0.3',1,2);
INSERT INTO `Measure` (
        `DUMID`,`Vrms`,`Irms`,
        `ActivePower`,`PF`,`THD`,`COS_PHI`,
        `Freq_1st`,`Freq_2nd`,`Freq_3rd`,`Freq_4th`,
        `Freq_5th`,`Freq_6th`,`Freq_7th`,`Freq_8th`,
        `Freq_9th`,`Freq_10th`
    ) VALUES (
        1,1.1,1.2,
        1.3,0.9,0.8,0.1,
        1.1 , 1.2, 1.3, 1.4,
        1.5 , 1.6, 1.7, 1.8,
        1.9 , 1.01
    );