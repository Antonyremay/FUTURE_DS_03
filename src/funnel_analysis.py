import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "bank_marketing",
    "bank-additional",
    "bank-additional",
    "bank-additional-full.csv"
)


OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH, sep=";")

df["converted"] = df["y"].map({"yes": 1, "no": 0})

funnel_summary = {
    "Total Leads": len(df),
    "Converted Customers": df["converted"].sum(),
    "Overall Conversion Rate": df["converted"].mean()
}

conversion_by_channel = (
    df.groupby("contact")["converted"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
conversion_by_channel.plot(kind="bar")
plt.title("Conversion Rate by Channel")
plt.ylabel("Conversion Rate")
plt.xlabel("Channel")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "conversion_by_channel.png"))
plt.close()

df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 25, 35, 45, 55, 65, 100],
    labels=["18–25", "26–35", "36–45", "46–55", "56–65", "65+"]
)

conversion_by_age = df.groupby("age_group")["converted"].mean()

plt.figure(figsize=(8, 5))
conversion_by_age.plot(kind="bar")
plt.title("Conversion Rate by Age Group")
plt.ylabel("Conversion Rate")
plt.xlabel("Age Group")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "conversion_by_age.png"))
plt.close()

dropoff_by_campaign = (
    df.groupby("campaign")["converted"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(9, 5))
dropoff_by_campaign.plot()
plt.title("Conversion Drop-off by Campaign Contacts")
plt.xlabel("Number of Contacts")
plt.ylabel("Conversion Rate")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "dropoff_by_campaign.png"))
plt.close()

summary_df = pd.DataFrame({
    "Metric": [
        "Total Leads",
        "Converted Customers",
        "Overall Conversion Rate",
        "Best Channel",
        "Best Age Group"
    ],
    "Value": [
        funnel_summary["Total Leads"],
        funnel_summary["Converted Customers"],
        round(funnel_summary["Overall Conversion Rate"], 4),
        conversion_by_channel.idxmax(),
        conversion_by_age.idxmax()
    ]
})

summary_df.to_csv(
    os.path.join(OUTPUT_DIR, "summary_metrics.csv"),
    index=False
)

print("Funnel analysis completed successfully.")
print("Outputs saved to:", OUTPUT_DIR)
