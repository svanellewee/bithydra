import unittest

"""
 dictionary = "d" 1*(string anytype) "e" ; non-empty dictionary
   list       = "l" 1*anytype "e"          ; non-empty list
   integer    = "i" signumber "e"
   string     = number ":" <number long sequence of any CHAR>
   anytype    = dictionary / list / integer / string
   signumber  = "-" number / number
   number     = 1*DIGIT
   CHAR       = %x00-FF                    ; any 8-bit character
   DIGIT      = "0" / "1" / "2" / "3" / "4" /
                "5" / "6" / "7" / "8" / "9"
"""
from bithydra.bencode import bencode, bdecode

encode = bencode
decode = bdecode

class TestBencode(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_encode(self):
        self.assertEqual(b"i123e", encode(123))
        self.assertEqual(b"i-123e", encode(-123))
        self.assertEqual(b"5:hello", encode(b"hello"))
        self.assertEqual(b"5:hello", encode("hello"))
        self.assertEqual(b"li123ee", encode([123]))
        self.assertEqual(b"li123e5:hello3:byee", encode([123, b"hello", "bye"]))
        self.assertEqual(b"li123ee", encode([123]))

        self.assertEqual(b"d5:monthi4e4:name5:aprile", encode({"month": 4, "name": "april"}))
        self.assertEqual(b'd4:thisi10e10:is spartaa4:teste', encode({"this": 10, "is spartaa": "test"}))


    def test_decode(self):
        self.assertEqual(decode(b"i-123e"), -123)
        self.assertEqual(decode(b"li123ee"), [123])
        self.assertEqual(decode(b"li123e5:hello3:byee"), [123, b"hello", b"bye"])
        self.assertEqual(decode(b"li123ee"), [123])
        self.assertEqual(decode(b"d5:monthi4e4:name5:aprile"), {b"month": 4, b"name": b"april"})
        self.assertEqual(decode(b'd4:thisi10e10:is spartaa4:teste'), {b"this": 10, b"is spartaa": b"test"})
