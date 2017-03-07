import unittest
import chatbot

class ChatBotResponseTest(unittest.TestCase):
    def test_about(self):
        r = chatbot.get_chatbot_response('!! about ')
        self.assertEquals(r, 'This is a chat room to discuss random things in a spacey environment. ')
    
    def test_help(self):
        r = chatbot.get_chatbot_response('!! help ')
        self.assertEquals(r, 'Available commands: <br>  !! about ->  descriptions of the chat room <br>  !! help ->  lists available chatbot commands <br>  !! add <num> <num> ->  add two integers together <br>  !! divide <num> <num> ->  divide two integers <br>  !! say <text> -> the chatbot repeats the text input by the user  <br>   ')
    
    def test_add(self):
        r = chatbot.get_chatbot_response('!! add 2 3 ')
        self.assertEquals(r, 5)
    
    def test_divide(self):
        r = chatbot.get_chatbot_response('!! divide 4 2 ')
        self.assertEquals(r, 2)
    
    def test_say(self):
        r = chatbot.get_chatbot_response('!! say this is a test ')
        self.assertEquals(r, "this is a test ")
        
    def test_random(self):
        r = chatbot.get_chatbot_response('!! say this is another test ')
        self.assertEquals(r, "this is another test ")

if __name__ == '__main__':
    unittest.main()