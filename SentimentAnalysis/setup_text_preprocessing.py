import re
from symspellpy import SymSpell, Verbosity
import pkg_resources

def load_spellcorrector():
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = pkg_resources.resource_filename(
      "symspellpy", "frequency_dictionary_en_82_765.txt")
    bigram_path = pkg_resources.resource_filename(
      "symspellpy", "frequency_bigramdictionary_en_243_342.txt")
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
    sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
    
    return sym_spell
    
HTML_CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
URL_CLEANER = re.compile(r'https?://\S+|www\.\S+')

SLANG_MAP = {
    "brb": "Be right back",
    "lmao": "Laughing my ass off",
    "lol": "Laughing out loud",
    "ppl": "People",
    "afk": "Away from keyboard",
    "asap": "As soon as possible",
    "btw": "By the way",
    "fyi": "For your information",
    "gg": "Good game",
    "gl": "Good luck",
    "gr8": "Great",
    "idk": "I don't know",
    "ikr": "I know, right?",
    "imo": "In my opinion",
    "imho": "In my humble opinion",
    "irl": "In real life",
    "jk": "Just kidding",
    "l8r": "Later",
    "lmk": "Let me know",
    "nvm": "Never mind",
    "omw": "On my way",
    "rofl": "Rolling on the floor laughing",
    "smh": "Shaking my head",
    "tbh": "To be honest",
    "tldr": "Too long; didn't read",
    "ttyl": "Talk to you later",
    "w/e": "Whatever",
    "w/o": "Without",
    "wtf": "What the fuck",
    "yolo": "You only live once",
    "b4": "Before",
    "cu": "See you",
    "dm": "Direct message",
    "fomo": "Fear of missing out",
    "ftw": "For the win",
    "gtg": "Got to go",
    "hmu": "Hit me up",
    "nsfw": "Not safe for work",
    "op": "Original poster",
    "srsly": "Seriously",
    "tmi": "Too much information",
    "u": "You",
    "ur": "Your",
    "yw": "You're welcome"
}

EMOTICON_MAP = {
    ":)": "Smile",
    ":‑)": "Smile",
    ":(": "Sad",
    ":‑(": "Sad",
    ":D": "Big grin",
    ":‑D": "Big grin",
    ";)": "Wink",
    ";‑)": "Wink",
    ":P": "Tongue out",
    ":‑P": "Tongue out",
    ":O": "Surprise",
    ":‑O": "Surprise",
    ":|": "Neutral",
    ":‑|": "Neutral",
    ":*": "Kiss",
    ":‑*": "Kiss",
    ":/": "Confused",
    ":‑/": "Confused",
    ">:(": "Angry",
    ">:‑(": "Angry",
    "XD": "Laughing hard",
    "x‑D": "Laughing hard",
    ":‑[": "Sad",
    ":‑]": "Happy",
    ":-{": "Sad",
    ":-}": "Happy",
    ":-@": "Screaming",
    ":-#": "Sealed lips",
    ":-X": "Sealed lips",
    ":-!": "Exclamation",
    ":-&": "Tongue-tied",
    ":-+": "Confused",
    ":-^": "Smirk",
    ":-<": "Sad"
}

CORRECTION_WHITELIST = {
    "reddit",
    "youtube",
    "facebook",
    "twitter",
    "tiktok",
    "snapchat",
    "instagram",
    "whatsapp",
    "linkedin",
    "bbc"
    "\"",
    "!",
    "?"
}