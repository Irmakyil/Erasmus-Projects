import unittest
from Name_Inverter import invert_name

class TestNameInverter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(invert_name(""), "")

    def test_single_name(self):
        self.assertEqual(invert_name("Irmak"), "Irmak")

    # Doğru senaryo: "Ad Soyad" girilir, "Soyad, Ad" beklenir
    def test_first_last(self):
        self.assertEqual(invert_name("Irmak Yilmaz"), "Yilmaz, Irmak")

    def test_name_with_spaces(self):
        self.assertEqual(invert_name("Irmak Yilmaz"), "Yilmaz, Irmak")

    def test_ignore_honorifics(self):
        self.assertEqual(invert_name("Ms. Irmak Yilmaz"), "Yilmaz, Irmak")

    def test_honorific_and_last_name(self):
        self.assertEqual(invert_name("Ms. Yilmaz"), "Yilmaz")

    def test_keep_post_nominal_suffixes(self):
        self.assertEqual(invert_name("Irmak Yilmaz III"), "Yilmaz, Irmak III")

if __name__ == "__main__":
    unittest.main()