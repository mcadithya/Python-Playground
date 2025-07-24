# 29. Butterfly Pattern in Python
# Enter the row size for the pattern: 5
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 


def butterfly_pattern(n):

    # Top Half

    for i in range(1, n + 1):

        # Left stars

        print('* ' * i, end='')

        # Spaces

        print('  ' * (2 * (n - i)), end='')

        # Right stars

        print('* ' * i)

    # Bottom Half
    for i in range(n, 0, -1):

        # Left stars
        print('* ' * i, end='')

        # Spaces
        print('  ' * (2 * (n - i)), end='')

        # Right stars
        print('* ' * i)

# Input from user
rows = int(input("Enter the row size for the pattern: "))

butterfly_pattern(rows)
