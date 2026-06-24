def shutdown(answer):
    if answer == "Yes":
        print("Shutting down")
    elif answer == "No":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown("Yes")