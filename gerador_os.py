# gerador_os.py
from pylatex import Document, Section, Tabular, LineBreak, Command
from pylatex.utils import NoEscape

def gerar_ordem_servico(nome_cliente, veiculo, servicos, total):
    # Configuração do documento
    doc = Document()
    doc.preamble.append(Command('title', 'Ordem de Serviço'))
    doc.preamble.append(Command('author', 'Oficina Mecânica'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    
    # Seção: Dados do cliente
    with doc.create(Section('Dados do Cliente')):
        doc.append(f'Nome: {nome_cliente}')
        doc.append(LineBreak())
        doc.append(f'Veículo: {veiculo}')
    
    # Seção: Serviços realizados
    with doc.create(Section('Serviços Realizados')):
        with doc.create(Tabular('|l|l|r|')) as table:
            table.add_hline()
            table.add_row(('Descrição', 'Quantidade', 'Preço (R$)'))
            table.add_hline()
            for servico in servicos:
                table.add_row((servico['descricao'], servico['quantidade'], f"{servico['preco']:.2f}"))
            table.add_hline()
    
    # Seção: Total
    with doc.create(Section('Total')):
        doc.append(f'Valor Total: R$ {total:.2f}')
    
    # Gerar PDF
    doc.generate_pdf('nome_do_arquivo', compiler='pdflatex', clean_tex=False)

