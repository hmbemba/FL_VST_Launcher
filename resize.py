from pathlib import Path
from PIL import Image



def lsfil(path):
    return [item for item in Path(path).iterdir() if item.is_file()]

def resizeImage(srcImgPath:str | Path, dstImgPath: str|Path, size:tuple):
        image = Image.open(str(srcImgPath))
        rs = image.resize(size)
        
        rs.save(dstImgPath)
    

def resizeImages(pathToFolderContainingImages:str | Path):
    for pic in lsfil(pathToFolderContainingImages):
        if "_resized_100" in str(pic):
            return
        
        resizedPath = Path(pic).parent / str(Path(pic).stem + "_resized_100" + Path(pic).suffix)
        if not resizedPath.exists():
            resizeImage(pic, resizedPath, (100,100))

for ico in lsfil(Path(__file__).parent / "VST_ICONS"):
    if "_resized_100" not in str(ico):
        print(f'd["{ico.stem.upper()}"] = open()')
