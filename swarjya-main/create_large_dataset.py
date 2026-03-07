import sqlite3

# Connect to database (make sure mydata.db exists)
conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

# Insert 500 sample schemes
for i in range(1, 501):
    cursor.execute(
        "INSERT INTO govt_schemes (title, description) VALUES (?, ?)",
        (f"scheme_{i}", f"This is a detailed description of scheme number {i}, created for large dataset corpus extraction testing.")
    )

# Save & close
conn.commit()
conn.close()

print("✅ Large dataset (500 schemes) created in database!")
