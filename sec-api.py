# SEC EDGAR API. 
# I want to pull the most recent line item values from SEC filings. 
# https://developer.edgar-online.com/docs
# 
# "Today I can go online and there are all these automated Ben Graham 12 screens, 
# I hit them, they're on the 12 screens for me two seconds later, the companies 
# pop up and the question is, if I can pull that up, what makes you think that 
# running these screens is going to give you a differential advantage?
# I am shocked at how much of traditional value investing is just running screens."

import requests
import pandas as pd

# https://data.sec.gov/api/xbrl/companyconcept/[CIK]/us-gaap/[Tag].json

MCO_cash = requests.get("https://data.sec.gov/api/xbrl/companyconcept/CIK0001059556/us-gaap/CashAndCashEquivalentsAtCarryingValue.json", headers=headers)
MCO_revenue = requests.get("https://data.sec.gov/api/xbrl/companyconcept/CIK0001059556/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax.json", headers=headers)
