from PyQt6.QtWidgets import QComboBox, QSlider, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Изображения")
        self.setGeometry(50, 50, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        
        self.image_layout = QVBoxLayout()
        self.layout.addLayout(self.image_layout)

     
        self.image_label1 = QLabel()
        self.label1_title = QLabel('До обработки')
        self.image_label2 = QLabel()
        self.label2_title = QLabel('После обработки')

       
        #self.update_images1("stuff/images/white.jpg")
        #self.update_images2("stuff/images/white.jpg")

        
        self.image_layout.addWidget(self.label1_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.label1_title.hide()
        self.image_layout.addWidget(self.label2_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label2, alignment=Qt.AlignmentFlag.AlignCenter)

       
        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)
        self.update_button()

        self.label1_title.hide()
        self.image_label1.hide()
        self.label2_title.hide()
        self.image_label2.hide()
        self.show() 

    def update_images1(self, image_path1):
        self.label1_title.show()
        pixmap1 = QPixmap(image_path1)

        
        scaled_pixmap1 = pixmap1.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label1.setPixmap(scaled_pixmap1)
        self.image_label1.show()
        
        self.update()
    def img_hide(self):
        self.label1_title.hide()
        self.image_label1.hide()
        
    def update_images2(self, image_path2):
        self.label2_title.show()
        
        pixmap2 = QPixmap(image_path2)

        
        scaled_pixmap2 = pixmap2.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label2.setPixmap(scaled_pixmap2)
        self.image_label2.show()
        
        self.update()

    
    def update_button(self):
        self.button1 = QPushButton("Выбрать изображение")
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button_layout.addWidget(self.button1)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Маштабирование")
        self.combo_box.addItem("Сдвиг")
        self.combo_box.addItem("Поворот")
        self.combo_box.addItem("Отражение")
        self.combo_box.addItem("Проекция")
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        self.button_layout.addWidget(self.combo_box)

        #Ползунок на х
        self.labelx_title = QLabel('X')
        self.button_layout.addWidget(self.labelx_title)
        self.labelx_title.hide()

        self.labelx = QLabel('0', self)
        self.labelx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelx)
        self.labelx.hide()

        self.slider_x = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_x.setMinimum(1)
        self.slider_x.setMaximum(200)
        self.slider_x.setValue(200)
        self.slider_x.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_x.setTickInterval(1)
        self.slider_x.valueChanged.connect(self.onChanged_x)
        self.button_layout.addWidget(self.slider_x)
        self.slider_x.hide()

        #Ползунок на y
        self.labely_title = QLabel('Y')
        self.button_layout.addWidget(self.labely_title)
        self.labely_title.hide()

        self.labely = QLabel('0', self)
        self.labely.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labely)
        self.labely.hide()

        self.slider_y = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_y.setMinimum(1) 
        self.slider_y.setMaximum(200)
        self.slider_y.setValue(200)
        self.slider_y.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_y.setTickInterval(1)
        self.slider_y.valueChanged.connect(self.onChanged_y)
        self.button_layout.addWidget(self.slider_y)
        self.slider_y.hide()

        #Ползунок на х shift
        self.labelxs_title = QLabel('X')
        self.button_layout.addWidget(self.labelxs_title)
        self.labelxs_title.hide()

        self.labelxs = QLabel('0', self)
        self.labelxs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelxs)
        self.labelxs.hide()

        self.slider_xs = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_xs.setMinimum(-1300)
        self.slider_xs.setMaximum(1300)
        self.slider_xs.setValue(0)
        self.slider_xs.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_xs.setTickInterval(1)
        self.slider_xs.valueChanged.connect(self.onChanged_xs)
        self.button_layout.addWidget(self.slider_xs)
        self.slider_xs.hide()

        #Ползунок на y shift
        self.labelys_title = QLabel('Y')
        self.button_layout.addWidget(self.labelys_title)
        self.labelys_title.hide()

        self.labelys = QLabel('0', self)
        self.labelys.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelys)
        self.labelys.hide()

        self.slider_ys = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_ys.setMinimum(-1300)
        self.slider_ys.setMaximum(1300)
        self.slider_ys.setValue(0)
        self.slider_ys.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_ys.setTickInterval(1)
        self.slider_ys.valueChanged.connect(self.onChanged_ys)
        self.button_layout.addWidget(self.slider_ys)
        self.slider_ys.hide()

        #Поле ввода по x
        self.labelxi_title = QLabel('X%')
        self.button_layout.addWidget(self.labelxi_title)
        self.labelxi_title.hide()

        self.input_fieldx = QLineEdit(self)
        self.button_layout.addWidget(self.input_fieldx)
        self.input_fieldx.hide()
        #Поле ввода по y
        self.labelyi_title = QLabel('Y%')
        self.button_layout.addWidget(self.labelyi_title)
        self.labelyi_title.hide()

        self.input_fieldy = QLineEdit(self)
        self.button_layout.addWidget(self.input_fieldy)
        self.input_fieldy.hide()

        #Ползунок на angle
        self.labela_title = QLabel('Угол')
        self.button_layout.addWidget(self.labela_title)
        self.labela_title.hide()

        self.labela = QLabel('0', self)
        self.labela.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labela)
        self.labela.hide()

        self.slider_a = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_a.setMinimum(-180)
        self.slider_a.setMaximum(180)
        self.slider_a.setValue(0)
        self.slider_a.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_a.setTickInterval(1)
        self.slider_a.valueChanged.connect(self.onChanged_a)
        self.button_layout.addWidget(self.slider_a)
        self.slider_a.hide()

        self.button_apply = QPushButton("Применить")
        self.button_apply.clicked.connect(self.on_button_apply_clicked)
        self.button_layout.addWidget(self.button_apply)
        self.button_apply.hide()

        #Комбобокс для отражения:
        self.combo_boxr = QComboBox()
        self.combo_boxr.addItem("По вертикали")
        self.combo_boxr.addItem("По горизонтали")
        self.combo_boxr.addItem("По вертикале и по горизонтале")
        self.combo_boxr.addItem("Не отражать")
        self.combo_boxr.currentIndexChanged.connect(self.on_combo_boxr_changed)
        self.button_layout.addWidget(self.combo_boxr)
        self.combo_boxr.hide()



    def show_scale(self,i):
        if i:
            self.labelx_title.show()
            self.labelx.show()
            self.slider_x.show()
            self.labely_title.show()
            self.labely.show()
            self.slider_y.show()
            #self.button_apply.hide()
        else:
            self.labelx_title.hide()
            self.labelx.hide()
            self.slider_x.hide()
            self.labely_title.hide()
            self.labely.hide()
            self.slider_y.hide()
            #self.button_apply.show()
    def show_shift(self, i):
        if i:
            self.labelxs_title.show()
            self.labelxs.show()
            self.slider_xs.show()
            self.labelys_title.show()
            self.labelys.show()
            self.slider_ys.show()
            self.button_apply.hide()
        else:
            self.labelxs_title.hide()
            self.labelxs.hide()
            self.slider_xs.hide()
            self.labelys_title.hide()
            self.labelys.hide()
            self.slider_ys.hide()
            #self.button_apply.show()
    def show_rotate(self,i):
        if i:
            self.input_fieldx.show()
            self.input_fieldy.show()
            self.labelyi_title.show()
            self.labelxi_title.show()
            self.labela_title.show()
            self.labela.show()
            self.slider_a.show()
        else:

            self.input_fieldx.hide()
            self.input_fieldy.hide()
            self.labelxi_title.hide()
            self.labelyi_title.hide()
            self.labela_title.hide()
            self.labela.hide()
            self.slider_a.hide()
    def show_flip(self, i):
        if i:
            self.combo_boxr.show()
        else:
            self.combo_boxr.hide()

        
 

 




