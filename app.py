from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Rafael', 5)
restaurante_praca.receber_avaliacao('Francisco', 8)
restaurante_praca.receber_avaliacao('Julio', 3)








def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()