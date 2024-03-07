from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Trạng thái mặc định của bảng
board = ['-'] * 9
current_player = 'X'
winner = None
game_over = False

def check_winner():
    global winner
    # Kiểm tra hàng ngang
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != '-':
            winner = board[i]
            return True
    # Kiểm tra cột dọc
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '-':
            winner = board[i]
            return True
    # Kiểm tra đường chéo
    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != '-':
        winner = board[2]
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html', board=board, winner=winner, game_over=game_over)

@app.route('/play/<int:position>')
def play(position):
    global board, current_player, game_over

    if not game_over and board[position] == '-':
        board[position] = current_player
        if check_winner():
            game_over = True
        elif '-' not in board:
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global board, current_player, winner, game_over
    board = ['-'] * 9
    current_player = 'X'
    winner = None
    game_over = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
