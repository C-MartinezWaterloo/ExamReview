#include <stdlib.h>
#include <stdio.h>
#include "ArrayList.h"

void create_circular_queue(CA **circular, int size){
    *circular = (CA *)malloc(sizeof(CA));
    (*circular)->arr = malloc(sizeof(int) * size);
    (*circular)->capacity = size;
    (*circular)->size = 0;
    (*circular)->start = 0;
    (*circular)->end = 0;
}

void enqueue(CA *circular, int element){
    if(circular->size >= circular->capacity){
        printf("Queue is full, cannot add another element\n");
        return;
    }

    circular->arr[circular->end] = element;
    circular->end = (circular->end + 1) % circular->capacity;
    circular->size++;
    printf("Element has been enqueued\n");
}

int dequeue(CA *circular){
    if (circular->size == 0) {
        printf("Queue is empty\n");
        return -1;  // optional error code
    }

    int elem = circular->arr[circular->start];
    circular->arr[circular->start] = 0;
    circular->start = (circular->start + 1) % circular->capacity;
    circular->size--;
    return elem;
}

void printQueue(CA *circular){
    int size = circular->size;
    int start = circular->start;

    for(int i = 0; i < size; i++){
        int index = (start + i) % circular->capacity;
        printf("%d ", circular->arr[index]);
    }
    printf("\n");
}




