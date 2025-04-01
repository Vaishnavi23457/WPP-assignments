import re

def hindi_tokenizer(text):
    # Define regex patterns for different token types
    patterns = {
        'punctuation': r'[।!,?;:"\'(){}[\]<>]',  # Common Hindi punctuation
        'date': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',  # Matches 01/01/2025 or 01-01-25
        'url': r'https?://[^\s]+',  # Matches URLs
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',  # Matches emails
        'number': r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?|\b\d+\.\d+\b|\b\d+/\d+\b',  # Matches numbers like 3,22,243 or 313/77
        'username': r'@[a-zA-Z0-9_]{1,15}',  # Matches social media usernames like @user123
        'hindi_word': r'[\u0900-\u097F]+'  # Matches Hindi words (Devanagari script)
    }

    # Combine patterns into one regex
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns.items())

    # Tokenize the input text
    tokens = []
    for match in re.finditer(combined_pattern, text):
        tokens.append((match.lastgroup, match.group(0)))

    return tokens

# Example Hindi text for testing
text = "नमस्ते @user! मेरी वेबसाइट https://example.com पर देखें। मेरी ईमेल test@example.com है। आज की तारीख 01/01/2025 है। कीमत 3,22,243.50 रुपये है।"

# Tokenizing the Hindi text
tokens = hindi_tokenizer(text)

# Printing the tokens
print("टोकन परिणाम:")
print("=====================")
for token_type, token_value in tokens:
    print(f'प्रकार: {token_type.capitalize()}, मान: {token_value}')