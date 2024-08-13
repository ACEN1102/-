import pyautogui
import pyperclip
import time

time.sleep(1)


def auto_reply():
    # 对方消息位置坐标(通过position获取)
    message_x, message_y = ,
    # 输入框位置坐标(通过position获取)
    input_x, input_y = ,

    # 双击选中消息
    pyautogui.doubleClick(message_x, message_y)
    time.sleep(1)  # 等待消息被选中

    # 复制选中的文本到剪贴板
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # 从剪贴板读取文本
    message_text = pyperclip.paste().strip()

    # 检查消息内容
    if message_text == "CNM":
        pyautogui.click(input_x, input_y)
        time.sleep(1)

        pyautogui.typewrite("SB")
        pyautogui.press('enter')

        pyperclip.copy('')


while True:
    auto_reply()
    time.sleep(3)