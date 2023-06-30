import os
from pathlib import Path
import unittest

class TestCreateFiles(unittest.TestCase):
    def setUp(self):
        self.folder_name = "unab"
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in self.vowels]
        self.path = Path(self.folder_name)

    def tearDown(self):
        for file in self.path.glob('*.txt'):
            file.unlink()
        self.path.rmdir()

    def test_files_created(self):
        for letter in self.consonants:
            file_path = self.path / f"{letter}.txt"
            with open(file_path, 'r') as f:
                content = f.read()
            self.assertEqual(content, "I am a consonant file\n")

        for letter in self.vowels:
            file_path = self.path / f"{letter}.txt"
            with open(file_path, 'r') as f:
                content = f.read()
            self.assertEqual(content, "I am a vowel file\n")
