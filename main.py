import time
def main():
    print("Hello from system-design!")
    # Record the start time
    start_time = time.time()

    # --- Your code to measure goes here ---
    print("Running a task...")
    time.sleep(2) # Simulate a task that takes 2 seconds
    # ------------------------------------

    # Record the end time
    end_time = time.time()

    # Calculate the difference in seconds
    elapsed_time = end_time - start_time

    print(f"The task took {elapsed_time:.4f} seconds to complete.")




if __name__ == "__main__":
    main()
