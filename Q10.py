# Multiple store location dictionaries
store_a = {"laptops": 10, "mice": 50, "keyboards": 20}
store_b = {"monitors": 15, "mice": 30, "cables": 100}

print("--- In-Memory Inventory Tracker ---")

# 1. Key existence check & Safe access via .get()
search_item = "mice"
if search_item in store_a:
    qty = store_a.get(search_item, 0)
    print(f"[*] Found '{search_item}' in Store A: {qty} units")
else:
    print(f"[*] '{search_item}' not found in Store A.")

# 2. Merging dictionaries using the update operator (|) 
# Note: In a direct merge, values from the right dictionary overwrite the left
flat_merge = store_a | store_b
print(f"\n[*] Flat Merge (store_a | store_b): \n    {flat_merge}")

# 3. Merging and summing actual stock levels using Dictionary Comprehension
all_keys = set(store_a.keys()) | set(store_b.keys())

total_inventory = {
    item: store_a.get(item, 0) + store_b.get(item, 0) 
    for item in all_keys
}

print(f"\n[*] Total Consolidated Inventory (Summed via Comprehension): \n    {total_inventory}")