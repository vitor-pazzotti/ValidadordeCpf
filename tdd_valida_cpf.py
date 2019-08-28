import unittest
from validacpf_vitor import retira_formatacao
from validacpf_vitor import validar_cpf

class TestStringMethods(unittest.TestCase):

    def testeFormatacao(self):
        self.assertEqual(
            retira_formatacao('123,456.789/01'),
            ('12345678901'))

        self.assertEqual(
            retira_formatacao('AJKL1234MNOQ'),
            ('Passe valores válidos para CPF.'))
        
        self.assertEqual(
            retira_formatacao('asgkjddn'),
            ('Passe valores válidos para CPF.'))
        self.assertEqual(
            retira_formatacao(''),(''))
        self.assertEqual(
            retira_formatacao('-----------'),
            ('Passe valores válidos para CPF.'))
        self.assertEqual(
            retira_formatacao(' 123.456.789-01'),
            ('123.456.789-01'))
    def testeValidacao(self):
        self.assertEqual(validar_cpf('11111111111'),False)

        self.assertEqual(validar_cpf('123'),False)

        self.assertEqual(validar_cpf(''), False)

        self.assertEqual(validar_cpf('aaaaBs'), False)

if __name__ == "__main__":
    unittest.main()
    