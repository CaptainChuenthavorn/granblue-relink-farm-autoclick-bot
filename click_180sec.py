import pydirectinput
import time
def countdown():
    for i in range(3, 0, -1):
        print(f"Will start in {i} second...")
        time.sleep(1)

def main():
    print("Starting countdown...")
    countdown()
    print("Countdown finished. Starting the main process...")
    total_seconds = 180
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        print('time left',time.time() - start_time )
        # print('Clicking...')
        pydirectinput.click()
        time.sleep(0.1)
        pydirectinput.mouseDown()
        # print('Pressed mouse down...')
        time.sleep(0.02)
        pydirectinput.mouseUp()
        # print('Pressed mouse up...')
        time.sleep(0.1)

    print("Done")

if __name__ == "__main__":
    print("Initialization...")
    time.sleep(1)  # Wait a second before starting the main process
    main()