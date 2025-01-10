# import tkinter as tk
# import pyautogui

# class MouseHighlight:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.overrideredirect(True)  # 去掉窗口边框
#         self.root.attributes('-topmost', True)  # 窗口置顶
#         self.root.attributes('-transparentcolor', 'white')  # 设置透明颜色
#         self.root.attributes('-alpha', 0.5)  # 设置透明度

#         # 设置画布背景颜色
#         self.canvas = tk.Canvas(self.root, width=100, height=100, bg='white', highlightthickness=0)
#         self.canvas.pack()

#         self.draw_highlight_circle()

#         self.update_position()
#         self.root.mainloop()

#     def draw_highlight_circle(self):
#         # 绘制一个圆形
#         # x0, y0, x1, y1 = 50, 0, 60, 70
#         # self.canvas.create_rectangle(x0, y0, x1, y1, fill='red', outline='black')
#         # 绘制一个圆形
#         diameter = 100
#         radius = diameter // 2
#         x0, y0, x1, y1 = 50 - radius, 50 - radius, 50 + radius, 50 + radius
        
#         # 绘制边框为黑色，填充颜色为透明
#         self.canvas.create_oval(x0, y0, x1, y1, fill='', outline='yellow', width=5)

#     def update_position(self):
#         x, y = pyautogui.position()  # 获取鼠标当前位置
#         # 更新窗口位置，使其居中在鼠标位置
#         self.root.geometry(f"+{x - 45}+{y - 45}")  
#         self.root.after(10, self.update_position)  # 每10毫秒更新一次位置

# if __name__ == '__main__':
#     MouseHighlight()

import tkinter as tk
import pyautogui

class MouseHighlight:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # 去掉窗口边框
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.attributes('-transparentcolor', 'white')  # 设置透明颜色
        self.root.attributes('-alpha', 0.5)  # 设置透明度

        # 设置画布背景颜色
        self.canvas = tk.Canvas(self.root, width=100, height=100, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.draw_highlight_circle()

        self.update_position()
        self.root.mainloop()

    def draw_highlight_circle(self):
        # 绘制一个圆形  diameter = 22 ,self.canvas.create_oval(width= 20 )
        diameter = 26       
        radius = diameter // 2
        x0, y0, x1, y1 = 50 - radius, 50 - radius, 50 + radius, 50 + radius
        
        # 绘制边框为黄色，填充颜色为透明
        self.canvas.create_oval(x0, y0, x1, y1, fill='', outline='yellow', width=24)

    def update_position(self):
        x, y = pyautogui.position()  # 获取鼠标当前位置
        # 更新窗口位置，使其居中在鼠标位置
        self.root.geometry(f"+{x - 50}+{y - 50}")  
        self.root.after(10, self.update_position)  # 每10毫秒更新一次位置

if __name__ == '__main__':
    MouseHighlight()
