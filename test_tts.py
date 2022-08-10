import chess.svg
import chess
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(voices[0].id)

engine.setProperty('rate', 150)
engine.say("Hello, How are you ?")
engine.runAndWait()

board = chess.Board()
board
board.push_uci("e2e4")
chess.svg.board(board, size=350)