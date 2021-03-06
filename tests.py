import unittest

import bip39


class MyTestCase(unittest.TestCase):
    mnemonic = "daughter song common combine misery cotton audit morning stuff weasel flee field"
    mini_secret = [49, 98, 91, 191, 124, 49, 124, 0, 208, 99, 248, 41, 196, 131, 195, 96, 115, 127, 171, 82, 16, 205,
                   187, 45, 20, 195, 40, 22, 91, 21, 209, 128]
    seed = [97, 142, 41, 83, 73, 179, 98, 128, 176, 134, 250, 222, 64, 184, 51, 176, 121, 119, 215, 115, 220, 77, 28,
            15, 253, 64, 10, 1, 213, 54, 239, 124]

    def test_generate_mnemonic(self):
        mnemonic = bip39.bip39_generate(12)
        self.assertTrue(bip39.bip39_validate(mnemonic))

    def test_generate_invalid_mnemonic(self):
        self.assertRaises(ValueError, bip39.bip39_generate, 13)

    def test_validate_mnemonic(self):
        self.assertTrue(bip39.bip39_validate(self.mnemonic))

    def test_invalidate_mnemonic(self):
        self.assertFalse(bip39.bip39_validate("Invalid mnemonic"))

    def test_mini_seed(self):
        self.assertEqual(self.mini_secret, bip39.bip39_to_mini_secret(self.mnemonic, ''))

    def test_seed(self):
        self.assertEqual(self.seed, bip39.bip39_to_seed(self.mnemonic, ''))


if __name__ == '__main__':
    unittest.main()
