import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize, RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords

#make functions reusable as modules 

stop_words = set(stopwords.words('english'))

def remove_specific_text(text):
    """
    Remove specific words and handle contractions from the input text
    using regular expression tokenizer.

    Parameters:
    - text (str): The input text to be preprocessed.
    - stop_words (set): A set of stop words to be used in the removal process.

    Returns:
    - str: The preprocessed text with specified words and contractions removed.

    Example:
    example_text = "I' ve seen these word before, I don't think he has. It's amp and don.
    preprocessed_example = remove_specific_text(example_text, stop_words)
    print(preprocessed_example)
    """
    
    # handle contractions
    tokenizer = RegexpTokenizer(r"\w+['’]?\w+|\w+")

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Join the filtered tokens back into a sentence
    filtered_text = ' '.join(filtered_tokens)

    return filtered_text

def verify_cvec_conversion(data, text_column='selftext'):
    """
    Verify the successful conversion of the text data in the original
    dataframe to a count matrix using Count Vectorizer

    Parameters:
    - data (DataFrame): The input dataframe containing the column selftext with
      the text data
    - text_column (str): The name of the column containing text data.
    Default is 'selftext'

    Returns:
    - tuple: A tuple showing the shape of the resulting count vectorizer matrix
    """
    if isinstance(data, pd.Series):
        # If it's a Series, directly use it as text data
        text_data = data.astype(str)
    elif isinstance(data, pd.DataFrame):
        # If it's a DataFrame, use the specified column name
        if text_column not in data.columns:
            raise KeyError(f"'{text_column}' column not found")
        text_data = data[text_column].astype(str)
    else:
        raise ValueError("Input data must be a DataFrame or Series.")

    # initialize counter vectorizer with English stop words
    cvec = CountVectorizer(stop_words='english')

    # fit and transform the text data to count matrix on the Reddit selftext
    cvec_matrix = cvec.fit_transform(text_data)

    # Check the shape of the resulting Count matrix
    print(f"\nShape of Count Matrix: {cvec_matrix.shape}")

    return cvec_matrix.shape

def verify_tvec_conversion(data, text_column='selftext'):
    """
    Verify the successful conversion of the text data in the original
    dataframe to a TF-IDF matrix using TfidfVectorizer.

    Parameters:
    - data (pd.DataFrame): The input dataframe containing the column selftext with
      the text data
    - text_column (str): The name of the column containing text data.
    Default is 'selftext'

    Returns:
    - tuple: A tuple showing the shape of the resulting TF-IDF matrix

    Example:
    verify_cvec_conversion(df_datascience)
    """
    if isinstance(data, pd.Series):
        # If it's a Series, directly use it as text data
        text_data = data.astype(str)
    elif isinstance(data, pd.DataFrame):
        # If it's a DataFrame, use the specified column name
        if text_column not in data.columns:
            raise KeyError(f"'{text_column}' column not found.")
        text_data = data[text_column].astype(str)
    else:
        raise ValueError("Input data must be a DataFrame or Series.")

    # initialize TF-IDF vectorizer
    tvec = TfidfVectorizer(stop_words='english')

    # fit and transform the text data to TF-IDF matrix on the Reddit selftext
    tvec_matrix = tvec.fit_transform(text_data)

    # Check the shape of the resulting TF-IDF matrix
    print(f"\nShape of TF-IDF Matrix: {tvec_matrix.shape}")

    return tvec_matrix.shape

