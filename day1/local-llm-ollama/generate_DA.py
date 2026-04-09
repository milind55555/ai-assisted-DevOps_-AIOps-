import ollama

PROMPT = """
You are a senior Data Analyst.

Generate a complete end-to-end data analysis solution for a {domain} dataset.

Include the following:

1. SQL:
- Create table schema
- Sample queries for analysis (aggregation, joins, filtering)

2. Python (Pandas):
- Data loading
- Data cleaning
- Exploratory Data Analysis (EDA)
- Visualization (matplotlib/seaborn)

3. Power BI:
- Dashboard design (KPIs, charts)
- Suggested visuals (bar, line, pie)
- Key metrics to track

4. Insights:
- Business insights from data
- Recommendations

Constraints:
- Output should be structured
- Use best practices
- Keep it practical and real-world
"""

def generate_data_analysis(domain):
    response = ollama.chat(
        model='llama3.2:1b',
        messages=[{
            'role': 'user',
            'content': PROMPT.format(domain=domain)  # ✅ FIXED
        }]
    )
    return response['message']['content']

if __name__ == '__main__':
    domain = input("Enter domain (sales/finance/healthcare): ")  # ✅ FIXED
    result = generate_data_analysis(domain)

    print("\nGenerated Data Analysis Project:\n")
    print(result)
