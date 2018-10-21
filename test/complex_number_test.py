import unittest

from complex_number import PurelyImaginaryNumber, DefaultPurelyImaginaryNumberStringSerializer, NonZeroIntegerNormalizer


class TestPurelyImaginaryNumber(unittest.TestCase):

    def test_init__validatorがinvalidと判定する引数で純虚数オブジェクトを作成できないこと(self):
        with self.assertRaises(ValueError):
            PurelyImaginaryNumber(0)

    def test_str__formatterに従って純虚数オブジェクトが文字列に変換されること(self):
        self.assertEqual("2i", str(PurelyImaginaryNumber(2)))

    def test_eq__虚部が同じ純虚数型のオブジェクトを同一と判定すること(self):
        self.assertEqual(PurelyImaginaryNumber(2), PurelyImaginaryNumber(2))

    def test_eq__虚部が違う純虚数型のオブジェクトを不同と判定すること(self):
        self.assertNotEqual(PurelyImaginaryNumber(2), PurelyImaginaryNumber(3))

    def test_conjugate__共役な純虚数オブジェクトを生成すること(self):
        self.assertEqual(PurelyImaginaryNumber(-2), PurelyImaginaryNumber(2).conjugate())


class TestDefaultPurelyImaginaryNumberStringSerializer(unittest.TestCase):

    def test_format__虚部が1かー1以外の場合は虚部を省略せずに表記すること(self):
        self.assertEqual("2i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(2)))

    def test_format__虚部が1の場合は虚部を省略して表記すること(self):
        self.assertEqual("i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(1)))

    def test_format__虚部がー1の場合は虚部は符号のみ表記すること(self):
        self.assertEqual("-i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(-1)))


class TestNonZeroIntegerNormalizer(unittest.TestCase):

    def test_validate__0以外をvalidとして判定すること(self):
        self.assertTrue(NonZeroIntegerNormalizer.normalize(1))

    def test_validate__0をinvalidとして判定すること(self):
        with self.assertRaises(ValueError):
            NonZeroIntegerNormalizer.normalize(0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
