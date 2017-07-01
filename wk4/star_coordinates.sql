alter table Star
  add column ra float,
  add column decl float;
  
  \d Star

delete from Star;
COPY Star FROM 'stars_full.csv' CSV

