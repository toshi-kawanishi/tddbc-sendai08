import unittest

from complex_number import ImaginaryNumber, PurelyImaginaryNumber, DefaultImaginaryNumberStringSerializer, NonZeroIntegerNormalizer


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


class TestImaginaryNumber(unittest.TestCase):

    def test___eq__(self):
        with self.subTest("実部と虚部が同じ虚数型のオブジェクトを同一と判定すること"):
            self.assertEqual(ImaginaryNumber(1, 2), ImaginaryNumber(1, 2))

        with self.subTest("実部が違う虚数型のオブジェクトを不同と判定すること"):
            self.assertNotEqual(ImaginaryNumber(1, 2), ImaginaryNumber(3, 2))

        with self.subTest("虚部が違う虚数型のオブジェクトを不同と判定すること"):
            self.assertNotEqual(ImaginaryNumber(1, 2), ImaginaryNumber(1, 3))

    def test_conjugate(self):
        with self.subTest("共役な虚数オブジェクトを生成すること"):
            self.assertEqual(ImaginaryNumber(1, -2), ImaginaryNumber(1, 2).conjugate())

    def test_delegation_to_other_objects(self):
        with self.subTest("normalizerがエラーをスローする引数を実部に与えて虚数オブジェクトを作成できないこと"):
            with self.assertRaises(ValueError):
                ImaginaryNumber(0, 1)

        with self.subTest("normalizerがエラーをスローする引数を虚部に与えて虚数オブジェクトを作成できないこと"):
            with self.assertRaises(ValueError):
                ImaginaryNumber(1, 0)

        with self.subTest("serializerに従って虚数オブジェクトが文字列に変換されること"):
            self.assertEqual("1 + 2i", str(ImaginaryNumber(1, 2)))


class TestDefaultImaginaryNumberStringSerializer(unittest.TestCase):

    def test_serialize(self):
        with self.subTest("実部と虚部がある場合"):
            with self.subTest("虚部が1以外の正数の場合は加算として表記すること"):
                self.assertEqual("1 + 2i", DefaultImaginaryNumberStringSerializer.serialize(ImaginaryNumber(1, 2)))

            with self.subTest("虚部が1の場合は虚部を省略して加算として表記すること"):
                self.assertEqual("1 + i", DefaultImaginaryNumberStringSerializer.serialize(ImaginaryNumber(1, 1)))

            with self.subTest("虚部が-1以外の負数の場合は加算として表記すること"):
                self.assertEqual("1 - 2i", DefaultImaginaryNumberStringSerializer.serialize(ImaginaryNumber(1, -2)))

            with self.subTest("虚部が-1の場合は虚部を省略して加算として表記すること"):
                self.assertEqual("1 - i", DefaultImaginaryNumberStringSerializer.serialize(ImaginaryNumber(1, -1)))

        with self.subTest("虚部のみの場合"):
            with self.subTest("虚部が1か-1以外の場合は虚部を省略せずに表記すること"):
                self.assertEqual("2i", DefaultImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(2)))

            with self.subTest("虚部が1の場合は虚部を省略して表記すること"):
                self.assertEqual("i", DefaultImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(1)))

            with self.subTest("虚部が-1の場合は虚部は符号のみ表記すること"):
                self.assertEqual("-i", DefaultImaginaryNumberStringSerializer.serialize(PurelyImaginaryNumber(-1)))


class TestNonZeroIntegerNormalizer(unittest.TestCase):

    def test_normalize(self):
        with self.subTest("0以外のintに変換できるオブジェクトをintに変換すること"):
            self.assertEqual(1, NonZeroIntegerNormalizer.normalize('1'))

        with self.subTest("0が渡された場合にエラーをスローすること"):
            with self.assertRaises(ValueError):
                NonZeroIntegerNormalizer.normalize(0)


if __name__ == "__main__":
    unittest.main()
