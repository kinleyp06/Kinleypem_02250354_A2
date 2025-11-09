# Sorting Algorithms Program

def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        swapped = False  # Track if any swaps were made in this pass
        # Compare adjacent elements - each pass places the largest unsorted element in its correct position
        for j in range(0, n - i - 1):
            # If current element is greater than next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True  # Mark that a swap occurred
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    # Start from the second element (index 1) since the first element is sorted
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be positioned
        j = i - 1     # Start comparing with the element just before the current one
        
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1               # Move to the previous element
        
        # Place the key in its correct position
        arr[j + 1] = key
    return arr

def quicksort(arr, recursive_calls=[0]):
    recursive_calls[0] += 1  # Count this recursive call
    
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as pivot
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three sub-arrays:
    left = [x for x in arr if x < pivot]    # Elements smaller than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot]   # Elements greater than pivot
    
    # Recursively sort left and right partitions, then combine with middle
    return quicksort(left, recursive_calls) + middle + quicksort(right, recursive_calls)

def main():
    # Data sets for sorting - hardcoded for demonstration
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Pema", "Sonam", 
                    "Deki", "Tashi", "Karma", "Sangay", "Dorji", "Yangchen", 
                    "Lhakpa", "Chimi"]
    
    test_scores = [78, 45, 92, 67, 88, 54, 73, 81, 95, 62, 49, 87, 71, 58, 
                  83, 66, 79, 91, 53, 76]
    
    book_prices = [450, 230, 678, 125, 890, 345, 512, 267, 789, 156, 623, 
                  411, 298, 534, 712]
    
    # Display menu options to user
    print("=== Sorting Algorithms Menu ===")
    print("Select a sorting operation (1-4):")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores") 
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit")
    
    # Main program loop - keeps running until user chooses to exit
    while True:
        # Get user's choice
        choice = input("\nEnter your choice: ")
        
        # Option 1: Bubble Sort for Student Names
        if choice == "1":
            print(f"\nOriginal: {student_names}")
            # Sort using bubble sort (create copy to preserve original)
            sorted_names = bubble_sort(student_names.copy())
            print(f"Sorted: {sorted_names}")
            
        # Option 2: Insertion Sort for Test Scores
        elif choice == "2":
            print(f"\nOriginal scores: {test_scores}")
            # Sort using insertion sort
            sorted_scores = insertion_sort(test_scores.copy())
            print(f"Sorted scores: {sorted_scores}")
            
            # Display top 5 scores (highest scores are at the end after ascending sort)
            print("\nTop 5 Scores:")
            for i in range(1, 6):
                # Use negative indexing to get scores from the end of the sorted list
                print(f"{i}. {sorted_scores[-i]}")
                
        # Option 3: Quick Sort for Book Prices
        elif choice == "3":
            print(f"\nOriginal prices: {book_prices}")
            # Initialize counter for recursive calls
            recursive_count = [0]
            # Sort using quick sort and track recursive calls
            sorted_prices = quicksort(book_prices.copy(), recursive_count)
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {recursive_count[0]}")
            
        # Option 4: Exit the program
        elif choice == "4":
            print("Thank you for using the sorting program!")
            break  # Exit the while loop and end program
        
        # Handle invalid menu choices
        else:
            print("Please enter 1-4 ONLY!")
            continue  # Go back to start of loop without asking to continue
        
        # Ask user if they want to perform another sort
        again = input("\nWould you like to perform another sort? (y/n): ")
        # If user doesn't type 'y', exit the program
        if again.lower() != 'y':
            print("Thank you for using the sorting program!")
            break  # Exit the while loop and end program

if __name__ == "__main__":
    main()