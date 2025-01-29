import sqlite3

def fix_db():
    conn = sqlite3.connect('hoongpt.db')
    c = conn.cursor()
    
    # Add test_suite column to runs if it doesn't exist
    c.execute("PRAGMA table_info(runs)")
    columns = {row[1] for row in c.fetchall()}
    if 'test_suite' not in columns:
        c.execute('ALTER TABLE runs ADD COLUMN test_suite TEXT DEFAULT "standard"')
        print("Added test_suite column to runs table")
    
    # Drop temp table if it exists
    c.execute('DROP TABLE IF EXISTS results_temp')
    
    # Create new results table with constraint
    c.execute('''
        CREATE TABLE results_new (
            id INTEGER PRIMARY KEY,
            run_id INTEGER REFERENCES runs(id),
            question_number INTEGER,
            test_number INTEGER,
            hoon_code TEXT,
            passed BOOLEAN,
            error_type TEXT,
            error_message TEXT,
            duration_ms INTEGER,
            UNIQUE(run_id, question_number, test_number)
        )
    ''')
    
    # Copy unique data to new table
    c.execute('''
        INSERT INTO results_new (
            run_id, question_number, test_number, hoon_code, passed, 
            error_type, error_message, duration_ms
        )
        SELECT DISTINCT 
            run_id, question_number, test_number, hoon_code, passed,
            error_type, error_message, duration_ms
        FROM results r1
        WHERE r1.rowid = (
            SELECT MIN(r2.rowid)
            FROM results r2
            WHERE r2.run_id = r1.run_id 
            AND r2.question_number = r1.question_number
            AND r2.test_number = r1.test_number
        )
    ''')
    
    # Drop old table and rename new one
    c.execute('DROP TABLE results')
    c.execute('ALTER TABLE results_new RENAME TO results')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    fix_db()