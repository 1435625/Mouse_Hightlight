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
- 控制窗口用于启用/禁用光标高亮和关闭应用程序。
- 根据用户输入切换光圈的可见性。
- 改进了窗口管理，确保程序在关闭时正确处理窗口状态。