# News Sentiment Analyzer

A Python-based sentiment analysis tool that collects live headlines from leading UK news outlets (BBC News and The Guardian) and determines sentiment using a custom rule-based NLP engine.  
The tool performs headline extraction, lexical scoring, classification, and visual sentiment charting.

---

## Features

- Live headline extraction from:
  - **BBC News**
  - **The Guardian UK**
- Custom-built lexicon for sentiment scoring
- Rule-based NLP pipeline (no external ML models required)
- Classification into **Positive / Neutral / Negative**
- Duplicate-filtering & text cleaning
- Aggregated sentiment reports per news source
- Error-handling for request failures and timeouts
- **Sentiment visualization using Matplotlib (NEW)**  
  Automatically generates a bar chart showing sentiment distribution.

---

## Technologies Used

- Python 3  
- Requests  
- BeautifulSoup (bs4)  
- Collections (Counter)  
- Matplotlib (for charts)

---

## How It Works

### 1. Data Collection  
The analyzer scrapes up to *12* `<h3>` headlines from BBC News and The Guardian using `requests` and `BeautifulSoup`.

### 2. Text Normalisation  
Headlines are lower-cased, cleaned, and spacing-normalised.

### 3. Rule-Based Sentiment Scoring  
A handcrafted lexicon assigns numeric weights:
- `+1` for each positive keyword  
- `-1` for each negative keyword  

### 4. Sentiment Classification  
Scores are mapped into one of:
- Positive  
- Neutral  
- Negative  

### 5. Reporting  
The tool prints:
- Sentiment counts  
- Labelled headline list  
- Combined cross-source summary  
- **Visual sentiment chart (bar plot)**

---

## Example Output

## Example Chart Output
Below is an example of the visual sentiment chart generated using Matplotlib:

## Project Structure
- news_sentiment_analyzer.py
- README.md
  
  ## Future Improvements
- Integrate VADER or TextBlob for model-based sentiment scoring
- Expand lexicon using data-driven weighting
- Add visual sentiment charts using Matplotlib
- Build a lightweight web interface using Flask
- Add keyword trend detection and timeline analysis
- Add CSV/JSON export for sentiment reports

 ## License
This project is released under the MIT License.  
You are free to use, modify, and distribute this software with proper attribution. 


