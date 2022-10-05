from pathlib import Path
from gui.DPGW.BaseView import BaseView
from dataclasses import dataclass
from gui.DPGW.BaseView import BaseView
from gui.DPGW.Container import Container
from gui.DPGW.Row import Row
from gui.DPGW.Button import Button
import dearpygui.dearpygui as dpg


@dataclass
class MyView(BaseView):
    def __post_init__(self):
        self.id = self.getId()
        with dpg.stage(tag=f"Stage_{self.id}"):
            self.top = Container(
                **{
                    "tag": f"top_{self.id}",
                    "show": True,
                    "w": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                    "h": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                    "autoSizeX": False,  # Overtakes w
                    "autoSizeY": False,  # Overtakes h
                    "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                    "horzGap": 0,  # space between items when itemOrientation is row
                    "verticalItemSpacing": [0, 0],
                    "border": True,
                    "borderRadius": 0,
                    "borderColor": [255, 0, 0, 255],  # "orange",
                    "bkgColor": [0, 0, 255, 255],
                    "padding": [0, 0],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create()
        self.createIconRow()
        
        # for icon in item.ls(vstIconsFolderPath)[:middle_index]:
        #     Image().create(Parent=row.link())
            
            
            

    def imageButton(vstName:str, iconPath:Path):
        ...
    
    def createIconRow(self):
        r1 = Row(
            **{
                "tag": f"row_1_{self.id}",
                "parent": self.top.link(),
                "numCols": 10,
                "sizing": 1,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 0, 0, 255],
                "padding": [0, 0],  # Default is [10,0]
                "user_data": None,
            }
        ).create()
        Button(
            **{
                "tag": f"harmor_{self.id}",
                "w": 100,
                "h": 100,
                "text": "Harmor",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_20",
                "callback": None,  # self.autoFind,
                "user_data": ...,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [0, 0, 0, 0],
                "bkgColorHovered": [0, 0, 0, 100],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [0, 0],  # [10, 10],
            }
        ).create(Parent=r1.link())
        
        Button(
            **{
                "tag": f"harmor2_{self.id}",
                "w": 100,
                "h": 100,
                "text": "Harmor2",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_20",
                "callback": None,  # self.autoFind,
                "user_data": ...,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [0, 0, 0, 0],
                "bkgColorHovered": [0, 0, 0, 100],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [0, 0],  # [10, 10],
            }
        ).create(Parent=r1.link())
