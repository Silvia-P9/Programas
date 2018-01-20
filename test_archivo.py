import unittest
import archivo


class TestsBasicos(unittest.TestCase):
            
    def test_split(self):
        data=archivo.leer_archivo()
        s=data[0]
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_palabra(self):
        palabra='hello'
        self.assertEqual(1, archivo.verificar_palabra(palabra))

    def test_letra(self):
        palabra='hello5'
        self.assertEqual(5, archivo.verificar_letra(palabra))

if __name__ == '__main__':
    unittest.main()
