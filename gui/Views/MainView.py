import subprocess
from pathlib import Path
from gui.DPGW.BaseView import BaseView
from dataclasses import dataclass
from gui.DPGW.BaseView import BaseView
from gui.DPGW.Container import Container
from gui.DPGW.Row import Row
from gui.DPGW.Button import Button
import dearpygui.dearpygui as dpg
from PIL import Image
from collections import defaultdict


@dataclass
class MyView(BaseView):
    iconsFolderPath:Path = Path(Path(Path(__file__).parent).parent).parent / "VST_ICONS"
    
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
                    "borderColor": [255, 0, 0, 0],  # "orange",
                    "bkgColor": [0, 0, 255, 0],
                    "padding": [0, 0],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create()
        self.createIconRow()
        self.createImageButtons()

    
            
    def lsfil(self,path):
        return [item for item in Path(path).iterdir() if item.is_file()]
    
    def resizeImage(self,srcImgPath:str | Path, dstImgPath: str|Path, size:tuple):
            image = Image.open(str(srcImgPath))
            rs = image.resize(size)
            
            rs.save(dstImgPath)
        

    def resizeImages(self, pathToFolderContainingImages:str | Path):
        for pic in self.lsfil(pathToFolderContainingImages):
            if "_resized_100" in str(pic):
                ...
            else:
                resizedPath = Path(pic).parent / str(Path(pic).stem + "_resized_100" + Path(pic).suffix)
                if not resizedPath.exists():
                    self.resizeImage(pic, resizedPath, (100,100))
    
    def openVst(self, vstName):
        def def_value():
            print(vstName)
            raise Exception("File Not Found")
        d = defaultdict(def_value)
        vstNameFormatted = vstName.split('_resized')[0].upper()
        
        
        def open(vstPath):
            subprocess.run(["powershell.exe", fr'start-process "{vstPath}" '])
        
        
        d["FLEX"] =  lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\1) MAIN\Main\FLEX.FST")
        d["HARMOR"] = lambda:open(r'D:/FL SymLinks/Image-Line/FL Studio/Presets/Plugin database/Generators/1) MAIN/Main/Harmor.fst')
        d["KONTAKT"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\synth\Kontakt.fsts")
        d["OPX"] = lambda:open(r'D:/FL SymLinks/Image-Line/FL Studio/Presets/Plugin database/Generators/1) MAIN/Main/OP-X PRO-II [64bit].fst')
        d["PG-8X"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\synth\PG-8X.fst")
        d["SAMPLETANK"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\1) MAIN\Main\SampleTank 4.fst")
        d["SCALER2"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\Instrument\Scaler 2.fst")
        d["SERATO_SAMPLE"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\synth\Serato Sample.fst")
        d["SUBLAB"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\1) MAIN\Main\SubLab.fst")
        d["TRUEPIANOS"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\Pianos\TruePianos.fst")
        d["XPAND"] = lambda:open(r"D:\FL SymLinks\Image-Line\FL Studio\Presets\Plugin database\Generators\1) MAIN\Main\Xpand!2 [64bit].fst")
        
        d[vstNameFormatted]()
        
    
    def createImageButton(self,iconPath:Path | str, parent):
        width, height, channels, data = dpg.load_image(str(iconPath))
        with dpg.texture_registry():
            dpg.add_static_texture(width=100, height=100, default_value=data, tag=Path(iconPath).stem)
        dpg.add_image_button(texture_tag=Path(iconPath).stem, parent=parent, callback=lambda: self.openVst(iconPath.stem))
            
    
    def createImageButtons(self):
        if not self.iconsFolderPath.exists():
            raise Exception("Can't find 'VST_ICONS' folder")
        
        self.resizeImages(self.iconsFolderPath)
        
        count = 0
        for index, path in enumerate(self.lsfil(self.iconsFolderPath)):
            if "_resized_100" in str(path):
                if count < 9:
                    parent = f"row_1_{self.id}_row"
                else:
                    parent = f"row_2_{self.id}_row"
                self.createImageButton(path, parent)
                count+=1
                
            


    
    def createIconRow(self):
        r1 = Row(
            **{
                "tag": f"row_1_{self.id}",
                "parent": self.top.link(),
                "numCols": 9,
                "sizing": 1,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 0, 0, 0],
                "padding": [10, 10],  # Default is [10,0]
                "user_data": None,
            }
        ).create()
        
        r2 = Row(
            **{
                "tag": f"row_2_{self.id}",
                "parent": self.top.link(),
                "numCols": 9,
                "sizing": 1,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 0, 0, 0],
                "padding": [10, 10],  # Default is [10,0]
                "user_data": None,
            }
        ).create()
