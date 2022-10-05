
from dataclasses import dataclass, field
from typing import Any, List
from abc import ABCMeta, abstractmethod
import dearpygui.dearpygui as dpg
from gui.Views.MainView import MyView
from gui.DPGW.Styles import DpgStyles
from gui.DPGW.Styles import DpgColor
import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

dpg.create_context()

with dpg.font_registry():
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

with dpg.window(tag="Primary Window", no_scrollbar=True):
    
    #Define Views
    view = MyView()


    # Show Starting View
    view.show()


with dpg.theme() as item_theme:
    with dpg.theme_component(dpg.mvAll):
        DpgStyles.windowPadding(0,0)
        DpgColor([31, 31, 31, 255]).windowBg()
dpg.bind_item_theme("Primary Window", item_theme)

dpg.create_viewport(title="FL VST Launcher", width=int(screen_width*.8), height=int(screen_height*.2))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


# @dataclass
# class xx(metaclass=ABCMeta):
#     _: List = field(default_factory=lambda: [])

#     @abstractmethod
# 	def foo(self):
# 		pass

# @dataclass
# class xx:
#     _: List = field(default_factory=lambda: [])