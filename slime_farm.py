import pydirectinput
import time

def click_mouse():
    pydirectinput.mouseDown()

def main():
    try:
        # Simulate clicking every 0.05 seconds for 3 minutes
        start_time = time.time()
        while time.time() - start_time < 3 * 60:
            click_mouse()
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Program terminated.")

if __name__ == "__main__":
    main()
