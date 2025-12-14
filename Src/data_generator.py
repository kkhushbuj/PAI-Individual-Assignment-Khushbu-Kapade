import random
from datetime import datetime, timedelta

COUNTRIES = ["UK", "USA", "France", "Germany", "India", "Japan", "Canada"]
METRICS = [
    "covid_cases",
    "covid_deaths",
    "vaccination_rate",
    "mental_health_reports",
    "hospital_admissions"
]

def generate_synthetic_record():
    start = datetime(2020, 1, 1)
    end = datetime(2024, 12, 31)
    delta = (end - start).days
    dt = start + timedelta(days=random.randint(0, delta))

    metric = random.choice(METRICS)
    if metric == "covid_cases":
        value = random.randint(0, 50000)
    elif metric == "covid_deaths":
        value = random.randint(0, 2000)
    elif metric == "vaccination_rate":
        value = round(random.uniform(0, 100), 2)
    else:
        value = random.randint(0, 15000)

    if random.random() < 0.03:
        value = None

    return {
        "country": random.choice(COUNTRIES),
        "date": dt.strftime("%Y-%m-%d"),
        "metric": metric,
        "value": value
    }

def generate_dataset(n=1000):
    return [generate_synthetic_record() for _ in range(n)]
