def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    seen = {} # key -> best_record_found_so_far
    order = [] # to keep track of the first time we see a key

    for rec in records:
        # Create unique ID based on key_columns
        row_key = tuple(rec[col] for col in key_columns)

        if row_key not in seen:
            seen[row_key] = rec
            order.append(row_key)
        else:
            # --- Strategy Logic ---
            
            # If strategy is "last", always overwrite with the newest record
            if strategy == "last":
                seen[row_key] = rec
            
            # Keep the first one found (do nothing to the existing record)
            elif strategy == "first":
                continue
            
            # Keep the one with the fewest None values
            elif strategy == "most_complete":
                current_score = sum(1 for v in seen[row_key].values() if v is not None)
                new_score = sum(1 for v in rec.values() if v is not None)
                if new_score > current_score:
                    seen[row_key] = rec

    return [seen[k] for k in order]