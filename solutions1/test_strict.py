import unittest
from solutions1.sample_func import add, sentence, echo, divide


class TestStrictDecorator(unittest.TestCase):
    def test_add_valid(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            add(2, 3.5)


    def test_sentence_valid(self):
        self.assertEqual(sentence("John", True), "Hi, John!")

    def test_sentence_wrong_type(self):
        with self.assertRaises(TypeError):
            sentence("john", "yes")

    def test_divide_valid(self):
        self.assertEqual(divide(10.0, 2.0), 5.0)

    def test_divide_invalid(self):
        with self.assertRaises(TypeError):
            divide(10, 2.0)



    def test_named_arguments(self):
        self.assertEqual(add(a=5, b=7), 12)

    def text_mixed_arguments(self):
        self.assertEqual(sentence("Alice", execited=False), "Hi, Alice.")

    def test_no_annotations(self):
        self.assertEqual(echo("any"), "any")
        self.assertEqual(echo(123), 123)



if __name__ == "__main__":
    unittest.main()
