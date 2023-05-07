import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if "https" in url else 0)
    return features

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False