
# %%
import chess
import chess.pgn

board = chess.Board()

board.legal_moves

# %%
pgn = open("data/game1.pgn", encoding="utf-8-sig")

first_game = chess.pgn.read_game(pgn)
first_game.errors

# %%
