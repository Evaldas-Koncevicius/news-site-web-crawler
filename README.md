# news-site-web-crawler
A robust web scraping template designed to extract and organize key content—like article titles, authors, and body text—from any news site. This tool delivers clean, structured data in a CSV format, complete with progress saving and error handling for reliable performance.

Key Features:

Modular Design: Built with a clean, function-based structure for easy readability and maintenance.

Error Handling: Implements a try-finally block to save progress and log failed links, ensuring data is never lost.

Duplicate Handling: Prevents duplicate entries in the final data set for clean, reliable results.

Customizable: Easily adaptable for any new website by updating simple variables.


How It Works
This script operates in a methodical, step-by-step process to ensure reliable data extraction:

Link Loading: The script first reads a list of article URLs from a provided CSV file.

Page Navigation & Content Extraction: It then navigates to each URL, intelligently locates the main article body, and extracts specific content (such as headlines, paragraphs, and list items).

Data Organization: The extracted information is cleaned, organized, and saved as a new row in a master.csv file.

Progress & Error Management: The script meticulously tracks progress and saves any failed or pending links to a separate files, allowing the process to be resumed without losing any data.

The output.csv file included in this repository is a small, clean example of the final, organized data that the script produces.
