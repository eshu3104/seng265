#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "emalloc.h"

#define MAX_LINE_LEN 5000

void inccounter(Patient *p, void *arg) {
    /* DO NOT CHANGE THIS FUNCTION. */
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(Patient *p, void *arg) {
    /* DO NOT CHANGE THIS FUNCTION. */
    char *fmt = (char *)arg;
    printf(fmt, p->name, p->birth_year, p->priority);
}


void dump(Patient *list) {
    /* DO NOT CHANGE THIS FUNCTION. */
    int len = 0;

    apply(list, inccounter, &len);    
    printf("Number of patients: %d\n", len);

    apply(list, print_word, "%s,%d,%d\n");
}

Patient *tokenize_line(char *line) {
    // Command of 4 tokens
    char *commands[4]; 
    // Keep track of command
    int commandIndex = 0;
    // Delimiter for strok - ','
    const char *delimiter = ","; 

    // Tokenize
    char *token = strtok(line, delimiter);
    while (token != NULL) {
        commands[commandIndex++] = token;
        token = strtok(NULL, delimiter);
    }

    // Builds new patient if enqueue
    if (commandIndex == 4 && strcmp(commands[0], "enqueue") == 0) {
        // Extract patient data and build Patient struct
        Patient *newPatient = new_patient(commands[1], atoi(commands[2]), atoi(commands[3]));
        return newPatient;
    // Returns NULL if dequeue
    } else if (commandIndex == 1 && strcmp(commands[0], "dequeue") == 0) {
        // Return NULL for dequeue
        return NULL;
    }

    return NULL; }


Patient *read_lines(Patient *list) {
    char line[MAX_LINE_LEN];
    // Gets input stdin and tokenizes
    while (fgets(line, sizeof(line), stdin) != NULL) {
        Patient *patient = tokenize_line(line);
        if (patient != NULL) {
            list = add_with_priority(list, patient);
        } else {
            // Handle dequeue or invalid command
            list = remove_front(list);
        }
    }

    return list;
}


void deallocate_memory(Patient *list) {
    // Free memory
    while (list != NULL) {
        Patient *temp = list;
        list = list->next;
        free(temp->name);
        free(temp);
    }
}


int main(int argc, char *argv[]) {
    /* DO NOT CHANGE THE MAIN FUNCTION. YOU HAVE TO IMPLEMENT YOUR
        CODE TO FOLLOW THE SEQUENCE OF INSTRUCTIONS BELOW. */
    Patient *list = NULL;

    if (argc != 1) {
            printf("Usage: %s\n", argv[0]);
            printf("Should receive no parameters\n");
            printf("Read from the stdin instead\n");
            exit(1);
    }

    list = read_lines(list);
 
    dump(list);
    
    deallocate_memory(list);

    exit(0); 
}
