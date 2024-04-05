
import win32gui,win32ui,win32con,win32api
from time import sleep
def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd),'"'+win32gui.GetWindowText(hwnd)+'"')
    win32gui.EnumWindows(winEnumHandler, None)

def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

def main():
    list_window_names()
    window_name = "Untitled - Notepad"
    hwnd = win32gui.FindWindow(None,window_name)
    hwnd = get_inner_windows(hwnd)['RichEditD2DPT']
    if hwnd != 0:  # Check if window handle is valid
        win = win32ui.CreateWindowFromHandle(hwnd)
        #send '2' from http://www.kbdedit.com/manual/low_level_vk_list.html
        win.SendMessage(win32con.WM_CHAR, ord('A'), 0)
        win.SendMessage(win32con.WM_CHAR, ord('B'), 0)
    else:
        print("Window not found")


if __name__ == "__main__":
    main()
