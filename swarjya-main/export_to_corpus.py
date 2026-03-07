import sqlite3
import os

# Step 1: Connect to your database
db_path = "mydata.db"  # change if DB is in another location
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 2: Make sure corpus folder exists
os.makedirs("corpus", exist_ok=True)

# Step 3: Fetch all records from govt_schemes table
cursor.execute("SELECT title, description FROM govt_schemes")
rows = cursor.fetchall()

# Step 4: Loop through records and save each as a text file
for title, description in rows:
    # Create a safe filename (lowercase, underscores)
    filename = title.strip().replace(" ", "_").lower() + ".txt"
    file_path = os.path.join("corpus", filename)
    
    # Write description into file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(description.strip())
    
    print(f"✅ Saved: {file_path}")

# Step 5: Close DB connection
conn.close()
print("🎯 Export complete!")
