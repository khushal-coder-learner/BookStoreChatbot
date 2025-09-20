# chatbot.py

class BookstoreChatbot:
    def __init__(self):
        self.catalog = {
            "1984": "George Orwell",
            "To Kill a Mockingbird": "Harper Lee",
            "The Great Gatsby": "F. Scott Fitzgerald",
            "The Catcher in the Rye": "J.D. Salinger",
            "The Alchemist": "Paulo Coelho",
        }

    def greet(self):
        return "Hello! Welcome to the Bookstore Chatbot. How can I help you today?"

    def search_book(self, title: str) -> str:
        """Search for a book by title."""
        title = title.strip().title()
        if title in self.catalog:
            return f"Yes, we have '{title}' by {self.catalog[title]}."
        else:
            return f"Sorry, we don't have '{title}' in our catalog."

    def recommend(self) -> str:
        """Recommend a book from the catalog."""
        # Just pick the first one for simplicity
        book, author = next(iter(self.catalog.items()))
        return f"I recommend '{book}' by {author}. It's a classic!"

    def handle_input(self, user_input: str) -> str:
        """Handle user queries."""
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return self.greet()
        elif "recommend" in user_input:
            return self.recommend()
        elif "have" in user_input or "search" in user_input:
            # Extract last word as title guess
            title = user_input.split()[-1]
            return self.search_book(title)
        else:
            return "I'm not sure I understand. You can ask me to recommend a book or search for one."
