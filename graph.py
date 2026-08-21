import matplotlib.pyplot as plt

# 8-Queens solution
#board = [0, 4, 7, 5, 2, 6, 1, 3]//problem1
board = [1,6,9,0,2,3,4,5]#problem2
fig, ax = plt.subplots(figsize=(6, 6))

# Draw chessboard
for row in range(8):
    for col in range(8):

        # Alternate square colors
        color = "white" if (row + col) % 2 == 0 else "gray"

        ax.add_patch(
            plt.Rectangle(
                (col, row),
                1,
                1,
                facecolor=color
            )
        )

        # Draw queen
        if board[col] == row:
            ax.text(
                col + 0.5,
                row + 0.5,
                "♛",
                fontsize=35,
                ha="center",
                va="center"
            )

# Set board limits
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

# Put labels on chessboard
ax.set_xticks(range(8))
ax.set_yticks(range(8))

ax.set_xticklabels(range(1, 9))
ax.set_yticklabels(range(1, 9))

ax.set_xlabel("Column")
ax.set_ylabel("Row")

ax.set_title("8-Queens Solution")

plt.show()


import matplotlib.pyplot as plt

def plot_board(board):

    fig, ax = plt.subplots(figsize=(6, 6))

    for row in range(8):
        for col in range(8):

            color = "white" if (row + col) % 2 == 0 else "gray"

            ax.add_patch(
                plt.Rectangle(
                    (col, row),
                    1,
                    1,
                    facecolor=color
                )
            )

            if board[col] == row:
                ax.text(
                    col + 0.5,
                    row + 0.5,
                    "♛",
                    fontsize=35,
                    ha="center",
                    va="center"
                )

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    ax.set_xticks(range(8))
    ax.set_yticks(range(8))

    ax.set_xticklabels(range(1, 9))
    ax.set_yticklabels(range(1, 9))

    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    ax.set_title("8-Queens Solution")

    plt.show()


# Example individual
board = [0, 4, 7, 5, 2, 6, 1, 3]

plot_board(board)