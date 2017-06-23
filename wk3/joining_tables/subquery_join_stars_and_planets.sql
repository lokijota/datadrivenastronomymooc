Select round(avg(p.t_eq),1), MIN(t_eff), MAX(t_eff)
From Star s INNER JOIN Planet p USING(kepler_id)
Where t_eff > (Select avg(t_eff) from Star)

