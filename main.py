class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question("Qual é a capital da Austrália?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n(d) Perth\n\n", "c"),
    Question("Quem descobriu a gravidade quando uma maçã caiu em sua cabeça?\n(a) Isaac Newton\n(b) Albert Einstein\n(c) Galileu Galilei\n(d) Nikola Tesla\n\n", "a"),
    Question("Qual é o maior planeta do Sistema Solar?\n(a) Terra\n(b) Júpiter\n(c) Marte\n(d) Vênus\n\n", "b"),
    Question("Qual é o maior osso do corpo humano?\n(a) Fêmur\n(b) Úmero\n(c) Escápula\n(d) Crânio\n\n", "a"),
    Question("Quantos elementos químicos existem na tabela periódica?\n(a) 92\n(b) 118\n(c) 104\n(d) 109\n\n", "b"),
    Question("Quem escreveu a famosa peça de teatro 'Romeu e Julieta'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n(d) Ernest Hemingway\n\n", "a"),
    Question("Qual é o maior oceano do mundo?\n(a) Oceano Índico\n(b) Oceano Atlântico\n(c) Oceano Pacífico\n(d) Oceano Ártico\n\n", "c"),
    Question("Quem pintou a famosa obra 'Mona Lisa'?\n(a) Michelangelo\n(b) Leonardo da Vinci\n(c) Vincent van Gogh\n(d) Pablo Picasso\n\n", "b"),
    Question("Qual é a fórmula química da água?\n(a) H2O\n(b) CO2\n(c) NH3\n(d) O2\n\n", "a"),
    Question("Qual é o país mais populoso do mundo?\n(a) Brasil\n(b) Estados Unidos\n(c) Rússia\n(d) China\n\n", "d")
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
