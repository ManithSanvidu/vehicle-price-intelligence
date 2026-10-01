# Vehicle Price Intelligence — Data Dictionary

This dictionary is based on the uploaded dataset and the group's initial report. The report confirms that **Price is the target and is expressed in LKR lakhs**, where 1 lakh = LKR 100,000. 

| Column | Meaning / role | Observed dtype | Observed quality / values | EDA note |
|---|---|---|---|---|
| Unnamed: 0 | Raw row/index identifier | int64 | 9,784 unique values; 4 duplicated IDs | Exclude from prediction after confirming it is only an index/identifier |
| Brand | Vehicle brand/manufacturer | object | 50 distinct brands | Moderate cardinality |
| Model | Vehicle model name | object | 1,554 distinct models | High cardinality; 914 models occur once |
| YOM | Year of manufacture | float64 | 1956–2024; 12 missing | Inspect unusual years and missing values |
| Engine (cc) | Engine capacity in cubic centimeters | float64 | 573–4,800 cc; 9 missing | Inspect extreme values |
| Gear | Transmission/gear type | object | Automatic, Manual | Binary |
| Fuel Type | Vehicle fuel/power type | object | Petrol, Hybrid, Diesel, Electric | Low cardinality |
| Millage(KM) | Recorded vehicle mileage in kilometres (raw spelling preserved) | float64 | 11,000–759,000 km; 9 missing | Perfectly linearly related to YOM in supplied file; investigate before modeling |
| Town | Town/location associated with listing | object | 107 towns | Moderate cardinality |
| Date | Listing date | object | 65 distinct dates from 2024-12-03 to 2025-02-05 | Convert to datetime for EDA |
| Leasing | Leasing status | object | No Leasing, Ongoing Lease | Binary |
| Condition | Vehicle condition | object | USED, NEW | Binary; heavily dominated by USED |
| AIR CONDITION | Air conditioning availability | object | Available, Not_Available | Binary |
| POWER STEERING | Power steering availability | object | Available, Not_Available | Binary |
| POWER MIRROR | Power mirror availability | object | Available, Not_Available | Binary |
| POWER WINDOW | Power window availability | object | Available, Not_Available | Binary |
| Price | Listed vehicle price | float64 | 2.65–790.00 LKR lakhs; 23 missing | Target for supervised regression; 1 lakh = LKR 100,000 |

## Important observations
- `Price` is the supervised regression target.
- `Model` is high-cardinality (1,554 distinct values).
- `Town` has 107 distinct values.
- `Unnamed: 0` appears to be a raw row/index identifier; confirm with the stakeholder before treating it as an identifier.
- The raw spelling `Millage(KM)` is preserved in this dictionary. A later preprocessing stage can rename it to `Mileage_KM`.
