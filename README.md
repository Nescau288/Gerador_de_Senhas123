# Gerador_de_Senhas123

Nos acostumamos a usar a mesma senha para tudo — e isso é uma baita vulnerabilidade. Basta um site ser comprometido para que sua senha esteja na mão de alguém mal-intencionado, e aí... game over, né?

Este gerador de senhas em Python foi criado justamente para evitar que você caia nessa armadilha.

## 🚨 Por que usar?

Usar a mesma senha em todo lugar é pedir para ser invadido. Se um site for comprometido e sua senha vazar, o estrago pode ser geral. Este projeto cria **senhas únicas e fortes** com base em:

- O nome do site onde será usada
- Uma "semente" de 3 dígitos que só você conhece

## 🧠 Como funciona?

O algoritmo:

1. Usa uma mistura de letras, números e símbolos (o alfabeto "louco" 😵)
2. Aplica uma cifra de César adaptada (baseada na semente + posição da letra)
3. Insere até 3 símbolos aleatórios para dar entropia extra
4. Garante pelo menos uma letra maiúscula e uma minúscula
5. Limita a senha entre **8 e 12 caracteres**, e anexa a semente no final