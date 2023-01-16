use db;

CREATE TABLE Garden(
    
    TumbuhanID int NOT NULL AUTO_INCREMENT,
    Nama_Tumbuhan varchar(50) NOT NULL,
    jumlah_air int NOT NULL,
    jumlah_pupuk int NOT NULL,
    Status_tumbuh varchar(50) NOT NULL,
    PRIMARY KEY(TumbuhanID)
);

INSERT INTO Garden(Nama_Tumbuhan, jumlah_air, jumlah_pupuk,Status_tumbuh)
VALUES("Anggrek",2, 3 ,"Berbunga" ),("Mawar", 1, 4, "Tanaman Kecil"), ("Melati", 3, 1, "Tunas")