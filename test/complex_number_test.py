import unittest

from complex_number import PurelyImaginaryNumber, DefaultPurelyImaginaryNumberStringSerializer, NonZeroIntegerNormalizer


class TestPurelyImaginaryNumber(unittest.TestCase):

    def test___eq__(self):
        with self.subTest("虚部が同じ純虚数型のオブジェクトを同一と判定すること"):
            self.assertEqual(PurelyImaginaryNumber(2), PurelyImaginaryNumber(2))

        with self.subTest("虚部が違う純虚数型のオブジェクトを不同と判定すること"):
            self.assertNotEqual(PurelyImaginaryNumber(2), PurelyImaginaryNumber(3))

    def test_conjugate(self):
        with self.subTest("共役な純虚数オブジェクトを生成すること"):
            self.assertEqual(PurelyImaginaryNumber(-2), PurelyImaginaryNumber(2).conjugate())

    def test_delegation_to_other_objects(self):
        with self.subTest("normalizerがエラーをスローする引数で純虚数オブジェクトを作成できないこと"):
            with self.assertRaises(ValueError):
                PurelyImaginaryNumber(0)

        with self.subTest("serializerに従って純虚数オブジェクトが文字列に変換されること"):
            self.assertEqual("2i", str(PurelyImaginaryNumber(2)))


class TestDefaultPurelyImaginaryNumberStringSerializer(unittest.TestCase):

    def test_serialize(self):
        with self.subTest("虚部が1か-1以外の場合は虚部を省略せずに表記すること"):
            self.assertEqual("2i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(2)))

        with self.subTest("虚部が1の場合は虚部を省略して表記すること"):
            self.assertEqual("i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(1)))

        with self.subTest("虚部が-1の場合は虚部は符号のみ表記すること"):
            self.assertEqual("-i", DefaultPurelyImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(-1)))


class TestNonZeroIntegerNormalizer(unittest.TestCase):

    def test_normalize(self):
        with self.subTest("0以外のintに変換できるオブジェクトをintに変換すること"):
            self.assertEqual(1, NonZeroIntegerNormalizer.normalize('1'))

        with self.subTest("0が渡された場合にエラーをスローすること"):
            with self.assertRaises(ValueError):
                NonZeroIntegerNormalizer.normalize(0)


if __name__ == "__main__":
    unittest.main()
