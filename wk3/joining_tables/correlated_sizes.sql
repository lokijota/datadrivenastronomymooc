Select p.koi_name, p.radius, s.radius
From Star s INNER JOIN Planet p USING(kepler_id)
Where s.kepler_id IN (
  Select kepler_id
  From Star
  Order by radius desc
  Limit 5)

