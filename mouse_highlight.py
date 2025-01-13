import tkinter as tk
import pyautogui

class MouseHighlight:
    def __init__(self):
        self.root = tk.Tk()
        self.is_closing = False  # 初始化关闭标志
        self.root.overrideredirect(True)  # 去掉窗口边框
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.attributes('-transparentcolor', 'white')  # 设置透明颜色
        self.root.attributes('-alpha', 0.5)  # 设置透明度

        # 设置画布背景颜色
        self.canvas = tk.Canvas(self.root, width=100, height=100, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.draw_highlight_circle()

        # 创建控制窗口
        self.control_window = tk.Toplevel(self.root)
        self.control_window.title("鼠标高亮v0.1")
        self.control_window.geometry("320x110")  # 设置窗口大小为320x110
        self.control_window.protocol("WM_DELETE_WINDOW", self.close_window)  # 绑定关闭事件

        # 创建框架以组织控件
        frame = tk.Frame(self.control_window)
        frame.pack(pady=10)  # 添加垂直间距

        # 在这里定义 use_cursor_var
        self.use_cursor_var = tk.BooleanVar(value=False)  # 默认禁用光标高亮
        self.cursor_checkbox = tk.Checkbutton(frame, text="启用光标高亮", variable=self.use_cursor_var, font=(12))  # 增大字体大小
        self.cursor_checkbox.grid(row=1, column=0, padx=10, pady=5)  # 使用 grid 布局

        # 添加关闭按钮
        self.close_button = tk.Button(frame, text="关闭程序", command=self.close_window, font=(10))  
        self.close_button.grid(row=2, column=0, padx=10, pady=5)  # 使用 grid 布局

        # 更新位置时检查复选框状态
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
        if self.is_closing:  # 检查是否正在关闭
            return
        if self.use_cursor_var.get():  # 检查复选框状态
            x, y = pyautogui.position()  # 获取鼠标当前位置
            self.root.geometry(f"+{x - 50}+{y - 50}")  
            self.root.deiconify()  # 显示光圈窗口
        else:
            self.root.withdraw()  # 隐藏光圈窗口
        self.root.after(10, self.update_position)  # 每10毫秒更新一次位置

    def toggle_cursor_highlight(self):
        self.use_cursor_var.set(not self.use_cursor_var.get())  # 切换光标高亮状态

    def close_window(self):
        self.is_closing = True  # 设置关闭标志
        self.control_window.destroy()  # 关闭控制窗口
        self.root.withdraw()  # 隐藏光圈窗口
        self.root.destroy()  # 关闭主窗口

if __name__ == '__main__':
    MouseHighlight()
