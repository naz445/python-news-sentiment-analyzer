# News Sentiment Analyzer  
A Python-based sentiment analysis tool that collects headlines from leading UK news outlets (BBC News and The Guardian) and evaluates the overall sentiment using a custom rule-based NLP engine.  
This project demonstrates skills in web scraping, natural language processing, data analysis, and software design.

---

## Features  
- Live headline extraction from:
  - **BBC News**
  - **The Guardian UK**
- Custom-built lexicon for sentiment scoring  
- Rule-based NLP pipeline (no external ML models required)  
- Classification into **Positive / Neutral / Negative**  
- Duplicate-filtering and headline cleaning  
- Aggregated sentiment reports per source  
- Detailed breakdown for each headline  
- Error-safe scraping layer (connection handling, strict timeouts)

---

## How It Works  

### 1. Data Collection  
The analyzer scrapes up to 12 `<h3>` headlines from both BBC News and The Guardian using `requests` and `BeautifulSoup`.  

### 2. Text Normalisation  
Each headline goes through spacing normalisation and lowercase conversion.

### 3. Rule-Based Sentiment Scoring  
A custom list of positive and negative keywords creates a numeric sentiment score:
- **+1** for each positive keyword  
- **–1** for each negative keyword  

### 4. Sentiment Classification  
Scores are mapped to one of:
- `Positive`
- `Neutral`
- `Negative`

### 5. Reporting  
The tool prints:
- Sentiment distribution for each news source  
- A formatted list of all headlines and their labels  
- A combined summary across sources

---

## Technologies Used  
- Python 3  
- Requests  
- BeautifulSoup (bs4)  
- Counter (collections module)
  
---

## Example Output
---

## Project Structure

---

## Future Improvements  
- Integrate VADER or TextBlob for model-based scoring  
- Expand lexicon using data-driven weighting  
- Add visual sentiment charts using Matplotlib  
- Build a lightweight web interface (Flask)  
- Add keyword trend detection  

---

## License  
This project is released under the MIT License.
