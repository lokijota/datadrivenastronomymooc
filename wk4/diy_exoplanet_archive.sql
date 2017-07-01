CREATE TABLE Star (
  kepler_id integer primary key,
  t_eff integer not null,
  radius float not null);
  
CREATE TABLE Planet (
  kepler_id integer references Star(kepler_id),
  koi_name varchar(20) primary key,
  kepler_name varchar(20),
  status varchar(20) not null,
  period float,
  radius float,
  t_eq integer);
  
COPY Star (kepler_id, t_eff, radius) FROM 'stars.csv' CSV;
COPY Planet FROM 'planets.csv' CSV;

