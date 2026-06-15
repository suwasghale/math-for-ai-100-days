import os
import json
import argparse

def create_notebook_content(day_num, topic):
    """Generates the JSON structure for a Jupyter Notebook with the standard template."""
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# Day {day_num:03d}: {topic}\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Objective\n",
                    "> *(Write a one-sentence plain-English explanation of what the algorithm achieves here)*"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Mathematical Foundation\n",
                    "> *(Define the variables and write the equation using LaTeX here)*\n",
                    "\n",
                    "**Example:**\n",
                    "$$ A \\cdot B = \\sum_{i=1}^{n} A_i B_i $$"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 3. Algorithmic Strategy\n",
                    "> *(Bullet points explaining how you will translate the math into arrays and loops)*"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 4. Implementation"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import numpy as np\n",
                    "\n",
                    "# Write your raw Python/NumPy code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 5. Verification"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Write a small test block proving your scratch code works\n",
                    "# Compare it against a known mathematical outcome if possible\n"
                ]
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 4
    }

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new day for the 100 Days of Math for AI challenge.")
    parser.add_argument("day", type=int, help="The day number (e.g., 4)")
    parser.add_argument("topic", type=str, help="The topic name in quotes (e.g., 'Dot Product')")
    
    args = parser.parse_args()
    
    # Format folder and file names
    formatted_topic = args.topic.replace(" ", "_").replace("/", "_")
    folder_name = f"Day_{args.day:03d}_{formatted_topic}"
    file_name = f"day_{args.day:03d}.ipynb"
    
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, file_name)
    
    # Create directory
    if os.path.exists(folder_path):
        print(f"⚠️ Directory '{folder_name}' already exists.")
        return
        
    os.makedirs(folder_path)
    
    # Create Jupyter Notebook
    notebook_json = create_notebook_content(args.day, args.topic)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(notebook_json, f, indent=1)
        
    print(f"✅ Successfully created: {folder_name}/{file_name}")
    print(f"🚀 You are ready to start coding!")

if __name__ == "__main__":
    main()