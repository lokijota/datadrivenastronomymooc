select kepler_name, radius
from Planet
where status = 'CONFIRMED' and kepler_name is not null
and radius between 1 and 3


