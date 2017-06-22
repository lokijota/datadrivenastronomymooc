Select kepler_id, count(kepler_id)
From Planet
group by kepler_id
having count(kepler_id) > 1
order by count(kepler_id) desc

