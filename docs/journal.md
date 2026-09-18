# decisions log

## Thursday, 3rd September 2026
I Choose the H&M dataset from Kaggle. Then 
ownloaded articles and customers csv, skipped transactions for now since its 3GB and I'm low on data. Looked at the columns then built the schema in Postgres. Used BIGINT for article_id since the codes are big.

Loaded both files in. Got an error on FN and Active, they came in as 1.0 instead of a plain number, so I changed them to NUMERIC and it worked.

## Thursday 17 September 2026
I Downloaded the transactions csv. Created a table in postgres with foreign keys 
referencing customers and articles. Then extracted the full year 2019 into its own 
table.  

## Friday, 18 September 2026
I found ~9.6% duplicate rows (same customer, article, date, sales channel). 
Checked the H&M's official dataset documentation which  confirmed duplicate rows 
represent  repeat purchases of the same item. So they were not data errors. Filled null ages with median (32) since mean was pulled up by 
older outliers; filled null club_member_status with "Unknown". Lastly Converted t_dat to datetime and age to int.