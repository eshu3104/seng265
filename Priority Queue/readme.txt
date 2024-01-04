Reads the input from stdin with the patients that arrive to the emergency room or leave the emergency
room, and interprets each line as either an enqueueing or a dequeueing operation;
- For each enqueueing operation with a patient that comes from stdin, adds the patient’s struct to the priority
queue (which is based on a linked list), by inserting it after all patients with higher or same priority than the
given patient;
- For each dequeueing operation from stdin, removes the first patient from the linked list;
- Dumps the ordered list of patients into stdout;
- Deallocated the dynamic memory for the linked list.

In the emergency room, higher priority means a smaller number than lower priority. For instance, a patient with
priority 1 has a higher priority than a patient with priority 2. A new patient with higher priority must come before
patients with lower priority in the linked list. Also, a new patient with the same priority as other patients must come
after those patients in the linked list, and before patients with lower priority