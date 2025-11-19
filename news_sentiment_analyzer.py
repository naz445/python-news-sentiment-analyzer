import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt


# ---------------------------------------------------------
#  Custom lexicon for rule-based sentiment scoring
# ---------------------------------------------------------

POSITIVE_TERMS = [
    "success", "growth", "improve", "recovery", "record",
    "gain", "boost", "strong", "optimistic", "progress",
    "win", "peace", "stability", "support", "benefit",
    "hope", "upgrade", "rise"
]

NEGATIVE_TERMS = [
    "crisis", "war", "conflict", "inflation", "recession",
    "loss", "drop", "decline", "strike", "attack",
    "risk", "fear", "collapse", "tension", "violence",
    "negative", "downturn", "cuts"
]


# ---------------------------------------------------------
#  Text preprocessing & sentiment classification
# ---------------------------------------------------------

def clean_headline(text: str) -> str:
    """Normalises spacing and prepares text for analysis."""
    return " ".join(text.split())


def score_sentiment(text: str) -> int:
    """
    Simple lexicon-based scoring system:
    +1 for each positive keyword
    -1 for each negative keyword
    """
    text = text.lower()
    score = 0

    for word in POSITIVE_TERMS:
        if word in text:
            score += 1

    for word in NEGATIVE_TERMS:
        if word in text:
            score -= 1

    return score


def sentiment_label(score: int) -> str:
    """Maps numeric score to a sentiment label."""
    if score > 0:
        return "Positive"
    if score < 0:
        return "Negative"
    return "Neutral"


def analyse_single_headline(text: str) -> tuple[str, int]:
    """Runs the complete sentiment pipeline for one headline."""
    cleaned = clean_headline(text)
    score = score_sentiment(cleaned)
    label = sentiment_label(score)
    return label, score


# ---------------------------------------------------------
#  Web scraping layer
# ---------------------------------------------------------

def extract_headlines(url: str, limit: int = 12) -> list[str]:
    """Fetches and extracts headline-like <h3> elements."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select("h3")

    headlines: list[str] = []
    for element in elements:
        text = element.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)
        if len(headlines) >= limit:
            break

    return headlines


def get_bbc_headlines(limit: int = 12) -> list[str]:
    """Returns BBC News headlines."""
    return extract_headlines("https://www.bbc.com/news", limit)


def get_guardian_headlines(limit: int = 12) -> list[str]:
    """Returns The Guardian UK headlines."""
    return extract_headlines("https://www.theguardian.com/uk", limit)


# ---------------------------------------------------------
#  Analysis & reporting
# ---------------------------------------------------------

def analyse_source(name: str, headlines: list[str]) -> dict:
    """Performs sentiment analysis for a single news outlet."""
    print(f"\n=== {name} ===")

    counter: Counter = Counter()
    details: list[tuple[str, str]] = []

    for idx, headline in enumerate(headlines, start=1):
        label, _score = analyse_single_headline(headline)
        counter[label] += 1
        details.append((label, headline))
        print(f"{idx:02}. [{label}] {headline}")

    return {
        "source": name,
        "total": len(headlines),
        "distribution": counter,
        "details": details
    }


def print_summary(results: list[dict]) -> None:
    """Prints aggregated sentiment summary across all sources."""
    print("\n\n=== Summary by Source ===")
    for result in results:
        name = result["source"]
        total = result["total"]
        dist: Counter = result["distribution"]

        print(f"\n{name}")
        print(f"  Total headlines: {total}")
        print(f"  Positive: {dist.get('Positive', 0)}")
        print(f"  Neutral : {dist.get('Neutral', 0)}")
        print(f"  Negative: {dist.get('Negative', 0)}")


# ---------------------------------------------------------
#  Visualisation
# ---------------------------------------------------------

def plot_sentiment_chart(results: list[dict]) -> None:
    """
    Generates a grouped bar chart comparing sentiment counts
    (Positive / Neutral / Negative) across all news sources.
    """
    if not results:
        return

    sources = []
    positives = []
    neutrals = []
    negatives = []

    for result in results:
        name = result["source"]
        dist: Counter = result["distribution"]

        sources.append(name)
        positives.append(dist.get("Positive", 0))
        neutrals.append(dist.get("Neutral", 0))
        negatives.append(dist.get("Negative", 0))

    x = range(len(sources))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar([i - width for i in x], positives, width=width, label="Positive")
    plt.bar(x, neutrals, width=width, label="Neutral")
    plt.bar([i + width for i in x], negatives, width=width, label="Negative")

    plt.xticks(list(x), sources)
    plt.ylabel("Number of headlines")
    plt.title("Sentiment Distribution by News Source")
    plt.legend()
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
#  Entry point
# ---------------------------------------------------------

def main() -> None:
    print("News Sentiment Analyzer")
    print("Scraping headlines and evaluating sentiment...\n")

    results: list[dict] = []

    try:
        bbc = get_bbc_headlines(limit=12)
        results.append(analyse_source("BBC News", bbc))
    except Exception as e:
        print("Error fetching BBC:", e)

    try:
        guardian = get_guardian_headlines(limit=12)
        results.append(analyse_source("The Guardian UK", guardian))
    except Exception as e:
        print("Error fetching The Guardian:", e)

    if results:
        print_summary(results)
        print("\nGenerating sentiment chart...")
        plot_sentiment_chart(results)
        print("\nAnalysis completed.")
    else:
        print("No data available — analysis skipped.")


if __name__ == "__main__":
    main()

   


   
