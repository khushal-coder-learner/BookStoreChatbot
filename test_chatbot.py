# test_chatbot.py

import pytest
from chatbot import BookstoreChatbot

@pytest.fixture
def bot():
    return BookstoreChatbot()

def test_greet(bot):
    response = bot.greet()
    assert "Welcome" in response

def test_search_existing_book(bot):
    response = bot.search_book("1984")
    assert "George Orwell" in response

def test_search_non_existing_book(bot):
    response = bot.search_book("Invisible Man")
    assert "Sorry" in response

def test_recommend(bot):
    response = bot.recommend()
    assert "recommend" in response.lower()

def test_handle_greeting(bot):
    response = bot.handle_input("hi there")
    assert "Welcome" in response

def test_handle_recommend(bot):
    response = bot.handle_input("Can you recommend me something?")
    assert "recommend" in response.lower()

def test_handle_search(bot):
    response = bot.handle_input("Do you have 1984?")
    assert "George Orwell" in response

def test_handle_unknown(bot):
    response = bot.handle_input("Tell me a joke")
    assert "not sure" in response.lower()
