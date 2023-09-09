class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question("Qual é a capital da França?\n(a) Paris\n(b) Londres\n(c) Berlim\n(d) Roma\n\n", "a"),
    Question("Quem escreveu a obra 'Dom Quixote'?\n(a) Machado de Assis\n(b) William Shakespeare\n(c) Miguel de Cervantes\n(d) Victor Hugo\n\n", "c"),
    Question("Qual é o maior planeta do Sistema Solar?\n(a) Terra\n(b) Júpiter\n(c) Marte\n(d) Vênus\n\n", "b"),
    Question("Qual é o maior osso do corpo humano?\n(a) Fêmur\n(b) Úmero\n(c) Escápula\n(d) Crânio\n\n", "a"),
    Question("Quantos elementos químicos existem na tabela periódica?\n(a) 92\n(b) 118\n(c) 104\n(d) 109\n\n", "b"),
    Question("Quem pintou a famosa obra 'Mona Lisa'?\n(a) Michelangelo\n(b) Leonardo da Vinci\n(c) Vincent van Gogh\n(d) Pablo Picasso\n\n", "b"),
    Question("Qual é a fórmula química da água?\n(a) H2O\n(b) CO2\n(c) NH3\n(d) O2\n\n", "a"),
    Question("Qual é o país mais populoso do mundo?\n(a) Brasil\n(b) Estados Unidos\n(c) Rússia\n(d) China\n\n", "d"),
    Question("Quem foi o primeiro homem a pisar na Lua?\n(a) Buzz Lightyear\n(b) Neil Armstrong\n(c) Yuri Gagarin\n(d) Alan Shepard\n\n", "b"),
    Question("Qual é o número de lados de um triângulo?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n\n", "a"),
    Question("Qual é o instrumento musical conhecido como 'rei dos instrumentos'?\n(a) Guitarra\n(b) Violino\n(c) Piano\n(d) Trombone\n\n", "c"),
    Question("Qual é o maior deserto do mundo?\n(a) Deserto do Atacama\n(b) Deserto do Saara\n(c) Deserto de Gobi\n(d) Deserto de Kalahari\n\n", "b"),
    Question("Quem escreveu 'A Odisséia'?\n(a) Homero\n(b) Sófocles\n(c) Virgílio\n(d) Aristóteles\n\n", "a"),
    Question("Qual é o maior rio do mundo?\n(a) Rio Nilo\n(b) Rio Amazonas\n(c) Rio Mississipi\n(d) Rio Ganges\n\n", "b"),
    Question("Quem é considerado o pai da filosofia ocidental?\n(a) Sócrates\n(b) Platão\n(c) Aristóteles\n(d) Tales de Mileto\n\n", "d"),
    Question("Qual é a velocidade da luz no vácuo?\n(a) 300.000 km/s\n(b) 500.000 km/s\n(c) 1.000.000 km/s\n(d) 186.282 mi/s\n\n", "d"),
    Question("Quem foi o fundador da Microsoft?\n(a) Steve Jobs\n(b) Bill Gates\n(c) Mark Zuckerberg\n(d) Jeff Bezos\n\n", "b"),
    Question("Qual é o elemento químico mais abundante na crosta terrestre?\n(a) Ferro\n(b) Oxigênio\n(c) Silício\n(d) Alumínio\n\n", "b"),
    Question("Quem é o autor da obra 'Cem Anos de Solidão'?\n(a) Gabriel García Márquez\n(b) Pablo Neruda\n(c) Julio Cortázar\n(d) Mario Vargas Llosa\n\n", "a"),
    Question("Qual é o maior órgão do corpo humano?\n(a) Coração\n(b) Pulmões\n(c) Pele\n(d) Fígado\n\n", "c"),
    Question("Quem foi o primeiro presidente dos Estados Unidos?\n(a) Abraham Lincoln\n(b) John F. Kennedy\n(c) George Washington\n(d) Thomas Jefferson\n\n", "c"),
    Question("Qual é o segundo planeta do Sistema Solar?\n(a) Marte\n(b) Júpiter\n(c) Vênus\n(d) Saturno\n\n", "c"),
    Question("Quem escreveu a peça 'Romeu e Julieta'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n(d) Ernest Hemingway\n\n", "a"),
    Question("Qual é o menor planeta do Sistema Solar?\n(a) Marte\n(b) Júpiter\n(c) Vênus\n(d) Mercúrio\n\n", "d"),
    Question("Qual é a unidade de medida de temperatura no sistema internacional?\n(a) Grau Celsius\n(b) Fahrenheit\n(c) Kelvin\n(d) Grau Rankine\n\n", "c"),
    Question("Quem foi o líder espiritual da Índia que defendeu a não-violência?\n(a) Dalai Lama\n(b) Genghis Khan\n(c) Mahatma Gandhi\n(d) Confúcio\n\n", "c"),
    Question("Qual é o símbolo químico do oxigênio?\n(a) Ox\n(b) O2\n(c) Oxg\n(d) O\n\n", "d"),
    Question("Qual é o maior estado do Brasil em área territorial?\n(a) São Paulo\n(b) Amazonas\n(c) Minas Gerais\n(d) Bahia\n\n", "b"),
    Question("Quem foi o primeiro ser humano a viajar para o espaço?\n(a) Yuri Gagarin\n(b) Neil Armstrong\n(c) John Glenn\n(d) Buzz Aldrin\n\n", "a"),
    Question("Qual é o maior oceano do mundo?\n(a) Oceano Índico\n(b) Oceano Atlântico\n(c) Oceano Pacífico\n(d) Oceano Ártico\n\n", "c"),
    Question("Quem é considerado o 'pai da física moderna'?\n(a) Albert Einstein\n(b) Isaac Newton\n(c) Galileu Galilei\n(d) Niels Bohr\n\n", "a"),
    Question("Qual é o maior deserto do mundo?\n(a) Deserto do Atacama\n(b) Deserto do Saara\n(c) Deserto de Gobi\n(d) Deserto de Kalahari\n\n", "b"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    return score

def calculate_iq(score):
    max_score = len(questions)
    iq = (score / max_score) * 100
    return iq

def get_iq_category(iq):
    if iq >= 130:
        return "Muito superior"
    elif iq >= 120:
        return "Superior"
    elif iq >= 110:
        return "Acima da média"
    elif iq >= 90:
        return "Média"
    elif iq >= 80:
        return "Abaixo da média"
    else:
        return "Abaixo do normal"

score = run_quiz(questions)
iq = calculate_iq(score)
iq_category = get_iq_category(iq)

print(f"\nSua pontuação no teste de QI: {score}/{len(questions)}")
print(f"Seu QI é: {iq}")
print(f"Você está na categoria: {iq_category}")
