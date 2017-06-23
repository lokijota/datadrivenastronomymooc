Select s.kepler_id, s.t_eff, s.radius
From Star s LEFT JOIN Planet p USING(kepler_id)
Where koi_name is null
Order by s.t_eff Desc

