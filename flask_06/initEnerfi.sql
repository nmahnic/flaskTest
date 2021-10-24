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
CREATE TABLE `user`
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(50) NOT NULL,
    `surname` VARCHAR(50) NOT NULL,
    `userName` VARCHAR(50) NOT NULL,
    `password` VARCHAR(50) NOT NULL,
    `mail` VARCHAR(80) NOT NULL,

    CONSTRAINT `PK_user` PRIMARY KEY  (`id`)
);

CREATE TABLE `meter`
(
    `meterID` INT NOT NULL AUTO_INCREMENT,
    `macAddress` VARCHAR(50),
    `ip` VARCHAR(50),
    `user_id_id` INT,
    `dum_id_id` INT,
    CONSTRAINT `PK_meter` PRIMARY KEY  (`meterID`)
);

CREATE TABLE `dum`
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id_id` INT,
    `name` VARCHAR(50),
    CONSTRAINT `PK_dum` PRIMARY KEY  (`id`)
);

CREATE TABLE `measure`
(
    `measureID` INT NOT NULL AUTO_INCREMENT,
    `dum_id_id` INT,
    `timeStamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `vrms` FLOAT,
    `irms` FLOAT,
    `activePower` FLOAT,
    `pf` FLOAT,
    `thd` FLOAT,
    `cosPhi` FLOAT,
    `freq_1st` FLOAT,
    `freq_2nd` FLOAT,
    `freq_3rd` FLOAT,
    `freq_4th` FLOAT,
    `freq_5th` FLOAT,
    `freq_6th` FLOAT,
    `freq_7th` FLOAT,
    `freq_8th` FLOAT,
    `freq_9th` FLOAT,
    `freq_10th` FLOAT,
    CONSTRAINT `PK_measureID` PRIMARY KEY  (`measureID`)
);

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
ALTER TABLE `meter` ADD CONSTRAINT `FK_meterid`
    FOREIGN KEY (`user_id_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE `meter` ADD CONSTRAINT `FK_meterDUMID`
    FOREIGN KEY (`dum_id_id`) REFERENCES `dum` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `dum` ADD CONSTRAINT `FK_dumid`
    FOREIGN KEY (`user_id_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `measure` ADD CONSTRAINT `FK_measureDUMID`
    FOREIGN KEY (`dum_id_id`) REFERENCES `dum` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;    

/*******************************************************************************
   Create Primary Key Unique Indexes
********************************************************************************/
                                    /* COMING SOON */

/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO `user` (`user_name`,`surname`,`userName`,`password`,`mail`) VALUES ('Nicolas','Mahnic','Mash','1234','nico.mahnic@gmail.com');
INSERT INTO `user` (`user_name`,`surname`,`userName`,`password`,`mail`) VALUES ('Juan Manuel','Deseta','Juanma','1234','juanmanueldeseta@gmail.com');
INSERT INTO `user` (`user_name`,`surname`,`userName`,`password`,`mail`) VALUES ('Juan Ignacio','Figueiras','Juani','1234','juanifigueiras@gmail.com');
INSERT INTO `user` (`user_name`,`surname`,`userName`,`password`,`mail`) VALUES ('Eric','Ortiz','Ericovich','1234','eric95ortiz@gmail.com');
INSERT INTO `user` (`user_name`,`surname`,`userName`,`password`,`mail`) VALUES ('Tiago','Monteiro','TiagoMedidas','1234','tmonteiro@frba.utn.edu.ar');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (1, 'Heladera');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (1, 'Lavarropas');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (2, 'Lavarropas');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (3, 'Lavarropas');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (4, 'Zapatilla ');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (5, 'Lavarropas');
INSERT INTO `dum` (`user_id_id`,`name`) VALUES (5, 'Computadora');
INSERT INTO `meter` (`macAddress`,`ip`,`user_id_id`,`dum_id_id`) VALUES ('84-D8-1B-0C-5B-C1','192.168.0.2',1,1);
INSERT INTO `meter` (`macAddress`,`ip`,`user_id_id`,`dum_id_id`) VALUES ('B0-B2-8F-1D-4D-02','192.168.0.3',1,2);
INSERT INTO `measure` (
        `dum_id_id`,`vrms`,`irms`,
        `activePower`,`pf`,`thd`,`cosPhi`,
        `freq_1st`,`freq_2nd`,`freq_3rd`,`freq_4th`,
        `freq_5th`,`freq_6th`,`freq_7th`,`freq_8th`,
        `freq_9th`,`freq_10th`
    ) VALUES (
        1,1.1,1.2,
        1.3,0.9,0.8,0.1,
        1.1 , 1.2, 1.3, 1.4,
        1.5 , 1.6, 1.7, 1.8,
        1.9 , 1.01
    );