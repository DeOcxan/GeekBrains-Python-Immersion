import re
from collections import Counter
from typing import List, Tuple

class TextAnalyzer:
    """Analyzes text to find the most frequent words."""

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")
        self._text = text
        self._word_counts = self._calculate_word_counts()

    def _preprocess_text(self) -> str:
        """Cleans the text by removing punctuation and converting to lowercase."""
        # Remove punctuation (keeps alphanumeric and spaces)
        cleaned_text = re.sub(r'[^\w\s]', '', self._text)
        return cleaned_text.lower()

    def _tokenize_text(self, cleaned_text: str) -> List[str]:
        """Splits the cleaned text into a list of words."""
        return cleaned_text.split()

    def _calculate_word_counts(self) -> Counter:
        """Counts the frequency of each word in the text."""
        preprocessed_text = self._preprocess_text()
        words = self._tokenize_text(preprocessed_text)
        # Filter out empty strings that might result from multiple spaces after cleaning
        return Counter(word for word in words if word)

    def get_most_frequent_words(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Returns the N most frequent words and their counts.

        Args:
            top_n: The number of most frequent words to return.

        Returns:
            A list of tuples, where each tuple contains a word and its frequency.
        """
        if not isinstance(top_n, int) or top_n <= 0:
            raise ValueError("top_n must be a positive integer.")
        return self._word_counts.most_common(top_n)

    @property
    def text(self) -> str:
        return self._text

    @property
    def word_counts(self) -> Counter:
        return self._word_counts

def main():
    """
    Main function to demonstrate the TextAnalyzer.
    """
    sample_text = ("""
    Python is an interpreted, high-level and general-purpose programming language. 
    Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
    Its language constructs and object-oriented approach aim to help programmers write clear, logical code for 
    small and large-scale projects. Python is dynamically-typed and garbage-collected. 
    It supports multiple programming paradigms, including structured (particularly, procedural), 
    object-oriented and functional programming. Python is often described as a "batteries included" 
    language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s, 
    as a successor to the ABC language, and first released it in 1991 as Python 0.9.0. 
    Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and 
    a garbage collection system with reference counting. Python 3.0 was released in 2008 and was a 
    major revision of the language that is not completely backward-compatible. Python 2 was discontinued 
    with version 2.7.18 in 2020. Python consistently ranks as one of the most popular programming languages.
    This is a sample text to test the word counting. Text, text, WORD, word.
    """)

    print(f"Original Text:\n{sample_text}\n")

    try:
        analyzer = TextAnalyzer(sample_text)
        top_10_words = analyzer.get_most_frequent_words(10)
        
        print("Top 10 most frequent words:")
        for word, count in top_10_words:
            print(f"- '{word}': {count}")

        # Example with a different N
        top_5_words = analyzer.get_most_frequent_words(5)
        print("\nTop 5 most frequent words:")
        for word, count in top_5_words:
            print(f"- '{word}': {count}")

        # Accessing all word counts
        # print("\nAll word counts:")
        # for word, count in analyzer.word_counts.items():
        # print(f"- '{word}': {count}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
