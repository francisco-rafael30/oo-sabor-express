class Livro:
    Livros = []

    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.Livros.append(self)

    def __str__(self):
        return f'Título: {self._titulo.ljust(20)} | Autor: {self._autor.ljust(20)} | Ano: {self._ano_publicacao}'
    
    @property
    def disponivel(self):
        return 'SIM' if self._disponivel else 'NÃO'

    @classmethod
    def emprestar_livro(cls, livro):
        livro._disponivel = False

    @classmethod
    def devolver_livro(cls, livro):
        livro._disponivel = True


    @classmethod
    def listar_livros(cls):
        for livro in cls.Livros:
            print(f'Título: {livro._titulo.ljust(15)} | Autor: {livro._autor.ljust(15)} | Ano: {livro._ano_publicacao.ljust(5)} | Disponível: {livro.disponivel}')
    
    @classmethod
    def verificar_disponibilidade(cls, ano):
        livros_disponiveis = []
        print('Os resultados encontrados para o ano solicitado: ')
        
        for livro in Livro.Livros:
             if livro._ano_publicacao == ano and livro.disponivel:
              livros_disponiveis.append(livro)
           
        for livro in livros_disponiveis:
             print(f'--{livro._titulo}')
        
        if len(livros_disponiveis) == 0:
           print('Sem livros disponiveis.')
    

livro1 = Livro('A arte da guerra', 'Fulano de tal', 1930)
livro2 = Livro('O colapso', 'Alguem da Silva', 1986)
livro3 = Livro('A casa de palha', 'Gabriel Toledo', 1930)
livro4 = Livro('Jornada da vida', 'Tobias Brasil', 1930)

#Livro.emprestar_livro(livro1)

#Livro.listar_livros()


Livro.verificar_disponibilidade(1986)

