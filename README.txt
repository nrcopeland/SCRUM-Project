ApexPalate.mp4 is the demo of the project.
How to recreate the database and formatted json from scratch.
-Download review.json and business.json
-Download or copy/paste review.py and business.py
-run those to create review.csv and business.csv
-run the following lines in the command line

sqlite3 project.db
.mode csv
create table business(id string, name string, state string, stars double, review_count int, is_open bool, type string);
 .import business.csv business;
‘shave off all the tuples that aren’t closed or in our 6 states’
create table smallbusiness as select id, name, state, stars, review_count, type from business where is_open = 0 and type like '%restaurant%' and (state like 'AZ' or state like 'NC' or state like 'NV' or state like 'OH' or state like 'ON' or state like 'PA');
‘now export the id and type columns as csv so we can clean up the type column’
.headers on
.mode csv
.output data.csv
select id, type from smallbusiness;
‘this gives me a data.csv file, I used regex like this [A-Za-z,\&()\/\-[:space:]]*pizza[A-Za-z,\&()\/\-[:space:]]*
but I don’t think it’s cheating to say we used OpenRefine. Then import back into sqlite’
create table cleantype(id string, type string);
.import data.csv cleantype
‘combine cleantype and smallbusiness’
create table biz as (select b.id, b.name, b.state, b.avg_stars, b.review_count, c.type from smallbusiness b, cleantype c where b.id=c.id);
‘now we create the review table, the big boy’
create table review(bid string, stars double, review_date date, review string);
‘connect the text of the reviews to the biz info, this took my computer a couple of hours to finish’
create table finalboss as (select b.state, b.type, b.avg_stars, b.name, r.stars , r.review_date, r.review from biz b, review r where r.bid=b.id);
‘now we export into csv and then run another python script to format it into json’
.output info.csv
SELECT type, avg_stars, name, stars, review_date, review FROM finalboss WHERE state=’AZ’;
‘Repeat for each state, NV, NC, ON, OH, PA
‘Exit out of sqlite3, download defaultdict.py and run’ 
python3 defaultdict.py | cat >> info.json
‘it still needs to be slightly altered before D3 will take it, mainly adding something about ‘flare’ to the top and probably renamed’ info.json 

  5 json files by state.  type, avg_stars, name, stars, review_date, review

