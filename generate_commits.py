import os
import subprocess
import random
from datetime import datetime, timedelta, time

# Configurations
TOTAL_COMMITS = 220
TOTAL_DAYS = 106
REPO_DIR = r"E:\GITHUB CONTRIBUTION"
LOG_FILE = os.path.join(REPO_DIR, "daily_learning_log.md")
README_FILE = os.path.join(REPO_DIR, "README.md")

LEARNING_TOPICS = [
    ("Python Basics", ["Variables & Data Types", "Control Flow & Loops", "Functions & Scope", "List Comprehensions", "Dictionary Methods"]),
    ("Advanced Python", ["Decorators & Wrappers", "Generators & Iterators", "Asyncio & Concurrency", "Context Managers", "Metaclasses"]),
    ("Data Structures", ["Arrays & Strings", "Linked Lists", "Stacks & Queues", "Binary Trees & BST", "Graphs & Traversal", "Hash Tables"]),
    ("Algorithms", ["Binary Search", "Sorting Algorithms", "Recursion & Backtracking", "Dynamic Programming", "Greedy Algorithms", "Two Pointers"]),
    ("Web Development", ["HTML5 Semantic Tags", "CSS Flexbox & Grid", "JavaScript ES6+ Features", "Promises & Async/Await", "RESTful API Design", "React Basics", "State Management"]),
    ("Databases", ["SQL Queries & Joins", "Database Indexing", "ACID Properties", "MongoDB & NoSQL", "ORM with SQLAlchemy"]),
    ("DevOps & Tools", ["Git Commands & Workflows", "Docker Containers", "Linux Command Line", "CI/CD Pipelines", "Environment Variables"]),
    ("System Design", ["Load Balancing", "Caching Strategies", "Database Sharding", "Message Queues", "Microservices Architecture"]),
    ("Data Science", ["NumPy Array Operations", "Pandas DataFrames", "Data Visualization with Matplotlib", "Scikit-Learn Basics", "Linear Regression"])
]

def generate_daily_counts(total_commits, total_days):
    # Initialize counts with at least 1 commit for active days
    # Give roughly 10-15 rest days (0 commits)
    counts = [0] * total_days
    
    # Select active days (~90-95 days out of 106)
    active_day_indices = set(random.sample(range(total_days), k=min(92, total_days)))
    
    # Assign minimum 1 commit to active days
    for idx in active_day_indices:
        counts[idx] = 1
    
    remaining = total_commits - sum(counts)
    
    # Distribute remaining commits among active days
    active_indices_list = list(active_day_indices)
    while remaining > 0:
        idx = random.choice(active_indices_list)
        # Cap max commits per day to 5 for natural distribution
        if counts[idx] < 5:
            counts[idx] += 1
            remaining -= 1
            
    return counts

def main():
    os.chdir(REPO_DIR)
    
    # Setup initial README.md
    readme_content = """# Daily Learning Journal 📚

A comprehensive record of daily learning, notes, and code snippets across software engineering, algorithms, and web development.

## Overview
- **Duration**: 106 Days
- **Total Contributions**: 220 Log Entries
- **Topics Covered**: Python, Data Structures & Algorithms, Web Development, System Design, DevOps, Databases.

---
"""
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("# Daily Learning Logs\n\n")

    # Determine date range: end date is today, start date is (TOTAL_DAYS - 1) days ago
    end_date = datetime.now()
    start_date = end_date - timedelta(days=TOTAL_DAYS - 1)
    
    daily_counts = generate_daily_counts(TOTAL_COMMITS, TOTAL_DAYS)
    
    commit_counter = 0
    
    for day_idx in range(TOTAL_DAYS):
        current_day_date = start_date + timedelta(days=day_idx)
        num_commits = daily_counts[day_idx]
        
        if num_commits == 0:
            continue
            
        for c in range(num_commits):
            commit_counter += 1
            
            # Generate realistic timestamp between 09:00 and 22:00
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_datetime = datetime(
                year=current_day_date.year,
                month=current_day_date.month,
                day=current_day_date.day,
                hour=hour,
                minute=minute,
                second=second
            )
            
            # Format ISO date string for Git
            date_str = commit_datetime.strftime("%Y-%m-%dT%H:%M:%S+05:30")
            
            # Select topic
            category, topics = random.choice(LEARNING_TOPICS)
            topic = random.choice(topics)
            
            commit_msg = f"Day {day_idx + 1}: Study {category} - {topic}"
            
            # Append entry to log file
            log_entry = f"## [{commit_datetime.strftime('%Y-%m-%d %H:%M')}] {category}: {topic}\n"
            log_entry += f"- Practiced {topic} concept and updated code examples.\n"
            log_entry += f"- Log entry {commit_counter} of {TOTAL_COMMITS}\n\n"
            
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
                
            # Stage files
            subprocess.run(["git", "add", "."], check=True)
            
            # Set environment variables for backdating
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                env=env,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    print(f"Successfully generated {commit_counter} commits across {TOTAL_DAYS} days!")

if __name__ == "__main__":
    main()
