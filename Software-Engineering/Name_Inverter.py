def invert_name(name):
    # 1. Handle empty string
    if name == "":
        return ""

    # 2. Trim whitespace
    name = name.strip()

    # Split the name into parts
    parts = name.split()
    
    # List of common titles to ignore
    titles = ["Mr.", "Ms.", "Mrs.", "Dr."]

    # 3. Handle honorifics (Ms., Mr. etc.)
    if parts[0] in titles:
        parts.pop(0) # Remove the title from the list
        if len(parts) == 0:
            return ""
        if len(parts) == 1:
            return parts[0] # Example: "Ms. Yilmaz" -> "Yilmaz"

    # 4. Handle single name
    if len(parts) == 1:
        return parts[0]

    # 5. Handle First Last and Suffixes
    first_name = parts[0]
    last_name = parts[1]
    
    # If there is a suffix (like III, PhD)
    if len(parts) > 2:
        suffix = parts[2]
        return last_name + ", " + first_name + " " + suffix

    # Standard "First Last" -> "Last, First"
    return last_name + ", " + first_name