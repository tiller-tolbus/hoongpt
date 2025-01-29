import sqlite3
from tabulate import tabulate

def analyze_results():
    conn = sqlite3.connect('hoongpt.db')
    c = conn.cursor()
    
    print("Success Rates by Question:")
    c.execute('''
        SELECT 
            question_number,
            COUNT(*) as total_tests,
            SUM(CASE WHEN passed THEN 1 ELSE 0 END) as passed_tests,
            ROUND(100.0 * SUM(CASE WHEN passed THEN 1 ELSE 0 END) / COUNT(*), 1) as pass_rate
        FROM results 
        GROUP BY question_number 
        ORDER BY question_number
    ''')
    results = c.fetchall()
    print(tabulate(results, headers=['Question', 'Total Tests', 'Passed', 'Pass Rate %'], tablefmt='psql'))
    
    print("\nError Type Distribution:")
    c.execute('''
        SELECT 
            error_type,
            COUNT(*) as count,
            ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) as percentage
        FROM results 
        WHERE NOT passed AND error_type IS NOT NULL
        GROUP BY error_type
        ORDER BY count DESC
    ''')
    results = c.fetchall()
    print(tabulate(results, headers=['Error Type', 'Count', 'Percentage %'], tablefmt='psql'))
    
    print("\nSuccess Rate by Run:")
    c.execute('''
        SELECT 
            r.id as run_id,
            r.prompt_strategy,
            COUNT(*) as total_tests,
            SUM(CASE WHEN t.passed THEN 1 ELSE 0 END) as passed,
            ROUND(100.0 * SUM(CASE WHEN t.passed THEN 1 ELSE 0 END) / COUNT(*), 1) as pass_rate,
            r.total_cost
        FROM runs r
        JOIN results t ON r.id = t.run_id
        GROUP BY r.id
        ORDER BY r.id
    ''')
    results = c.fetchall()
    print(tabulate(results, headers=['Run', 'Strategy', 'Tests', 'Passed', 'Pass Rate %', 'Cost'], tablefmt='psql'))
    
    conn.close()

if __name__ == "__main__":
    analyze_results()