# HashTable_Implementation
HELLO!! This is Mehad Naveed , This Project is for our course Data Structure and Algorithm (CS211).
In this project I implement Hash Table by Open Addressing and Chaining Method.

HashTable:
A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values.
Where,
	Keys are Student Id,
	Values are Student Names

So we,
Distribute the keys uniformly into buckets.
n: number of keys.
m: number of buckets / size of array.
h(x) = n % m   ( modulo operator )

If Collision occurs due to mapping we use 2 methods for resolving:

Collision resolution with chaining:

we put multiple entries into the same slot with the help of a linked list.
If there are many collisions: O(1) complexity gets worse !!.
It has an additional memory cost due to the references.

Collision resolution with open addressing:

Collision resolution with open addressing is better solution.If collision occurs, we find an empty slot instead.
Linear probing:
              if a collision occures, we try the next slot. if there is a collision too we keep trying the next slot until we find an empty slot.
Quadratic probing:
                we trying slots 1,2,4,8… units far away.
Rehashing: 
              we hash the result again in order to find an empty slot.



	Average	Worst case
Space	O(n)	O(n)
Search	O(1)	O(n)
Insert	O(1)	O(n)
Delete	O(1)	O(n)
