# H&M Fashion Retail Analysis 2019

An analysis of H&M purchase data from 2019, built with PostgreSQL, pandas and seaborn. I chose six business questions myself to practise answering them with data. They are not from Kaggle or H&M.

## Data

The data comes from the [H&M Personalized Fashion Recommendations dataset on Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data). The original file has about 31.8 million purchases. I use the 16,396,930 purchases from 2019, the only complete calendar year.

Prices are scaled, so all revenue figures here are relative, not real currency. The data is used for non-commercial learning and is not stored in this repo. This project is independent of H&M.

## Key findings

### 1. Best and worst selling

Garment Upper body leads, with 6.5M purchases and 38.2% of revenue. Its lead comes from volume, because its average price is lower than Garment Full body and Bags. Accessories has more purchases than Shoes, 816K against 400K, but Shoes earns more revenue, 15.6K against 12.9K. 12 of the top 20 products by revenue are Garment Lower body. About 5.8% of products sold exactly once, so I did not rank the worst sellers.

Notebook: `notebooks/02_best_selling.ipynb`

![Best and worst selling](reports/best_selling_dashboard.png)

### 2. Seasonal patterns

Swimwear is the most seasonal category. June holds 23.3% of its yearly revenue, about 2.8 times an average month, and it falls to near 1% from September to December. Garment Full body peaks in June at 14.8%. Garment Upper body is mildly seasonal, peaking in September at 11.4%. Underwear is flat.

Notebook: `notebooks/03_seasonal_patterns.ipynb`

![Seasonal profile](reports/seasonal_profile.png)

### 3. Pricing within category

Socks and Tights has the lowest median price, about 0.012. Shoes, Garment Full body and Bags are highest at about 0.034, with Garment Lower body just below. Garment Upper body has the most uneven prices of the large categories, with a long tail of expensive purchases. Items, Bags and Swimwear have narrow price ranges, though Swimwear also has many unusually cheap purchases. Categories with fewer than 1,000 purchases are left out.

Notebook: `notebooks/04_price.ipynb`

![Price distribution by category](reports/goal3_price_boxplot.png)

### 4. Age

Garment Upper body is the top category in every age band. Its share of revenue rises with age, from about 37% under 45 to 47.8% for 65+. Customers under 25 lean most toward Swimwear. The bands from 25 to 64 lean only slightly.

Notebook: `notebooks/05_age.ipynb`

![Category preference by age band](reports/age_preference_index.png)

### 5. Membership status

ACTIVE makes up about 97.6% of purchases, so the small groups are less reliable. The median price is identical in all four groups, 0.025407, and the mean is 6 to 9% higher in the three smaller groups. LEFT CLUB and Unknown lean toward Shoes, and PRE-CREATE toward Swimwear.

Notebook: `notebooks/06_membership.ipynb`

![Category preference by membership status](reports/membership_preference_index.png)

### 6. Colour

The data has 50 colour names. Black is the most common, with 34.6% of purchases, and it takes 13 colours to reach 80% of all purchases.

Notebook: `notebooks/07_color.ipynb`

![Top 10 colours](reports/top_colours.png)

## How to reproduce

1. Download the dataset from Kaggle into `data/raw/`.
2. Install the packages with `pip install -r requirements.txt`.
3. Create the database with `sql/schema.sql` and load the raw files.
4. Add a `.env` file with your database credentials.
5. Run `python scripts/extract_data.py` to create `data/processed/hm_2019.csv`.
6. Run `notebooks/01_cleaning_data.ipynb` to create `merged_cleaned_2019.csv`.
7. Run the other notebooks in order.

## Limitations

Only 2019 is covered, so the patterns can't be separated from one-off events. Each row is a purchase, not a customer, so frequent buyers count many times. Age and membership are customer attributes, not necessarily their values at purchase time. Price is per purchase, so price spreads inside a category mix different products and possible discounts. About 0.6% of product names appear in more than one category.

## Author

Built by Solace Asante. https://github.com/solace-asante