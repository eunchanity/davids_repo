--QUESTION 1:
select state, year, sum(freq)
from name_freq
group by state, year 
limit 10;

--QUESTION 2:
select name, sum(freq) 
from name_freq
where year = 2000
group by name
having sum(freq) > 1000
limit 10;

--QUESTION 3:
select state, name, sum(freq)
from name_freq
where year = 2000
group by state, name 
having sum(freq) > 1000
limit 10;

--QUESTION 4:
select count(distinct state)
from name_freq;
select count(distinct state)
from region;
select distinct(nf.state)
from name_freq nf
where nf.state not in
(select r.state from region r);

--QUESTION 5:
select name
from name_freq nf left join region r on (nf.state = r.state)
where r.region = 'Pacific' and gender = 'M'
order by freq desc 
limit 1;

--QUESTION 6:
with noah_table as (select state, sum(freq) as Noah
from name_freq
where year = 2000 and name = 'Noah'
group by state),
total_names as (select state, sum(freq) as total
from name_freq
where year = 2000
group by state)
select noah_table.state, (cast(noah_table.noah as decimal)/total_names.total)*100
from noah_table
join total_names on total_names.state = noah_table.state;