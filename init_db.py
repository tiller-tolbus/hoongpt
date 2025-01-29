import sqlite3
import os
from datetime import datetime

def init_db():
    """Initialize the database with a schema.
    NEVER drops or modifies existing tables."""
    
    # If database exists, create a backup first
    if os.path.exists('hoongpt.db'):
        backup_name = f'hoongpt_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db.bak'
        print(f"Creating backup: {backup_name}")
        import shutil
        shutil.copy2('hoongpt.db', backup_name)
    
    conn = sqlite3.connect('hoongpt.db')
    c = conn.cursor()

    # Check for existing tables
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing_tables = {row[0] for row in c.fetchall()}
    
    # Create tables only if they don't exist
    if 'runs' not in existing_tables:
        c.execute('''
            CREATE TABLE runs (
                id INTEGER PRIMARY KEY,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                model TEXT,
                prompt_strategy TEXT,
                prompt_text TEXT,
                prompt_tokens INTEGER,
                total_cost REAL,
                test_suite TEXT DEFAULT 'standard',
                UNIQUE(timestamp, model, prompt_strategy, test_suite)
            )
        ''')

    if 'results' not in existing_tables:
        c.execute('''
            CREATE TABLE results (
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

    if 'prompt_strategies' not in existing_tables:
        c.execute('''
            CREATE TABLE prompt_strategies (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                description TEXT,
                template TEXT
            )
        ''')

    if 'questions' not in existing_tables:
        c.execute('''
            CREATE TABLE questions (
                id INTEGER PRIMARY KEY,
                question_text TEXT,
                category TEXT,
                difficulty INTEGER
            )
        ''')

    # Always try to add known prompt strategies (will fail silently if they exist)
    c.execute('''
        INSERT OR IGNORE INTO prompt_strategies (name, description)
        VALUES 
            ('minimal', 'Just core instructions without Urbit docs'),
            ('small_prompt', 'Minimal system prompt with just core instructions'),
            ('full_docs', 'Complete Urbit documentation included in prompt')
    ''')

    # Load questions if they don't exist
    import json
    for i in range(1, 11):  # Questions 1-10
        try:
            with open(f'questions/{i}.json', 'r') as f:
                data = json.load(f)
                c.execute('''
                    INSERT OR IGNORE INTO questions (id, question_text)
                    VALUES (?, ?)
                ''', (i, data['question']))
        except FileNotFoundError:
            print(f"Warning: questions/{i}.json not found")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()