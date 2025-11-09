# Function to search for a student ID using linear search
def find_student(student_list, target_id):
    # Check each student ID in the list one by one
    for i, student_id in enumerate(student_list, start=1):
        # If we find the student ID we're looking for
        if student_id == target_id:
            return f"Student ID {target_id} is present at position {i}."
    # If we checked all IDs and didn't find it
    return f"Student ID {target_id} is not present in class."

# Function to search for a score using binary search (requires sorted list)
def find_a_score(scores, target_score):
    # Set starting points - beginning and end of list
    left, right = 0, len(scores) - 1
    
    # Keep searching until we've checked all possible positions
    while left <= right:
        # Find the middle position of current search range
        mid = (left + right) // 2
        
        # Check if the middle element is what we're looking for
        if scores[mid] == target_score:
            return mid  # Return the position where we found the score
            
        # If middle element is smaller, search the right half
        elif scores[mid] < target_score:
            left = mid + 1  # Move left boundary to right of middle
            
        # If middle element is larger, search the left half  
        else:
            right = mid - 1  # Move right boundary to left of middle
            
    return -1  # Return -1 if score not found

# Our data - list of student IDs (can be in any order)
class_id = [1017, 1003, 1011, 1008, 1019, 1005, 1014, 1001, 1016, 1020, 
            1009, 1012, 1004, 1018, 1006, 1013, 1002, 1010, 1015, 1007]

# Our data - list of scores (MUST be sorted for binary search to work)
sorted_scores = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 
                 29, 30, 32, 34, 36, 37, 39, 40, 43, 44]

# Display menu options to user
print("Select a search operation (1-3):")
print("1. Linear Search - Find Student ID")
print("2. Binary Search - Find Score") 
print("3. Exit")

# Main program loop - keeps running until user chooses to exit
while True:
    # Get user's choice
    choice = input("\nEnter your choice: ")
    
    # Option 1: Linear Search for Student ID
    if choice == "1":
        try:
            # Ask user which student ID to search for
            target_id = int(input("Enter student ID to search: "))
            # Call the linear search function
            result = find_student(class_id, target_id)
            # Display the result
            print(result)
        except ValueError:
            # Handle error if user enters something that's not a number
            print("Please enter a valid number!")
    
    # Option 2: Binary Search for Score
    elif choice == "2":
        try:
            # Ask user which score to search for
            target_score = int(input("Enter score to search: "))
            # Call the binary search function
            result = find_a_score(sorted_scores, target_score)
            # Check if score was found or not
            if result != -1:
                print(f"Score {target_score} found at position {result}")
            else:
                print(f"Score {target_score} not found")
        except ValueError:
            # Handle error if user enters something that's not a number
            print("Please enter a valid number!")
    
    # Option 3: Exit the program
    elif choice == "3":
        print("Thank you for using the search program!")
        break  # Exit the while loop and end program
    
    # Handle invalid menu choices
    else:
        print("Please enter 1-3 ONLY!")
        continue  # Go back to start of loop
    
    # Ask user if they want to perform another search
    again = input("\nWould you like to try another search? (y/n): ")
    # If user doesn't type 'y', exit the program
    if again.lower() != 'y':
        print("Thank you for using the search program!")
        break  # Exit the while loop and end program