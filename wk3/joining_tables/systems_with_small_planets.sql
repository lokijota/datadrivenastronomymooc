Select s.radius as sun_radius, p.radius as planet_radius
From Star as s, Planet as p
Where s.kepler_id = p.kepler_id and s.radius/p.radius > 1
order by s.radius desc

