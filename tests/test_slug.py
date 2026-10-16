import unittest
from src.slug import slugify


class TestSlugify(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World! 123"), "hello-world-123")


if __name__ == '__main__':
    unittest.main()
