# -*- coding: utf-8 -*-

"""

knapsack.py - CS6515, Intro to Graduate Algorithms

Implement a Dynamic Programming Solution to the knapsack problem.   The program will be given a set
of items and a weight limit, and it should select the combination of items which achieves the highest
value without exceeding the weight limit.   Each item may only be selected once (non-repeating).

"""
import argparse  # argparse allows the parsing of command line arguments
import GA_ProjectUtils as util  # utility functions for cs 6515 projects


def initTable(numItems, maxWt):
    """
    Initialize the table to be used to record the best value possible for given
    item idx and weight
    NOTE : this table must:
              -- be 2 dimensional (i.e. T[x][y])
              -- contain a single numeric value (no tuples or other complicated abtract data types)
    """

    # T = [0][0]
    T = []
    n = numItems
    B = maxWt
    # T = [[0 for b in range(B+1)] for i in range(n + 1)]
    # T = [[0 for b in range(B+1)] for i in range(n)]
    # print(T)
    for i in range(0, n + 1):
        # for i in range(1, n):
        i_row = []
        for b in range(0, B + 1):
            # for b in range(0, B):
            i_row.append(0)
        T.append(i_row)
    # print("what is the length of T or is the # of rows? \n", len(T))
    # print("what is the length of T[0] or is the # of T[0] rows? \n", len(T[0]))
    # print("what is the length of T[0] or is the # of T[1] rows? \n", len(T[1]))
    # print("what is T[0] \n", T[0])
    # print("what is T[0][1] \n", T[0][1])
    # print("what is T[1][1] \n", T[1][1])
    return T


def buildItemIter(numItems):
    """
    Build item iterator - iterator through all available items
        numItems : number of items
    """
    # n = numItems
    # return n
    return range(1, numItems + 1)
    # return range(0, numItems)


def buildWeightIter(maxWt):
    """
    Build weight iterator - iterator of all possible integer weight values
        maxWt : maximum weight available
    """
    # B = maxWt
    # return B
    return range(1, maxWt + 1)
    # return range(0, maxWt)


def subProblem(T, iterWt, itemIDX, itemWt, itemVal):
    """
    Define the subproblem to solve for each table entry - set the value to be maximum for a given
    item and weight value
        T : the table being populated
        iterWt : weight from iteration through possible weight values
        itemIDX : the index of the item from the loop iteration
        itemWt : the weight of the item
        itemVal : the value of the item
    """
    b = iterWt
    i = itemIDX
    w_i = itemWt
    v_i = itemVal
    # print("what are these things \nT: ", T, "\niterWt: ",iterWt, "\nitemIDX: ", itemIDX, "\n itemWt: ", itemWt, "\n itemVal: ", itemVal)
    # print("what are these things \niterWt: ", iterWt, "\nitemIDX: ", itemIDX, "\n itemWt: ", itemWt,
    #       "\n itemVal: ", itemVal)
    # print("what is T: \n", T)
    # if cntr_check == 0:
    #     print("This is the table at the start:\n", T)
    # elif cntr_check > 1:
    #     print("This is the table at second outer loop attempt:\n", T)
    if i == 0 or b == 0:
        # # # if T[i][0] == 0:
        # if T[i][0] == 0 or T[0][b] == 0:
        # T[i][b] = 0
        new_T_i_b = 0
    elif w_i <= b:
        # if w_i <= b:
        # T[i, b] = max((v_i + T[i-1, b-w_i]), T[i-1, b])
        # print("what is w_i: \n", w_i)
        # print("what is v_i: \n", v_i)
        # print("what is b: \n", b)
        # print("what is i: \n", i)
        # print("what is T[i][b]: \n", T[i][b])
        # print("what was T[i-1][b]: \n", T[i-1][b])
        # print("what was T[i][b]? ", T[i][b])
        # T[i][b] = max(v_i + T[i-1][b-w_i], T[i-1][b])
        new_T_i_b = max(v_i + T[i - 1][b - w_i], T[i - 1][b])
        # print("what is T[i][b]? ", T[i][b])
        # if b == 1:
        #     print("if statement check")
        #     print("what is b: \n", b)
        #     print("what is w_i: \n", w_i)
        #     print("what is v_i: \n", v_i)
        #     print("what is b: \n", b)
        #     print("what is i: \n", i)
        #     print("what is T[i][b]: \n", T[i][b])
        #     print("what was T[i-1][b]: \n", T[i-1][b])
        #     print("what is T[1][1]? ", T[1][1])
        # print("what is T[i-1][b]? ", T[i-1][b])
    else:
        # T[i, b] = T[i-1, b]
        # print("am i geting past here? else start")
        # print("'else' what is w_i: \n", w_i)
        # print("'else' what is v_i: \n", v_i)
        # print("'else' what is b: \n", b)
        # print("'else' what is i: \n", i)
        # print("'else' what was T[i][b]? ", T[i][b])
        # print("'else' what was T[i-1][b]? ", T[i-1][b])
        # if b == 1:
        #     print("if statement check")
        #     print("'else' what is b: \n", b)
        #     print("'else' what is w_i: \n", w_i)
        #     print("'else' what is v_i: \n", v_i)
        #     print("'else' what is b: \n", b)
        #     print("'else' what is i: \n", i)
        #     print("'else' what was T[i-1][b]: \n", T[i-1][b])
        #     print("'else' what was T[1][1]? ", T[1][1])
        #     print("'else' what was T[i][b]: \n", T[i][b])
        # T[i][b] = T[i-1][b]
        new_T_i_b = T[i - 1][b]
        # if b == 1:
        #     print("if statement check")
        #     print("'else' what is T[i][b]: \n", T[i][b])
        #     print("'else' what is T[1][1]? ", T[1][1])
        # print("'else' what is T[i][b]? ", T[i][b])
        # print("'else' what is T[1][1]? ", T[1][1])
        # print("'else' what is T[i-1][b]? ", T[i-1][b])
        # print("am i geting past here? else end")
    # if b == 400 and i > 20:
    #     print("last T entry \n", T[i][b])
    return new_T_i_b  # T[i][b]
    # return T[0][0]


def buildResultList(T, items, maxWt):
    """
    Construct list of items that should be chosen.
        T : the populated table of item values, indexed by item idx and weight
        items : list of items
        maxWt : maximum weight allowed

    	result: a list composed of item tuples
    """
    result = []

    B = maxWt
    b = B
    t = len(items)
    # print("what is the T? \n", T)
    # print("what is the length of T or is the # of rows? \n", len(T))
    # print("what is the length of T[0] or is the # of T[0] col? \n", len(T[0]))
    # print("what is the length of items: ", len(items))
    # bot_right = T[len(items)][B]
    # bot_right = T[-1][-1]
    # print("why doesn't this work T[len(items)]", T[len(items)-1])
    # print("why doesn't this work T[:][B]", T[:][B])
    # print("what is the table at T[n][B]: ", T[-1][-1])
    # print("what is the table at T[len(items)][B]: ", T[len(items)][-1])
    # print("what are the items: ", items)
    # print("what are the length of items list: ", n)
    # print("what is the max weight: ", B)
    # last_item = T[-1][-1]
    # bot_right = T[len(items)][B]
    # print("first bottom right ", bot_right)
    forloop_cntr = 0
    dummy_t = 0
    ####### try the while set t == 22, b is 400
    while t > 0 and b > 0:
        # for t in range(len(items), 0, -1):
        # if bot_right >= 0:
        # print('which item am i on? ', items[t])
        # print("what is t ", t, "\nb? ", b, "\nT[t][b] is ", T[t][b])
        # if T[t][b] <= 0:
        # print("what is bottom right ?", bot_right)
        # print("what is b ?", b)
        # print("what is T[t][b]? ", T[t][b])
        # print("what is T[t-1][b]? ", T[t - 1][b])
        # print("what is T[t][b-1]? ", T[t][b - 1])
        # if bot_right <= 0:
        # if you get to the top left, break
        # break
        if T[t][b] == T[t - 1][b]:
            # elif bot_right == T[t-1][b]:
            # if bot_right == T[t-1][b]:
            # if the row above in the same column is equal, the last object wasn't chosen.
            # print("what was bot right, ", T[t][b])
            # print("what was one above bot right, ", T[t-1][b])
            # print("skipping ?")
            # continue
            # print("previous row @ same weight is the same")
            t -= 1
            # result.append(tuple(items[t - 1]))
            # item_wt = items[t - 1][2]
            # item_val = items[t - 1][1]
            # b = b - item_wt
            # t -= 1
            # bot_right = bot_right - item_val
            # print("what is items at \nt ", items[t], "and items at \nt-1 ", items[t-1])
            # # result.append(tuple(items[t-1]))
            # result.append(items[t - 1])
            # print("this is what the result list is like ", result)
            # item_wt = items[t-1][2]
            # b = b - item_wt
        # elif bot_right == T[t][b - items[t][2]]:
        else:
            # print("'else': what was bot right, ", T[t][b])
            # print("'else': what was one above bot right, ", T[t-1][b])
            # result.append(tuple(items[t]))
            # print("previous row @ same weight is NOT the same")
            result.append(items[t])
            # print("'else': this is what the result list is like ", result)
            # print("do i know how to find the weight? items[t]", items[t])
            # print("do i know how to find the weight? items[t][0]", items[t][0])
            # print("do i know how to find the weight? items[t][1]", items[t][1])
            # print("do i know how to find the weight? items[t][2]", items[t][2])
            # print("do i know how to find the weight? items[t][-1]", items[t][2])
            # print("do i know how to find the weight? items[t][len(items[[t])-1]", items[t-1][len(items[t-1])-1])
            # item_wt = items[t][len(items[t])-1]
            item_wt = items[t][1]
            ########## weight is first, value is second
            item_val = items[t][2]
            # print("b at first ", b)
            b = b - item_wt
            t -= 1
            # print("b at second ", b)
            # bot_right = T[t-1][b]
            # bot_right = bot_right - item_val
        # forloop_cntr += 1
        # print("the for loop counter is at ", forloop_cntr, "\n and the value of t is ", t)
    # print("result is \n", result)
    return result


def knapsack(items, maxWt):
    """
    Solve the knapsack problem for the passed list of items and max allowable weight
    DO NOT MODIFY THE FOLLOWING FUNCTION
    NOTE : There are many ways to solve this problem.  You are to solve it
            using a 2D table, by filling in the function templates above.
            If not directed, do not modify the given code template.
    """
    numItems = len(items)
    # initialize table properly
    table = initTable(numItems, maxWt)
    # build iterables
    # item iterator
    itemIter = buildItemIter(numItems)
    # weight iterator
    weightIter = buildWeightIter(maxWt)

    for itmIdx in itemIter:
        # query item values from list
        item, itemWt, itemVal = items[itmIdx]
        for w in weightIter:
            # expand table values by solving subproblem
            table[itmIdx][w] = subProblem(table, w, itmIdx, itemWt, itemVal)

    # build list of results - chosen items to maximize value for a given weight
    return buildResultList(table, items, maxWt)


def main():
    """
    The main function
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    # You may change default values, but any values you set will be overridden when autograded
    parser = argparse.ArgumentParser(description='Knapsack Coding Quiz')
    parser.add_argument('-i', '--items', help='File holding list of possible Items (name, wt, value)',
                        default='defaultItems.txt', dest='itemsListFileName')
    parser.add_argument('-w', '--weight', help='Maximum (integer) weight of items allowed', type=int, default=400,
                        dest='maxWeight')

    # args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName', help='Student name, used for autograder', default='GT', dest='studentName')
    parser.add_argument('-a', '--autograde', help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2],
                        default=1, dest='autograde')
    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE
    itemsList = util.buildKnapsackItemsDict(args)
    itemsChosen = knapsack(itemsList, args.maxWeight)
    util.displayKnapSack(args, itemsChosen)


if __name__ == '__main__':
    main()
