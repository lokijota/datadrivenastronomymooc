CREATE TABLE Planet (
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(15) UNIQUE NOT NULL,
  kepler_name VARchar(15) ,
  status varchar(20) NOT NULL,
  radius float NOT NULL
);

insert into Planet VALUES 
  (6862328, 'K00865.01', null, 'CANDIDATE', 119.021),
  (10187017, 'K00082.05', 'Kepler-102 b', 'CONFIRMED', 5.286),
  (10187017, 'K00082.04', 'Kepler-102 c', 'CONFIRMED', 7.071);
  
select * from Planet;


