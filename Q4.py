def task_scheduler():
    queue = []
    print("=== Interactive Task Scheduler ===")
    print("Criteria for execution: Task must have NO pending dependencies AND (be Urgent OR manually approved).")

    while True:
        print("\nOptions: [1] Add Task  [2] Process Queue  [3] View Queue  [4] Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            # Nested logic to gather task details
            task_name = input("Enter task name: ").strip()
            if not task_name:
                print("Task name cannot be empty. Try again.")
            else:
                urgent = input("Is the task urgent? (y/n): ").strip().lower() == 'y'
                dependencies = input("Does the task have pending dependencies? (y/n): ").strip().lower() == 'y'
                
                queue.append({
                    "name": task_name,
                    "urgent": urgent,
                    "dependencies": dependencies
                })
                print(f"Task '{task_name}' added to the queue.")

        elif choice == '2':
            if not queue:
                print("Queue is empty. Nothing to process.")
            else:
                print("\n--- Processing Queue ---")
                remaining_tasks = []
                
                for task in queue:
                    print(f"\nEvaluating: {task['name']}")
                    
                    # LAZY EVALUATION DEMONSTRATION:
                    # 1. 'not task["dependencies"]' is evaluated first. 
                    # 2. If it is False (dependencies exist), the 'and' short-circuits, and the rest is ignored.
                    # 3. If True, it evaluates '(task["urgent"] or ...)'.
                    # 4. If 'task["urgent"]' is True, the 'or' short-circuits, and it DOES NOT ask for manual approval.
                    if not task["dependencies"] and (task["urgent"] or input(f"Task '{task['name']}' is not urgent. Run anyway? (y/n): ").strip().lower() == 'y'):
                        print(f"[X] Executing task: {task['name']}...")
                    else:
                        # Nested logic for postponed tasks
                        if task["dependencies"]:
                            print(f"[!] Postponed: '{task['name']}' has unresolved dependencies.")
                        else:
                            print(f"[-] Postponed: '{task['name']}' was not approved for manual execution.")
                        remaining_tasks.append(task)
                
                # Update queue with only the unexecuted tasks
                queue = remaining_tasks
                print("\nQueue processing complete.")

        elif choice == '3':
            if not queue:
                print("Queue is currently empty.")
            else:
                print("\n--- Current Queue ---")
                for i, task in enumerate(queue, 1):
                    status_urg = "Urgent" if task["urgent"] else "Normal"
                    status_dep = "Has Dependencies" if task["dependencies"] else "Ready"
                    print(f"{i}. {task['name']} [{status_urg} | {status_dep}]")

        elif choice == '4':
            print("Exiting Task Scheduler. Goodbye!")
            break  # Exit condition breaks the infinite loop

        else:
            print("Invalid input. Please select a valid option (1-4).")

if __name__ == "__main__":
    task_scheduler()