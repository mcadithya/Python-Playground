# 30. Hollow Butterfly Pattern in Python
# Enter the row size for the pattern: 5
# *                 * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   * 
# * *             * * 
# *                 * 


def hollow_butterfly_pattern(rows):

    for i in range(1,rows+1):
        
        for col in range(2*rows+1):

            if col ==0:

                print("*",end = " ")


