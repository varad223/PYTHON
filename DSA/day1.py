class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1  # Initialize both front and rear to -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, val):
        if self.is_full():
            print("Queue overflow")
        else:
            if self.front == -1:  # Handle the first element case
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = val
            print("Successfully inserted", val)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
        else:
            val = self.queue[self.front]
            if self.front == self.rear:  # Handle the only element case
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            print("Successfully deleted", val)
            return val

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements: ", end="")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.capacity
            print(self.queue[i])  # Print the last element

if __name__ == "__main__":
    capacity = 5
    q = CircularQueue(capacity)
    while True:
        print("\n1) Insert")
        print("2) Delete")
        print("3) Display")
        print("4) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            q.enqueue(val)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
