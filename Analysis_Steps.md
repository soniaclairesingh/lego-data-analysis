1. **Data Setup**  
    Downloaded LEGO sets.csv and themes.csv.  
    Cleaned/renamed datasets and mainly focussed on the following.  
        sets: set_num, name, year, theme_id, num_parts  
        themes: id, name, parent_id  

2. **SQL Exploration**  
Used DB Browser for SQLite to run and test SQL queries.  
Key Queries:  
    -Top LEGO themes by set count --- Joined sets and themes on theme_id = id, counted sets per theme.  
    -Average parts per theme --- Calculated AVG(num_parts) grouped by theme_id.  
    -Yearly trends in LEGO set size --- GROUP BY year, averaged number of parts per year.  
   
*Saved relevant outputs as .csv for use in Python.*  

3. **Python Visualization**  
Used Spyder (Anaconda) with Pandas, Seaborn, and Matplotlib.  
Visuals Created:  
    -Top LEGO Themes by Set Count --- Bar plot of top 10 themes.  
    -Top Themes by Average Parts --- Horizontal bar plot showing complexity via part count.  
    -LEGO Set Size Over Time --- Line plot showing trends in parts per year.  

*---Plots saved to /visuals/ folder (e.g., top_lego_themes.png, top_lego_parts.png, yearly_trends_parts.png)*  

**Key Take-aways:**  
    SQL joins and GROUP BY with aggregate functions.  
    Importing SQL results into Python for visualization.  
    Using pd.merge() to combine datasets by ID.  
    Creating Seaborn plots, setting labels, rounding numbers, customizing aesthetics.  
    Using GitHub for portfolio projects, embedding images in README.  

**Next Steps (ongoing)**  
    Add Power BI dashboard showcasing findings.  
    Include an interactive notebook version (.ipynb).  
    Further analyze nostalgic vs. modern themes, based on year trends.  

*Portions of this project, including drafting code comments and documentation, were supported by AI tools (e.g., ChatGPT) to enhance clarity and efficiency. All code and analysis were reviewed and curated by me.*
