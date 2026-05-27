def add(numbers):
    # 1. Check if the input is empty
    if numbers == "":
        return 0

    # Default delimiter is comma
    # We will convert every special character to a comma to make it easy
    processed_numbers = numbers
    
    # 4, 7, 8, 9. Handling different and multiple delimiters
    if numbers.startswith("//"):
        # Find where the numbers actually start
        newline_index = numbers.find("\n")
        header = numbers[2:newline_index]
        processed_numbers = numbers[newline_index + 1:]
        
        # If there are multiple delimiters like //[*][%]\n
        if "[" in header:
            # Simple way to extract delimiters between [ and ]
            current_delim = ""
            inside_bracket = False
            for char in header:
                if char == "[":
                    inside_bracket = True
                    current_delim = ""
                elif char == "]":
                    inside_bracket = False
                    # Replace this custom delimiter with a comma
                    processed_numbers = processed_numbers.replace(current_delim, ",")
                elif inside_bracket:
                    current_delim += char
        else:
            # Simple single character delimiter like //;\n
            processed_numbers = processed_numbers.replace(header, ",")

    # 3. Handle new lines by converting them to commas
    processed_numbers = processed_numbers.replace("\n", ",")

    # 2. Split everything by comma (handles unknown amount of numbers)
    parts = processed_numbers.split(",")
    
    total = 0
    negatives = []

    for p in parts:
        if p != "": # Skip empty strings
            val = int(p)
            
            # 5. Check for negative numbers
            if val < 0:
                negatives.append(val)
            
            # 6. Ignore numbers bigger than 1000
            elif val <= 1000:
                total += val

    # 5. Raise error if there are negative numbers
    if len(negatives) > 0:
        # Convert list to string for the message
        neg_msg = ""
        for i in range(len(negatives)):
            neg_msg += str(negatives[i])
            if i < len(negatives) - 1:
                neg_msg += ","
        raise ValueError("negatives not allowed: " + neg_msg)

    return total