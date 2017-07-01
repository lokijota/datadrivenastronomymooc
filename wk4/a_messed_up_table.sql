select * from Planet;
delete from Planet Where radius < 0;
update Planet Set kepler_name = null where status != 'CONFIRMED';
select * from Planet;

