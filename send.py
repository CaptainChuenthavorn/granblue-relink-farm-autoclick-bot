import win32gui
import win32ui
import win32con
import win32api
from time import sleep

def main():
    window_name = "Untitled - Notepad"
    hwnd = win32gui.FindWindow(None, window_name)
    inner_windows = get_inner_windows(hwnd)
    print("Inner Windows:")
    print(inner_windows)
    
    if 'Edit' in inner_windows:
        edit_hwnd = inner_windows['Edit']
        win = win32ui.CreateWindowFromHandle(edit_hwnd)

        win32api.SendMessage(edit_hwnd, win32con.WM_KEYDOWN, 0x41, 0)  # Send 'A'
        sleep(0.5)
        win32api.SendMessage(edit_hwnd, win32con.WM_KEYUP, 0x41, 0)    # Release 'A'
    else:
        print("Edit window not found")

def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

if __name__ == "__main__":
    main()
