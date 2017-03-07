import unittest
import chatbot

class ChatBotResponseTest(unittest.TestCase):
    def test_hello(self):
        r = chatbot.get_chatbot_response('!! about ')
        self.assertEquals(r, 'This is a chat room to discuss random things in a spacey environment.')
    
    def test_add(self):
        r = chatbot.get_chatbot_response('!! add 2 3 ')
        self.assertEquals(r, 5)
    
    def test_divide(self):
        r = chatbot.get_chatbot_response('!! divide 4 2 ')
        self.assertEquals(r, 2)
    
    def test_say(self):
        r = chatbot.get_chatbot_response('!! say this is a test ')
        self.assertEquals(r, "this is a test ")

if __name__ == '__main__':
    unittest.main()