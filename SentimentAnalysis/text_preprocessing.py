import nltk
nltk.download('words')

import re
import pandas as pd
import emoji as e
import spacy
from nltk.corpus import words
from symspellpy import Verbosity
from setup_text_preprocessing import load_spellcorrector, HTML_CLEANER, URL_CLEANER, SLANG_MAP, EMOTICON_MAP, CORRECTION_WHITELIST # Config file for text preprocessing


# Initialize spaCy and SymSpell
nlp = spacy.load("en_core_web_sm")
sym_spell = load_spellcorrector()

def replace_words_with_dict(text, dictionary):
    """Replace words in text using a dictionary, prioritizing longer phrases."""
    sorted_words = sorted(dictionary.keys(), key=len, reverse=True)
    for word in sorted_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, dictionary[word], text, flags=re.IGNORECASE)
    return text.lower()

def text_correction(text, sym_spell=sym_spell, whitelist=CORRECTION_WHITELIST):
    """Autocorrect words not in the whitelist using SymSpell."""
    words = text.split()
    corrected_words = []
    for word in words:
        if word in whitelist:
            corrected_words.append(word)
        else:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
            corrected_words.append(suggestions[0].term if suggestions else word)
    return " ".join(corrected_words)

def text_lemmatization(text):
    """Lemmatize text using spaCy."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def text_preprocessing(text):
    """
    Preprocess text for NLP tasks (e.g., sentiment analysis).
    Steps are ordered to preserve meaning and optimize efficiency.
    """
    # 1. Remove HTML tags
    cleaned_text = re.sub(HTML_CLEANER, '', text)
    # 2. Replace hyphens with spaces
    cleaned_text = cleaned_text.replace('-', ' ') 
    # 3. Remove URLs
    cleaned_text = re.sub(URL_CLEANER, '', cleaned_text)
    # 4. Convert to lowercase for consistency
    cleaned_text = cleaned_text.lower()
    # 5. Convert emojis to text and make readable (replace ':' and '_' with spaces)
    cleaned_text = e.demojize(cleaned_text)
    cleaned_text = cleaned_text.replace(':', ' ').replace('_', ' ')
    # 6. Convert emoticons to text
    cleaned_text = replace_words_with_dict(cleaned_text, EMOTICON_MAP)
    # 7. Replace slang with full phrases
    cleaned_text = replace_words_with_dict(cleaned_text, SLANG_MAP)
    # 8. Remove numbers
    cleaned_text = re.sub(r'\d+', '', cleaned_text)
    # 9. Autocorrect misspelled words
    cleaned_text = text_correction(cleaned_text)
    # 10. Remove non-alphabetic characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text)
    # 11. Normalize whitespace (replace multiple spaces with one)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    # 12. Strip leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    # 13. Lemmatize to reduce words to base forms
    cleaned_text = text_lemmatization(cleaned_text)
    return cleaned_text

# Only for Test
if __name__ == "__main__":
    import pandas as pd
    dataset = pd.read_csv("./data/imdb_dataset.csv")
    for i in range(2):
        text = dataset.iloc[i]["review"]
        print(f"{text}\n ↓ \n{text_preprocessing(text)}\n\n")
