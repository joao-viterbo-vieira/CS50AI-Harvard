# CS50AI - Introduction to Artificial Intelligence with Python

This repository contains my solutions to projects from Harvard University's CS50's Introduction to Artificial Intelligence with Python course. The course explores modern AI concepts and implementations, from search algorithms to neural networks and large language models. 

Through hands-on projects, I gain exposure to the theory behind graph search algorithms, classification, optimization, machine learning, large language models, and other topics in artificial intelligence as I incorporate them into my own Python programs. By the end of the course, I emerge with experience in libraries for machine learning as well as knowledge of artificial intelligence principles that enable me to design intelligent systems of my own.

## Certificate of Completion

I have successfully completed Harvard University's CS50's Introduction to Artificial Intelligence with Python course. The certificate is included in this repository as `CS50AI_Certificate.pdf`.

![CS50 AI Certificate](CS50AI_Certificate.png)

*Note: To view the certificate, please open the PDF file in a PDF viewer. GitHub may not display the PDF preview directly in the repository view.*


## Course Overview

CS50 AI teaches the concepts and algorithms at the foundation of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, and machine translation.

## Weekly Topics

### Week 0: Search
- Concepts: Agents, state spaces, search algorithms, adversarial search
- Projects: Degrees, Tic-Tac-Toe

**Degrees**: This project implements a "Six Degrees of Kevin Bacon" concept using search algorithms. The goal is to find the shortest path between any two actors through movies they've appeared in. 

**Tic-Tac-Toe**: An AI that plays Tic-Tac-Toe optimally using the Minimax algorithm with Alpha-Beta pruning.

### Week 1: Knowledge
- Concepts: Knowledge-based agents, propositional logic, inference, first-order logic
- Projects: Knights, Minesweeper

**Knights**: This project solves "Knights and Knaves" logic puzzles using propositional logic. The puzzles involve characters who either always tell the truth (Knights) or always lie (Knaves), and the AI uses model checking to determine which characters are which based on their statements.

**Minesweeper**: An AI that plays Minesweeper by making logical deductions about mine locations. Using propositional logic and inference rules, the AI identifies safe moves and mine locations based on the information revealed as the game progresses

### Week 2: Uncertainty
- Concepts: Probability, Bayes' Rule, Bayesian Networks, Markov Models
- Projects: PageRank, Heredity

**PageRank**: This project implements the PageRank algorithm used by search engines to rank web pages. Using both a random surfer model and an iterative calculation approach, the AI determines the relative importance of web pages based on the link structure of the web.

**Heredity**: This project uses Bayesian Networks to model genetic inheritance of traits. The AI calculates the probability of individuals having certain genes based on their family relationships and known gene distributions, demonstrating how probability models can reason about uncertain outcomes.

### Week 3: Optimization
- Concepts: Local search, linear programming, constraint satisfaction
- Projects: Crossword, Scheduling

**Crossword**: This project uses constraint satisfaction techniques to generate valid crossword puzzles. The AI formulates the problem as variables (words in the grid), domains (possible words from a vocabulary), and constraints (word overlaps and lengths), then applies backtracking search to find a valid solution that satisfies all requirements.

**Scheduling**: This project tackles the problem of creating optimal schedules given a set of constraints. Using local search algorithms like hill climbing, the AI finds solutions that minimize conflicts and optimize resource allocation, demonstrating how optimization techniques can solve complex planning problems.

### Week 4: Learning
- Concepts: Supervised learning, reinforcement learning, unsupervised learning
- Projects: Shopping, Nim

**Shopping**: This project uses supervised learning to predict whether online shopping customers will complete a purchase. Using a nearest-neighbor classifier trained on customer browsing data, the AI learns patterns in user behavior to make accurate predictions about conversion rates, demonstrating how machine learning can extract insights from user data.

**Nim**: This project implements reinforcement learning to train an AI to play Nim, a mathematical game of strategy. Using Q-learning, the AI learns an optimal strategy through repeated gameplay and exploration, illustrating how reinforcement learning allows systems to improve through experience without explicit programming.

### Week 5: Neural Networks
- Concepts: Neural networks, deep learning, computer vision
- Projects: Traffic (Traffic Sign Recognition)

**Traffic**: This project implements a convolutional neural network to recognize traffic signs. Using TensorFlow and computer vision techniques, the AI learns to classify traffic sign images into different categories, demonstrating how neural networks can be trained to understand visual information and make accurate predictions even with complex image data.

### Week 6: Language
- Concepts: Natural language processing, n-grams, Attention, Transformers, Markov models, Naive Bayes, word representations, LLMs
- Projects: Parser, Attention

**Parser**: This project implements a natural language parser using context-free grammar techniques. The AI processes English sentences to extract noun phrases and syntactic structure, demonstrating how computational linguistics algorithms can transform unstructured text into structured representations that capture meaning relationships between words.

**Attention**: This project explores attention mechanisms in neural networks for natural language processing. Using **transformer-based architectures**, the AI learns to focus on relevant parts of input text when generating responses or translations, demonstrating how modern language models can capture contextual relationships in text data.

