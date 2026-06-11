# 🎬 Empire Online — Top 100 Movies Scraper

This project automatically collects the list of the **Top 100 Greatest Movies of All Time** according to Empire Online and generates a text file with all titles organized from #1 to #100.

---

## 📌 Objective

Extract the titles from the official Empire Online page, filter them accurately, and generate a clean, ordered final list. The focus is on:

- Accessing the page with browser‑like headers to avoid blocks  
- Correctly identifying the HTML elements that contain the titles  
- Filtering only valid movie titles  
- Reversing the order to obtain the list from 1 to 100  
- Saving the result to a simple file  

---

## 🧠 How It Works

The program:

- Retrieves the HTML from the Empire Online page using headers that simulate a real browser  
- Parses the content with BeautifulSoup  
- Locates the elements containing the movie titles  
- Extracts only the relevant text, ignoring elements like “Director:”  
- Organizes the list in the correct order  
- Exports all titles to a `movies.txt` file  
