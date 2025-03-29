#ifndef CA
#define CA

typedef struct CircularArray {
    int *arr;
    int size;      // current number of elements
    int capacity;  // total capacity
    int start;     // index of front
    int end;       // index of next insert position
} CA;

void create_circular_queue(CA **circular, int size);

void enqueue(CA *circular, int element);

void dequeue(CA *circular);

void printQueue(CA *circular);

#endif











