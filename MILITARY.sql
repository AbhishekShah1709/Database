drop database if exists MILITARY;
create database MILITARY;
use MILITARY;

drop table if exists EQUIPMENTCOUNT;
drop table if exists EQUIPMENTS;
drop table if exists BASE;
drop table if exists SOLDIER;
drop table if exists CONTACT;
drop table if exists CONTACTINFO;
drop table if exists SOLDIERSALARY;
drop table if exists DUTY;

create table EQUIPMENTS
(
    WeaponId INT NOT NULL
    AUTO_INCREMENT,
    WeaponName VARCHAR
    (50) NOT NULL,
    Price INT NOT NULL,
    PRIMARY KEY
    (WeaponId)
);

    create table BASE
    (
        BaseId INT NOT NULL
        AUTO_INCREMENT,
    BaseLocation VARCHAR
        (100) NOT NULL,
    PRIMARY KEY
        (BaseId)
);

        create table EQUIPMENTCOUNT
        (
            WeaponId INT NOT NULL,
            BaseId INT NOT NULL,
            Count INT NOT NULL,
            PRIMARY KEY (WeaponId,BaseId),
            FOREIGN KEY (BaseId) REFERENCES BASE(BaseId),
            FOREIGN KEY (WeaponId) REFERENCES EQUIPMENTS(WeaponId)
        );

        create table SOLDIERSALARY
        (
            Position VARCHAR(30) NOT NULL,
            Salary INT NOT NULL,
            PRIMARY KEY (Position)
        );

        create table DUTY
        (
            DutyId INT NOT NULL
            AUTO_INCREMENT,
    DutyType VARCHAR
            (40) NOT NULL,
    PRIMARY KEY
            (DutyId)
);

            create table SOLDIER
            (
                SoldierId INT NOT NULL
                AUTO_INCREMENT,
    Fname VARCHAR
                (30) NOT NULL,
    Mname VARCHAR
                (30) NOT NULL,
    Lname VARCHAR
                (30) NOT NULL,
        Gender ENUM
                ('F','M') NOT NULL,

    DOB DATE NOT NULL,
    JoiningDate DATE NOT NULL,
    Category INT NOT NULL,
    Position VARCHAR
                (30) NOT NULL,
    BaseId INT NOT NULL,
    HeadId INT NOT NULL,
    DutyId INT NOT NULL,
    PRIMARY KEY
                (SoldierId),
    FOREIGN KEY
                (HeadId) REFERENCES SOLDIER
                (SoldierId),
    FOREIGN KEY
                (BaseId) REFERENCES BASE
                (BaseId),
    FOREIGN KEY
                (Position) REFERENCES SOLDIERSALARY
                (Position),
    FOREIGN KEY
                (DutyId) REFERENCES DUTY
                (DutyId)
);


                create table CONTACTINFO
                (
                    ContactNumber VARCHAR(10) NOT NULL,
                    Parent VARCHAR(30) NOT NULL,
                    StreetAddress VARCHAR(70) NOT NULL,
                    Pincode INT(10) NOT NULL,
                    City VARCHAR(30) NOT NULL,
                    Stat VARCHAR(30) NOT NULL,
                    PRIMARY KEY (ContactNumber)
                );

                create table CONTACT
                (
                    SoldierId INT NOT NULL,
                    ContactNumber VARCHAR(10) NOT NULL,
                    PRIMARY KEY (SoldierId),
                    FOREIGN KEY (SoldierId) REFERENCES SOLDIER(SoldierId),
                    FOREIGN KEY (ContactNumber) REFERENCES CONTACTINFO(ContactNumber)
                );


-- ALTER table CONTACT
-- ADD CONSTRAINT Mob CHECK (ContactNumber >= 1111111111 AND ContactNumber <= 9999999999);

-- INSERT INTO CONTACTINFO
--     (Parent, StreetAddress, Pincode, City, Stat, ContactNumber)
-- VALUES
--     ("ABCD", "AAA", 123, "Abx", "123", 100002)
-- ;