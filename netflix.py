import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles 2.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.isna().sum())

#cleaning
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
titles_per_year = df["year_added"].value_counts().sort_index()
df["country"] = df["country"].fillna("Unknown")

df["main_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0])

# Q1: How has Netflix’s content library evolved over time?

plt.figure()
plt.plot(titles_per_year.index, titles_per_year.values)
plt.title("Netflix Content Added Over Time")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


# Q2: Movies vs TV Shows

type_counts = df["type"].value_counts()
print(type_counts)

plt.figure()
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# Q3: Which countries produce the most Netflix content?

country_df = df.assign(
    country=df["country"].str.split(", ")
).explode("country")

top_countries = country_df["country"].value_counts().head(10)
print(top_countries)

plt.figure()
top_countries.plot(kind="bar")
plt.title("Top 10 Content-Producing Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Q4: What genres dominate Netflix’s catalogue?

top_genres = df["main_genre"].value_counts().head(10)
print(top_genres)

plt.figure()
top_genres.plot(kind="bar")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Q5: Does Netflix focus on recent content?

plt.figure()
plt.hist(df["release_year"], bins=20)
plt.title("Distribution of Release Years on Netflix")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()