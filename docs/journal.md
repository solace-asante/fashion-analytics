# decisions log

## Thursday, 3rd September 2026
I Choose the H&M dataset from Kaggle. Then 
ownloaded articles and customers csv, skipped transactions for now since its 3GB and I'm low on data. Looked at the columns then built the schema in Postgres. Used BIGINT for article_id since the codes are big.

Loaded both files in. Got an error on FN and Active, they came in as 1.0 instead of a plain number, so I changed them to NUMERIC and it worked.