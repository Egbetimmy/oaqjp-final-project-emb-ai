"""
Unit tests for the Emotion Detection application.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    TestCase class containing unit tests for the emotion_detector function.
    """
    def test_emotion_detector(self):
        """
        Tests emotion_detector with various inputs and asserts dominant_emotion.
        """
        # Test case 1: joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case 2: anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case 3: disgust
        result_3 = emotion_detector('I am really disgusted by this at work')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case 4: sadness
        result_4 = emotion_detector('I am sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case 5: fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
