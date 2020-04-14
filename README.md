# LeetCode 30 days challenge
https://leetcode.com/discuss/general-discussion/551411/30-day-leetcoding-challenge

## Day 1 Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Day 2 Happy Number
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

## Day 3 Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Day 4 Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

## Day 5 Best Time to Buy and Sell Stock II
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Constraints:

1 <= prices.length <= 3 * 10 ^ 4

0 <= prices[i] <= 10 ^ 4

## Day 6 Group Anagrams
Given an array of strings, group anagrams together.

Note:

* All inputs will be in lowercase.

* The order of your output does not matter.

## Day 7 Counting Elements
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them separately.

## Day 8 Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Note: The number of nodes in the given list will be between 1 and 100.

## Day 9 Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

## Day 10 Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

getMin() -- Retrieve the minimum element in the stack.

Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

## Day 11 Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

## Day 12 Last Stone Weight
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
* If x == y, both stones are totally destroyed;
* If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Note:
1. 1 <= stones.length <= 30
2. 1 <= stones[i] <= 1000

## Day 13 Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

## Day 14 Perform String Shifts
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

* direction can be 0 (for left shift) or 1 (for right shift). 
* amount is the amount by which string s is to be shifted.
* A left shift by 1 means remove the first character of s and append it to the end.
* Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.

Constraints:

* 1 <= s.length <= 100
* s only contains lower case English letters.
* 1 <= shift.length <= 100
* shift[i].length == 2
* 0 <= shift[i][0] <= 1
* 0 <= shift[i][1] <= 100

Hint #1  
Intuitively performing all shift operations is acceptable due to the constraints.

Hint #2  
You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.
## Day 15
## Day 16
## Day 17
## Day 18
## Day 19
## Day 20
## Day 21
## Day 22
## Day 23
## Day 24
## Day 25
## Day 26
## Day 27
## Day 28
## Day 29
## Day 30
