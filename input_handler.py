# ============================================================
# input_handler.py
# Handles two input methods:
#   1. Manual entry (user types reviews one by one)
#   2. CSV file loading
# ============================================================

import csv
import os


def load_from_csv(filepath):
    """
    Loads reviews from a CSV file.
    Expected CSV format (with header row):
      review_text, rating
    Example:
      "This phone is great", 5
      "Terrible waste of money", 1
    """
    reviews = []

    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        return reviews

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                review_text = row["review_text"].strip()
                rating = int(row["rating"].strip())
                if 1 <= rating <= 5 and review_text:
                    reviews.append({"review_text": review_text, "rating": rating})
                else:
                    print(f"[WARNING] Skipped invalid row: {row}")
            except (KeyError, ValueError):
                print(f"[WARNING] Skipped malformed row: {row}")

    print(f"[INFO] Loaded {len(reviews)} review(s) from '{filepath}'")
    return reviews


def load_manually():
    """
    Lets the user type reviews one by one in the terminal.
    Type 'done' as review text to finish.
    """
    reviews = []
    print("\n--- Manual Review Entry ---")
    print("Enter your reviews below. Type 'done' when finished.\n")

    while True:
        review_text = input("Review text (or 'done' to finish): ").strip()
        if review_text.lower() == "done":
            break
        if not review_text:
            print("[WARNING] Empty review skipped.")
            continue

        while True:
            try:
                rating = int(input("Star rating (1-5): ").strip())
                if 1 <= rating <= 5:
                    break
                else:
                    print("[ERROR] Please enter a number between 1 and 5.")
            except ValueError:
                print("[ERROR] Invalid input. Please enter a number.")

        reviews.append({"review_text": review_text, "rating": rating})
        print(f"[OK] Review saved. ({len(reviews)} so far)\n")

    print(f"\n[INFO] {len(reviews)} review(s) entered manually.")
    return reviews


def get_reviews():
    """
    Asks the user which input method to use and returns reviews list.
    """
    print("\n========================================")
    print("  Product Review Analyzer - Input Mode  ")
    print("========================================")
    print("1. Enter reviews manually")
    print("2. Load from CSV file")
    print("3. Both (manual + CSV)")

    choice = input("\nChoose an option (1/2/3): ").strip()

    all_reviews = []

    if choice == "1":
        all_reviews = load_manually()

    elif choice == "2":
        filepath = input("Enter CSV file path (e.g., reviews.csv): ").strip()
        all_reviews = load_from_csv(filepath)

    elif choice == "3":
        print("\n[Step 1] Load from CSV")
        filepath = input("Enter CSV file path (e.g., reviews.csv): ").strip()
        all_reviews = load_from_csv(filepath)
        print("\n[Step 2] Add more reviews manually")
        all_reviews += load_manually()

    else:
        print("[ERROR] Invalid choice. Defaulting to manual entry.")
        all_reviews = load_manually()

    return all_reviews
