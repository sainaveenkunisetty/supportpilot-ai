
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_FILE = BASE_DIR / "data" / "support_knowledge.txt"


class KnowledgeBase:
    def __init__(self):
        text = KNOWLEDGE_FILE.read_text(encoding="utf-8")

        self.documents = [
            item.strip()
            for item in text.split("\n\n")
            if item.strip()
        ]

        if not self.documents:
            raise ValueError("Knowledge base is empty.")

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
        )

        self.document_vectors = self.vectorizer.fit_transform(
            self.documents
        )

    def search(self, question, top_k=3, min_score=0.10):
        if not question or not question.strip():
            return []

        question_vector = self.vectorizer.transform([question])

        if question_vector.nnz == 0:
            return []

        scores = cosine_similarity(
            question_vector,
            self.document_vectors,
        ).flatten()

        ranked_indices = scores.argsort()[::-1]

        results = []

        for index in ranked_indices:
            score = float(scores[index])

            if score < min_score:
                continue

            results.append({
                "text": self.documents[index],
                "score": score,
            })

            if len(results) >= top_k:
                break

        return results
