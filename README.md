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

## Day 15 Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]

Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Day 16 Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

Note: The string size will be in the range [1, 100].

## Day 17 Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

## Day 18 Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

## Day 19 Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

## Day 20 Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Note: 
* 1 <= preorder.length <= 100
* The values of preorder are distinct.

## Day 21 Leftmost Column with at Least a One
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

* BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
* BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

Constraints:
* 1 <= mat.length, mat[i].length <= 100
* mat[i][j] is either 0 or 1.
* mat[i] is sorted in a non-decreasing way.

Hint #1  
1. (Binary Search) For each row do a binary search to find the leftmost one on that row and update the answer.

Hint #2  
2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner. p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. Try to figure out the correctness and time complexity of this algorithm.

## Day 22 Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2

Output: 2

Note:
* The length of the array is in range [1, 20,000].
* The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Hint #1  
Will Brute force work here? Try to optimize it.

Hint #2  
Can we optimize it by using some extra space?

Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?

Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

## Day 23 Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

## Day 24 LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:

Could you do both operations in O(1) time complexity?

## Day 25 Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

* Example 1:
* Input: [2,3,1,1,4]
* Output: true
* Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Day 26 Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Constraints:
* 1 <= text1.length <= 1000
* 1 <= text2.length <= 1000
* The input strings consist of lowercase English characters only.

## Day 27 Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

## Day 28 First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:
* FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
* int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
* void add(int value) insert value to the queue.
 
Constraints:
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^8
* 1 <= value <= 10^8
* At most 50000 calls will be made to showFirstUnique and add.
 
## Day 29
## Day 30
