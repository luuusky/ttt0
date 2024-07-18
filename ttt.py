def print_board(board):
  print("---------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(cell, end="|")
    print()
  print("---------")
def get_player_move(player):
  while True:
    try:
      move = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
      if 0 <= move <= 8 and board[move // 3][move % 3] == " ":
        return move
      else:
        print("Неверный ход. Попробуйте снова.")
    except ValueError:
      print("Неверный ввод. Введите число.")
def check_win(board):
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return board[0][col]
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]
  if all(cell != " " for row in board for cell in row):
    return "Ничья"
  return None
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
while True:
  print_board(board)
  move = get_player_move(current_player)
  board[move // 3][move % 3] = current_player
  winner = check_win(board)
  if winner:
    print_board(board)
    if winner == "Ничья":
      print("Ничья")
    else:
      print(f"Игрок {winner} победил")
    break
  current_player = "O" if current_player == "X" else "X"