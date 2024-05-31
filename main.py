import cv2
import sys
from window import ImageWindow
import numpy as np
from PyQt6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QWidget

save_process_path='stuff/saved/save_proc.jpg'
class Mywindow(ImageWindow):
    def __init__(self):
        super().__init__()
        self.initial_path=''
        self.scaleX=200
        self.scaleY=200
        self.shiftX=0
        self.shiftY=0
        self.selected_oper=0
        self.centerx=50
        self.centery=50
        self.angle=-90
    #Кнопки
    def on_button1_clicked(self):
        self.img_hide()
        self.download_img(1)
    # def on_button_apply_clicked(self):
    #     if self.selected_oper==2:
    #         self.rotate()
    #Комбобоксы
    def on_combo_box_changed(self, index):
        self.selected_oper=index
        if index == 0:
            self.show_scale(1)
            self.show_shift(0)
            self.show_rotate(0)
            self.show_flip(0)
        elif index == 1:
            self.show_scale(0)
            self.show_shift(1)
            self.show_rotate(0)
            self.show_flip(0)
        elif index == 2:
            self.show_scale(0)
            self.show_shift(0)
            self.show_rotate(1)
            self.show_flip(0)
        elif index == 3:
            self.show_scale(0)
            self.show_shift(0)
            self.show_rotate(0)
            self.show_flip(1)
    def on_combo_boxr_changed(self, index):
        self.flip(index)

    #Ползунки
    def onChanged_x(self, value):
        self.scaleX=value
        self.labelx.setText(str(value))
        if self.selected_oper==0:
            self.scale()
    def onChanged_y(self, value):
        self.scaleY=value
        self.labely.setText(str(value))
        if self.selected_oper==0:
            self.scale()
    def onChanged_xs(self, value):
        self.shiftX=value
        self.labelxs.setText(str(value))
        self.shift()
    def onChanged_ys(self, value):
        self.shiftY=value
        self.labelys.setText(str(value))
        self.shift()
    def onChanged_a(self, value):
        self.angle=value
        self.labela.setText(str(value))
        self.rotate()


    def download_img(self, i):
        try:
            self.initial_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.jpeg)")
            if not self.initial_path:
                raise FileNotFoundError("Путь к изображению не был выбран.")
            if i==1:
                self.update_images1(self.initial_path)
            else:
                raise FileNotFoundError("Куда ты хочешь картинку?")
        except Exception as e:
            print("Ошибка при загрузке изображения", e)
            return None
        
    def loadcv2(self, ini):
        try:
            if not ini:
                raise FileNotFoundError("Путь к изображению не был выбран.")
            img = cv2.imread(ini)
            return img
        except Exception as e:
            print("Ошибка при выполнении операции: ", e)
            return None
    def saved_and_print_process(self, img):
        cv2.imwrite(save_process_path, img)
        self.update_images2(save_process_path)


    def scale(self):
        img = self.loadcv2(self.initial_path)
        img = cv2.resize(img, (self.scaleY, self.scaleX), interpolation=cv2.INTER_LINEAR)
        self.saved_and_print_process(img)
    def shift(self):
        img = self.loadcv2(self.initial_path)
        rows, cols = img.shape[:2]
        M = np.float32([[1, 0, self.shiftX], [0, 1, self.shiftY]])
        img = cv2.warpAffine(img, M, (cols, rows))
        self.saved_and_print_process(img)
    def input_center(self,img:cv2):
        # if not img:
        #     raise ValueError("Не выбранно изображение")
        if not (self.input_fieldy.text() and self.input_fieldx.text()):
            raise ValueError("Не выбранна координата точки")
        self.centery,self.centerx=int(self.input_fieldy.text())/100,int(self.input_fieldx.text())/100
        rows, cols=img.shape[:2]
        self.centery=int(rows*self.centery)
        self.centerx=int(cols*self.centerx)
    def rotate(self):
        try:
            img = self.loadcv2(self.initial_path)
            self.input_center(img)
            rows, cols = img.shape[:2]
            #M = cv2.getRotationMatrix2D((self.centery,self.centerx), self.angle, 1)
            M = cv2.getRotationMatrix2D((self.centery,self.centerx), self.angle, 1)
            img = cv2.warpAffine(img, M, (cols, rows), flags=cv2.INTER_LINEAR)
            self.saved_and_print_process(img)
        except Exception as e:
            print("Ошибка при rotate: ", e)
            return None
    def flip(self, index):
        try:
            img = self.loadcv2(self.initial_path)
            if index==0:
                img=cv2.flip(img, 1)
            elif index==1:
                img=cv2.flip(img, 0)
            elif index==2:
                img=cv2.flip(img,-1)
            elif index==3:
                self.saved_and_print_process(img)
            else:
                raise("Индекс выбран не правильно")
            self.saved_and_print_process(img)
        except Exception as e:
            print("Ошибка при reflection: ", e)
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    sys.exit(app.exec())
