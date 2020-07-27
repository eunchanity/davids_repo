-- How many babies were born in each of the six regions?
select clean_region, sum(frequency)
from (select case when region.region = 'New_England' then 'New England' 
		else region end as clean_region, name_freq.freq as frequency
		from name_freq left join region on (name_freq.state = region.state)) as clean_data
group by clean_region

-- or
with clean_data as 
(select case when region.region = 'New_England' then 'New England' 
		else region end as clean_region, name_freq.freq as frequency
		from name_freq left join region on (name_freq.state = region.state))

select clean_region, sum(frequency) from clean_data group by clean_region

-- dummy variables
select clean_region, sum(frequency),
		case when clean_region = 'Midwest' then 1 else 0 end as midwest_dummy,
		case when clean_region = 'South' then 1 else 0 end as south_dummy
from (select case when region.region = 'New_England' then 'New England' 
		else region end as clean_region, name_freq.freq as frequency
		from name_freq left join region on (name_freq.state = region.state)) as clean_data
group by clean_region


-- Rank the most popular androgynous names in 2000
select name, sum(freq), count(distinct gender) as num_genders
from name_freq
where year = 2000
group by name
having count(distinct gender) = 2 
order by sum(freq) desc
limit 10


-- Which state has the highest percent of John’s in 2000?
select state_num_johns.state, num_johns * 100.0 / num_names as pct_johns

from 
(select state, freq as num_johns
from name_freq nf 
where name = 'John' and year = 2000) as state_num_johns

left join 
(select state, sum(freq) as num_names
from name_freq nf 
where year = 2000
group by state) as state_num_names
on state_num_johns.state = state_num_names.state
order by pct_johns desc
limit 2



-- Show the top 3 girl names for each state in the year 2000
with popular_girl_names as (select state, name, freq,
		rank() over(partition by state order by freq desc) as popularity
from
(select * from name_freq nf where year = 2000 and gender = 'F') as mytable)

select * from popular_girl_names where popularity <= 3