# Hash Tables Project

This project is a collection of C functions that implement various operations on hash tables. A hash table is a fundamental data structure that allows for efficient key-value storage and retrieval.

## Table of Contents

- [Tasks](#tasks)
    1. [Create a Hash Table](#1-create-a-hash-table)
    2. [Implement the djb2 Hash Function](#2-implement-the-djb2-hash-function)
    3. [Find the Index of a Key](#3-find-the-index-of-a-key)
    4. [Add an Element to the Hash Table](#4-add-an-element-to-the-hash-table)
    5. [Retrieve a Value by Key](#5-retrieve-a-value-by-key)
    6. [Print the Hash Table](#6-print-the-hash-table)
    7. [Delete the Hash Table](#7-delete-the-hash-table)

## Tasks

### 1. Create a Hash Table

**Prototype:** `hash_table_t *hash_table_create(unsigned long int size);`

This function creates a hash table.

- `size` is the size of the array.
- Returns a pointer to the newly created hash table.
- If something went wrong, the function should return NULL.

### 2. Implement the djb2 Hash Function

**Prototype:** `unsigned long int hash_djb2(const unsigned char *str);`

This function implements the djb2 hash algorithm.

- `str` is the input string.
- Returns the hash value.

### 3. Find the Index of a Key

**Prototype:** `unsigned long int key_index(const unsigned char *key, unsigned long int size);`

This function returns the index at which a key should be stored in the hash table.

- `key` is the key.
- `size` is the size of the hash table's array.
- Uses the `hash_djb2` function.
- Returns the index.

### 4. Add an Element to the Hash Table

**Prototype:** `int hash_table_set(hash_table_t *ht, const char *key, const char *value);`

This function adds an element to the hash table.

- `ht` is the hash table to which the element will be added.
- `key` is the key (cannot be an empty string).
- `value` is the value associated with the key.
- Returns 1 if it succeeds, 0 otherwise.
- In case of collision, adds the new node at the beginning of the list.

### 5. Retrieve a Value by Key

**Prototype:** `char *hash_table_get(const hash_table_t *ht, const char *key);`

This function retrieves the value associated with a key.

- `ht` is the hash table to search.
- `key` is the key to look for.
- Returns the value associated with the element, or NULL if the key couldn't be found.

### 6. Print the Hash Table

**Prototype:** `void hash_table_print(const hash_table_t *ht);`

This function prints the contents of the hash table.

- `ht` is the hash table to print.
- Prints the key-value pairs in the order they appear in the array of the hash table.
- If `ht` is NULL, nothing is printed.

### 7. Delete the Hash Table

**Prototype:** `void hash_table_delete(hash_table_t *ht);`

This function deletes a hash table.

- `ht` is the hash table to delete.

## Usage

To use these functions, include the provided header file `hash_tables.h` and compile your code with the appropriate source files.

```c
#include <stdio.h>
#include <stdlib.h>
#include "hash_tables.h"

int main(void) {
    hash_table_t *ht;

    ht = hash_table_create(1024);
    hash_table_set(ht, "key", "value");
    char *result = hash_table_get(ht, "key");
    printf("Value: %s\n", result);
    hash_table_delete(ht);

    return (EXIT_SUCCESS);
}

