# news-site-web-crawler

A robust web scraping template designed to extract and organize key content—like article titles, authors, and body text—from any news site. This tool delivers clean, structured data in a CSV format, complete with progress saving and error handling for reliable performance.

Key Features

  Modular Design: Built with a clean, function-based structure for easy readability and maintenance.

  Error Handling: Implements a try-finally block to save progress and log failed links, ensuring data is never lost.

  Customizable: Easily adaptable for any new website by updating simple variables.


How It Works

  This system operates in a methodical, step-by-step process to ensure reliable data extraction:

  Link Discovery: The system first runs a separate script ([get_links.py](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/get_links.py)) to intelligently locate and gather all relevant article URLs from a website's sitemap. These links are then saved to a CSV file.

  Link Loading: The main script ([crawler.py](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/crawler.py)) then reads the list of article URLs from that CSV file.

  Page Navigation & Content Extraction: It then navigates to each URL, intelligently locates the main article body, and extracts specific content (such as headlines, paragraphs, and list items).

  Data Organization: The extracted information is cleaned, organized, and saved as a new row in a master.csv file.

  Progress & Error Management: The script meticulously tracks progress and saves any failed or pending links to separate files, allowing the process to be resumed without losing any data.

  The [output.csv](https://github.com/Evaldas-Koncevicius/news-site-web-crawler/blob/main/output.csv) file included in this repository is a small, clean example of the final, organized data that the script produces.
