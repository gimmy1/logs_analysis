# About
Worked with data with fields representing information that a web server would record, such as HTTP status codes and URL paths.

# Mission
Build an informative summary by exploring the database which has over a million rows. Constructed complex SQL queries to draw business conclusions from the data.


# Required software
1. Python
2. Vagrant
3. VirtualBox
4. PostgreSQL

# Set-up
1. Clone Repository
2. Activate Vagrant and Virtual Machine
- `vagrant up`
- `vagrant ssh`
3. Load data and then psql into file & then database.
- `psql -d news -f newsdata.sql`
- `psql -d news`
4. Create Views

```
 Create View reqs As Select Cast(time As date) As date, Count(*) as total, Count(Case When status = '404 NOT FOUND' Then 1 End) as errors from log Group By date Order By date;
```

```
Create View errs As Select reqs.date,
reqs.errors::float/reqs.total * 100 as percentage From reqs;
```

5. Run `python logs.py`

# Results
1. What are the 3 most popular articles of All-time
```
 Candidate is jerk, alleges rival - 338647 views
 Bears love berries, alleges bear - 253801 views
 Bad things gone, say good people - 170098 views
```

2. Who are most popular authors? Rank by views
```
  Ursula La Multa - 507594 views
  Rudolf von Treppenwitz - 423457 views
  Anonymous Contributor - 170098 views
  Markoff Chaney - 84557 views
```


3. On what day did requests lead to errors greater than 1%?
```
July 17, 2016 - 2.26 % errors

```
