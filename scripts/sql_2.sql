select sum(freq), state, year 
from name_freq 
where name = 'Kate' and state = 'CA' 
group by state, year

select sum(freq), state, year 
from name_freq 
where name = 'Kate' and state = 'CA' 
group by state, year 
order by sum(freq) desc limit 1

select name, max(freq)
from name_freq left join region on (name_freq.state = region.state)
where gender = 'M' and year = 2000 and region = 'South'
group by name
order by max(freq) desc limit 1

select name, max(freq)
from name_freq left join region on (name_freq.state = region.state)
where gender = 'F' and year = 2000 and region = 'South'
group by name
order by max(freq) desc limit 1

select count(distinct name), state
from name_freq
where year = 2000
group by state
order by count(distinct name) desc limit 1

select count(distinct name), region
from name_freq left join region on (name_freq.state = region.state)
where year = 2000
group by region
order by count(distinct name) desc limit 1

select sum(freq), state 
from name_freq
where year between 2000 and 2010
group by state

select distinct name_freq.state, region 
from name_freq left join region on (name_freq.state = region.state)
where region is NULL