# 🎰 Impossible Game

Um mini game interativo estilo cassino, onde dois jogadores tentam adivinhar o mesmo número gerado pela máquina.

## 🚀 Funcionalidades

* 🎮 Sistema de turnos (Player 1 e Player 2)
* 🎰 Animação estilo slot machine
* 🎯 Número aleatório de **1 a 100**
* 📊 Contador de tentativas com banco de dados
* 🔒 Jogabilidade justa (sem ver a escolha do outro jogador)

---

## 🧠 Como funciona

1. Player 1 escolhe um número (1 a 100)
2. O valor é escondido
3. Player 2 escolhe outro número
4. A máquina gera um número aleatório
5. Ambos ganham apenas se:

   * Player 1 == Player 2 == Máquina

---

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* SQLite
* HTML, CSS, JavaScript

---

## ▶️ Como rodar o projeto

### 🔹 Backend

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

### 🔹 Frontend

Abra o arquivo:

```
frontend/index.html
```

---

## 📊 Endpoints

### POST /game

Executa uma rodada do jogo

**Parâmetros:**

* player1 (int)
* player2 (int)

---

### GET /tries

Retorna o número total de tentativas

---

## 📌 Melhorias futuras

* Ranking de jogadores
* Histórico de partidas
* Sistema de login
* Deploy online
* Multiplayer real

---

## 👨‍💻 Autor

valdsoares360

---

## ⭐ Se curtir o projeto, deixa uma estrela!
