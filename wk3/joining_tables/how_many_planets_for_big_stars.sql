Select s.radius, count(s.kepler_id) as count
FROM Star as s, Planet as p
Where s.kepler_id = p.kepler_id and s.radius > 1
Group by s.kepler_id
Having count(s.kepler_id) > 1
Order by s.radius desc

