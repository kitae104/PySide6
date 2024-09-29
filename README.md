# PySide6
 Python GUI

### Command (.ui -> .py )
pyside6-uic widget.ui > ui_widget.py

- widget.ui
- ui_widget.py
- widget.py

### Compiling the resource file to python
pyside6-rcc resource.qrc -o resource_rc.py 

### Modal, Modaless
- modal : exec()
- modaless : show() 

### 기본 파일 설정 
디자이너에서 ui 파일 생성 후 아래 파일 확인 및 추가
- widget.ui
- widget.py
- main.py

작성한 후 
- pyside6-uic widget.ui > ui_widget.py 으로 변경 후 반드시 UTF-8으로 파일 다시 저장 