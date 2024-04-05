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
    click_seconds = 180
    waiting_screen_seconds=95
    round_to_iterate=9

    for i in range(round_to_iterate):
        start_time = time.time()
        while time.time() - start_time < click_seconds:
            timeleft=click_seconds-(time.time() - start_time)
            print('loop',i+1,'of',round_to_iterate,f': Time left: {timeleft:.2f}')
            # print('Clicking...')
            pydirectinput.click()
            time.sleep(0.1)
            pydirectinput.mouseDown()
            # print('Pressed mouse down...')
            time.sleep(0.02)
            pydirectinput.mouseUp()
            # print('Pressed mouse up...')
            time.sleep(0.1)
        # Countdown for the next 95 seconds
        for j in range(waiting_screen_seconds, 0, -1):
            print(f'In quest information: Time left: {j} seconds')
            time.sleep(1) 
    print("Done")

if __name__ == "__main__":
    print("Initialization...")
    time.sleep(1)  # Wait a second before starting the main process
    main()