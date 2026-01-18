import os
import sys
import re
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from thefuzz import fuzz

# 1. Use 'warnings' to keep our test output clean
warnings.filterwarnings("ignore")

def run_advanced_test():
    print("🚀 STARTING TOOLBELT SMOKE TEST V2\n" + "="*40)

    # --- Test 1: Built-ins (os & re) ---
    current_path = os.getcwd()
    # Regex: Find the last folder name in the path
    folder_match = re.search(r'[^\\/]+$', current_path)
    folder_name = folder_match.group() if folder_match else "Unknown"
    print(f"📁 System Check: Working in folder [{folder_name}]")

    # --- Test 2: Third-Party (Pandas & Openpyxl) ---
    try:
        data = {
            'Tool': ['Pandas', 'Matplotlib', 'TheFuzz', 'Openpyxl'],
            'Status': [100, 100, 95, 100]
        }
        df = pd.DataFrame(data)
        
        # CREATE THE EXCEL FILE HERE:
        df.to_excel("smoke_test_output.xlsx", index=False)
        
        print(f"📊 Pandas Check: Created DataFrame and saved to 'smoke_test_output.xlsx'")
    except Exception as e:
        print(f"❌ Excel/Pandas Error: {e}")

    # --- Test 3: TheFuzz (Fuzzy Matching) ---
    score = fuzz.ratio("Python 3.14", "Python 3.14.2")
    print(f"🧠 Fuzzy Check: Version match score is {score}/100")

    # --- Test 4: Matplotlib (Visuals) ---
    print("🎨 Matplotlib Check: Generating test plot...")
    plt.figure(figsize=(5, 3))
    plt.bar(df['Tool'], df['Status'], color='skyblue')
    plt.title("ToolBelt Health Levels")
    
    # This will open a window on your laptop!
    print("✨ Close the graph window to finish the test.")
    plt.show()

    print("="*40 + "\n✅ ALL SYSTEMS OPERATIONAL")

if __name__ == "__main__":
    run_advanced_test()