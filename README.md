# Mouse Highlight Program

## 简介
这个程序使用 Tkinter 和 PyAutoGUI 库创建一个鼠标高亮效果的窗口。窗口会跟随鼠标移动，并在鼠标位置绘制一个透明的圆形高亮。

## 依赖
- tkinter
- pyautogui

## 使用方法
1. 确保已安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行程序：
   ```bash
   python mouse_highlight.py
   ```

## 功能
- 窗口无边框，始终在最上层。
- 窗口透明，显示一个黄色边框的圆形高亮。
- 每10毫秒更新一次窗口位置，以跟随鼠标移动。 