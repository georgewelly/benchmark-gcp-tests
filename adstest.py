from datetime import date, timedelta
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from keyfile import keyfile_dict  # your separate file with credentials dict

# Hardcode GA4 property

DEMENTIA_UK = "358899668"#grant connected
KEEN_LONDON = "448828434"#no grant
PROPERTY_ID = KEEN_LONDON  # replace with your GA4 property ID

# Auth
creds = service_account.Credentials.from_service_account_info(keyfile_dict)
client = BetaAnalyticsDataClient(credentials=creds)

# Date range: last 3 full days (excluding today)
end_date = date.today() - timedelta(days=1)
start_date = end_date - timedelta(days=2)

# GA4 request
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[
        Dimension(name="date"),
        Dimension(name="sessionGoogleAdsCustomerId")
    ],
    metrics=[Metric(name="sessions")],
    date_ranges=[DateRange(start_date=str(start_date), end_date=str(end_date))],
    keep_empty_rows=True
)

# Run and print
response = client.run_report(request)

print(f"GA4 data from {start_date} to {end_date}")
for row in response.rows:
    ga_date = row.dimension_values[0].value
    cust_id = row.dimension_values[1].value
    sessions = row.metric_values[0].value
    print(f"{ga_date}| {cust_id}  | {sessions}") 
