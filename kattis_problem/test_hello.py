import unittest
from unittest.mock import patch
from io import StringIO
import hello

class TestHello(unittest.TestCase):

    @patch("sys.stdout", StringIO("Hello World!"))
    def test_hello(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            # pylint: disable=no-member
            hello.main()
            # pylint: enable=no-member
            actual_ans = mock_output.getvalue().strip()
            expexted_ans = "Hello World!"
            self.assertEqual(actual_ans, expexted_ans)


if __name__ == "main":
    unittest.main()
