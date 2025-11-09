# This function sorts a list using the bubble sort algorithm
def bubble_sort(arr):
    # Get the number of items in the list
    n = len(arr)
    
    # First loop: we need to go through the list multiple times
    # Each time we go through, one more item gets in the right place
    for i in range(n):
        # This flag helps us know if we made any swaps
        # If no swaps, the list is already sorted and we can stop early
        swapped = False
        
        # Second loop: compare each pair of neighbors
        # We don't check the last i elements because they're already sorted
        for j in range(0, n-i-1):
            # Compare current item with the next item
            # If they're in the wrong order, swap them
            if arr[j] > arr[j+1]:
                # Swap the two elements - like switching two books on a shelf
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Mark that we made a swap
                swapped = True
        
        # If we went through the whole list without swapping anything,
        # that means everything is already in order - we can stop!
        if not swapped:
            break
    
    # Return the sorted list
    return arr

# List of 15 student names
# These are in random order - not alphabetical
student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Pema", "Sonam", "Deki", "Tashi", "Karma", "Sangay", "Dorji", "Yangchen", "Lhakpa", "Chimi"]

print("Original Student Names:")
print(student_names)

# Sort the list using bubble sort
sorted_names = bubble_sort(student_names.copy())


# Show the sorted list after organizing alphabetically
print("\nSorted Student Names (Alphabetically):")
print(sorted_names)

def insertion_sort(arr):
    # Start from the second element (index 1) because the first element is already "sorted"
    for i in range(1, len(arr)):
        key = arr[i]  # This is the current score we're trying to insert in the right place
        j = i - 1     # j is the index of the last element in the sorted part
        
        # Move through the sorted part from right to left
        # Shift elements that are larger than key to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Move the larger element one position right
            j -= 1               # Move left to check the next element
        
        # We found the correct position for key - insert it here
        arr[j + 1] = key
    
    return arr

# List of 20 test scores (in random order)
test_scores = [78, 45, 92, 67, 88, 54, 73, 81, 95, 62, 49, 87, 71, 58, 83, 66, 79, 91, 53, 76]

print("Original Test Scores:")
print(test_scores)

# Sort the scores using insertion sort
# We use .copy() to keep the original list unchanged
sorted_scores = insertion_sort(test_scores.copy())

print("\nSorted Test Scores (Ascending Order):")
print(sorted_scores)

# Display top 5 scores
# Since the list is sorted from lowest to highest, the top scores are at the end of the list
print("\nTop 5 Scores:")
for i in range(1, 6):
    # sorted_scores[-1] means the last element (highest score)
    # sorted_scores[-2] means second last, and so on...
    print(f"{i}. {sorted_scores[-i]}")

# This function sorts using bubble sort - like bubbles rising in water
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if we made any swaps this round
        
        # Compare each pair of neighbors
        for j in range(0, n-i-1):
            # If they're in wrong order, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        # If no swaps, the list is already sorted - we can stop!
        if not swapped:
            break
    return arr

# This function sorts using insertion sort - like sorting cards in your hand
def insertion_sort(arr):
    # Start from second element (first element is already "sorted")
    for i in range(1, len(arr)):
        key = arr[i]  # The element we're trying to insert
        j = i - 1     # Start comparing with the element before it
        
        # Shift larger elements to the right to make space
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Move larger element right
            j -= 1               # Move left to check next element
            
        arr[j + 1] = key  # Insert our element in the correct spot
    
    return arr

# This function sorts using quick sort 
def quicksort(arr, recursive_calls=[0]):
    recursive_calls[0] += 1  # Count how many times this function calls itself
    
    # Base case: if list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose middle element as the "pivot" (comparison point)
        pivot = arr[len(arr) // 2]
        
        # Split into three groups:
        left = [x for x in arr if x < pivot]    # Elements smaller than pivot
        middle = [x for x in arr if x == pivot] # Elements equal to pivot  
        right = [x for x in arr if x > pivot]   # Elements larger than pivot
        
        # Recursively sort left and right parts, then combine
        return quicksort(left, recursive_calls) + middle + quicksort(right, recursive_calls)

# Our data sets for testing
student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Pema", "Sonam", "Deki", "Tashi", "Karma", "Sangay", "Dorji", "Yangchen", "Lhakpa", "Chimi"]
test_scores = [78, 45, 92, 67, 88, 54, 73, 81, 95, 62, 49, 87, 71, 58, 83, 66, 79, 91, 53, 76]
book_prices = [450, 230, 678, 125, 890, 345, 512, 267, 789, 156, 623, 411, 298, 534, 712]

print("=== Sorting Algorithms Menu ===")
print("Select a sorting operation (1-4):")
print("1. Bubble Sort - Sort Student Names")
print("2. Insertion Sort - Sort Test Scores") 
print("3. Quick Sort - Sort Book Prices")
print("4. Exit program")

# Main program loop
while True:
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        print("Original names:", student_names)
        # Use .copy() so we don't change the original list
        sorted_names = bubble_sort(student_names.copy())
        print("Sorted names:", sorted_names)
        
    elif choice == "2":
        print("Original scores:", test_scores)
        sorted_scores = insertion_sort(test_scores.copy())
        print("Sorted scores:", sorted_scores)
        
        # Show top 5 scores (highest scores are at the end after sorting)
        print("\nTop 5 Scores:")
        for i in range(1, 6):
            # Use negative indexing: -1 = last element, -2 = second last, etc.
            print(f"{i}. {sorted_scores[-i]}")
            
    elif choice == "3":
        print("Original prices:", book_prices)
        # We use a list to count recursive calls (lists are mutable)
        recursive_count = [0]
        sorted_prices = quicksort(book_prices.copy(), recursive_count)
        print("Sorted prices:", sorted_prices)
        print(f"Recursive calls: {recursive_count[0]}")
        
    elif choice == "4":
        print("Thank you for using the sorting program!")
        break  # Exit the loop and end program
        
    else:
        print("Please enter 1-4 only!")
        continue  # Go back to start of loop
    
    # Ask if user wants to continue
    again = input("\nWould you like to perform another sort? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for using the sorting program!")
        break  # Exit the loop and end program