import os
import json
import argparse

def rename_day(day_num, new_topic):
    # 1. Find the existing folder
    day_str = f"{day_num:03d}"
    folders = [f for f in os.listdir('.') if f.startswith(f"Day_{day_str}_")]
    
    if not folders:
        print(f"❌ No folder found for Day {day_str}")
        return
    
    old_folder = folders[0]
    new_folder = f"Day_{day_str}_{new_topic.replace(' ', '_')}"
    
    # 2. Rename the folder
    os.rename(old_folder, new_folder)
    print(f"📂 Renamed folder to: {new_folder}")
    
    # 3. Rename the notebook file inside
    old_nb_path = os.path.join(new_folder, f"day_{day_str}.ipynb")
    new_nb_path = os.path.join(new_folder, f"day_{day_str}.ipynb") # Name stays same
    
    # 4. Update the title inside the notebook
    with open(old_nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Update first cell (the title cell)
    nb['cells'][0]['source'] = [f"# Day {day_num:03d}: {new_topic}\n"]
    
    with open(old_nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        
    print(f"📝 Updated notebook title to: {new_topic}")
    print("✅ Done! Now run 'python update_readme.py' to refresh the links.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("topic", type=str)
    args = parser.parse_args()
    rename_day(args.day, args.topic)