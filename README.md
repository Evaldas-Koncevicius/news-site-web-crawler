# News Site Web Crawler

A **robust web scraping template** designed to extract and organize key content—like article titles, authors, and body text—from any news site. This tool delivers **clean, structured data in CSV format**, complete with **progress saving** and **error handling** for reliable performance.

---

## Key Features

- **Modular Design:** Built with a clean, function-based structure for easy readability and maintenance.
- **Error Handling:** Implements a `try-finally` block to save progress and log failed links, ensuring data is never lost.
- **Customizable:** Easily adaptable for any new website by updating simple variables.

---

## How It Works

This system operates in a **methodical, step-by-step process** to ensure reliable data extraction:

1. **Link Discovery:**  
   The system first runs a separate script ([get_links.py](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/get_links.py)) to intelligently locate and gather all relevant article URLs from a website's sitemap. These links are then saved to a CSV file.

2. **Link Loading:**  
   The main script ([crawler.py](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/crawler.py)) reads the list of article URLs from the CSV file.

3. **Page Navigation & Content Extraction:**  
   It navigates to each URL, intelligently locates the main article body, and extracts specific content (headlines, paragraphs, and list items).

4. **Data Organization:**  
   The extracted information is cleaned, organized, and saved as a new row in `master.csv`.

5. **Progress & Error Management:**  
   The script meticulously tracks progress and saves any failed or pending links to separate files, allowing the process to **resume without losing any data**.

---

## Setup

1. get_links.py
   - Placeholders (PATH_TO_FILENAME.csv, LINK_TO_BASE_LEVEL_SITEMAP, 'SITEMAP_STRUCTURE_FILTER_TO_GET_RELEVENT_CATEGORIES') need to be adjusted in code.
   - PATH_TO_FILENAME.csv needs to be changed to filename of your choice with .csv at the end.
   - LINK_TO_BASE_LEVEL_SITEMAP needs to be changed to full link to a sitemap you intend to get links from.
   - SITEMAP_STRUCTURE_FILTER_TO_GET_RELEVENT_CATEGORIES there are 2 of these both need to be changed to search for categories, or simply any text string starting with your chosen symbols.

2. crawler.py
   - Placeholders (PATH_TO_FILENAME.csv, PATH_TO_LINKNAME.csv, PATH_TO_FAILEDNAME.csv, ELEMENT_OR_DIV_HOLDING_MAIN_ARTICLE, NAMES_OF_CLASSES, NAMES_OF_ELEMENTS_HOLDING_CONTENT) need to be adjusted in code.
   - PATH_TO_FILENAME.csv needs to be changed to filename (that will hold gathered data) of your choice with .csv at the end.
   - PATH_TO_LINKNAME.csv. needs to be changed to filename (that will save pending links and saves uncrawled links in case of crawler not being able to finnish) of your choice with .csv at the end.
   - PATH_TO_FAILEDNAME.csv needs to be changed to filename (that will save links that failed to be crawled) of your choice with .csv at the end.
   - ELEMENT_OR_DIV_HOLDING_MAIN_ARTICLE needs to be changed to an ELEMENT that would most accuretly pinpoint main article.
   - NAMES_OF_CLASSES needs to be changed to a list of names of unwanted classes to be skiped if they clutter data you need.
   - NAMES_OF_ELEMENTS_HOLDING_CONTENT needs to be changed to most accurate available elements that hold article information. (Most ussualy it will be P, h2, h3, li)

## Usage

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Evaldas-Koncevicius/news-site-web-crawler.git](https://github.com/Evaldas-Koncevicius/news-site-web-crawler.git)
    cd news-site-web-crawler
    ```

2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the script:**
    ```sh
    python main.py
    ```
---

## Example Output

The [output.csv](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/output.csv) file included in this repository is a **small, clean example** of the final, organized data that the script produces.

---

**Note:** This template is ideal for anyone looking to **scrape news sites reliably**, whether for personal projects, research, or freelance work.
