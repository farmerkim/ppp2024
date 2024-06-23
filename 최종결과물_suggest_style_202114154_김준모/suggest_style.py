import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

"""코딩 쭉 한번 훑기"""
"""ppt 파일(짧게)"""
"""보고서 작성"""

def suggest_style(height, weight, face_shape):
    suggestions = {
        "키": f"{height} cm",
        "몸무게": weight,
        "얼굴형": face_shape,
    }
    return suggestions

class ClickableLabel(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.url = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.url:
            webbrowser.open(self.url)

    def set_url(self, url):
        self.url = url

class StyleApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('성인남자의 얼굴형과 체형 선택에 따른 옷 스타일 추천')
        
        layout = QVBoxLayout()

        self.height_label = QLabel("키를 입력하세요 (cm):")
        layout.addWidget(self.height_label)
        self.height_combobox = QComboBox(self)
        self.height_options = [
            "평균 이하",
            "평균",
            "평균 이상"
        ]
        self.height_combobox.addItems(self.height_options)
        layout.addWidget(self.height_combobox)

        self.weight_label = QLabel("어떤 체중에 해당하시나요?")
        layout.addWidget(self.weight_label)
        self.weight_combobox = QComboBox(self)
        self.weight_options = [
            "저체중",
            "정상",
            "과체중(비만도 해당)"
        ]
        self.weight_combobox.addItems(self.weight_options)
        layout.addWidget(self.weight_combobox)

        self.face_shape_label = QLabel("자신의 얼굴형을 선택하세요:")
        layout.addWidget(self.face_shape_label)
        self.face_shape_combobox = QComboBox(self)
        self.face_shape_options = [
            "원형 얼굴",
            "역삼각형 얼굴",
            "네모난 얼굴"
        ]
        self.face_shape_combobox.addItems(self.face_shape_options)
        layout.addWidget(self.face_shape_combobox)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit)
        layout.addWidget(self.submit_button)

        self.image_label = ClickableLabel(self)
        self.image_label.setFixedSize(400, 400)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def submit(self):
        try:
            height_index = self.height_combobox.currentIndex()
            weight_index = self.weight_combobox.currentIndex()
            face_shape_index = self.face_shape_combobox.currentIndex()

            if height_index != -1 and weight_index != -1 and face_shape_index != -1:
                height = self.height_options[height_index]
                weight = self.weight_options[weight_index]
                face_shape = self.face_shape_options[face_shape_index]

                style_suggestion = suggest_style(height, weight, face_shape)
                
                suggestion_text = "\n당신의 스타일 제안:\n"
                for category, suggestion in style_suggestion.items():
                    suggestion_text += f"- {category}: {suggestion}\n"

                QMessageBox.information(self, "스타일 제안", suggestion_text)
                """키 0(평균이하) 키 1(평균) 키 2(평균이상) / 몸무게 0(저체중) 1(정상) 2(고체중) /
                얼굴 0(원형얼굴) 1(역삼각형얼굴) 2(네모난얼굴)"""
                if height_index == 0 and weight_index == 0 and face_shape_index == 0:
                    self.show_image('male_street_fashion.png', "https://www.musinsa.com/brands/filluminate")
                elif height_index == 0 and weight_index == 0 and face_shape_index == 1:
                    self.show_image('male_minimalism_fashion.png', "https://www.musinsa.com/brands/lemard")
                elif height_index == 0 and weight_index == 0 and face_shape_index == 2:
                    self.show_image('male_amekaji_fashion.png', "https://www.musinsa.com/brands/uniformbridge")
                elif height_index == 0 and weight_index == 1 and face_shape_index == 0:
                    self.show_image('male_denim_fashion.png', "https://www.musinsa.com/brands/levis")
                elif height_index == 0 and weight_index == 1 and face_shape_index == 1:
                    self.show_image('male_contemporary_fashion.png', "https://www.uniqlo.com/kr/ko/men")
                elif height_index == 0 and weight_index == 1 and face_shape_index == 2:
                    self.show_image('male_amekaji_fashion.png', "https://www.musinsa.com/brands/uniformbridge")
                elif height_index == 0 and weight_index == 2 and face_shape_index == 0:
                    self.show_image('male_street_fashion.png', "https://www.musinsa.com/brands/brownbreath")
                elif height_index == 0 and weight_index == 2 and face_shape_index == 1:
                    self.show_image('male_amekaji_fashion.png', "https://www.musinsa.com/brands/espionage")
                elif height_index == 0 and weight_index == 2 and face_shape_index == 2:
                    self.show_image('male_athleisure_fashion.png', "https://www.musinsa.com/brands/alphaindustries")
                elif height_index == 1 and weight_index == 0 and face_shape_index == 0:
                    self.show_image('male_unisex_fashion.png', "https://www.musinsa.com/brands/graver")
                elif height_index == 1 and weight_index == 0 and face_shape_index == 1:
                    self.show_image('male_minimalism_fashion.png', "https://www.musinsa.com/brands/musinsastandard")
                elif height_index == 1 and weight_index == 0 and face_shape_index == 2:
                    self.show_image('male_bohemian_fashion.png', "https://karaku.co.kr/")
                elif height_index == 1 and weight_index == 1 and face_shape_index == 0:
                    self.show_image('male_contemporary_fashion.png', "https://www.uniqlo.com/kr/ko/men")
                elif height_index == 1 and weight_index == 1 and face_shape_index == 1:
                    self.show_image('male_tailoring_fashion.png', "https://www.musinsa.com/brands/musinsastandard")
                elif height_index == 1 and weight_index == 1 and face_shape_index == 2:
                    self.show_image('male_denim_fashion.png', "https://www.musinsa.com/brands/levis")
                elif height_index == 1 and weight_index == 2 and face_shape_index == 0:
                    self.show_image('male_street_fashion.png', "https://thisisneverthat.com/")
                elif height_index == 1 and weight_index == 2 and face_shape_index == 1:
                    self.show_image('male_amekaji_fashion.png', "https://www.musinsa.com/brands/outstanding")
                elif height_index == 1 and weight_index == 2 and face_shape_index == 2:
                    self.show_image('male_athleisure_fashion.png', "https://www.musinsa.com/brands/alphaindustries")
                elif height_index == 2 and weight_index == 0 and face_shape_index == 0:
                    self.show_image('male_contemporary_fashion.png', "https://www.uniqlo.com/kr/ko/men")
                elif height_index == 2 and weight_index == 0 and face_shape_index == 1:
                    self.show_image('male_minimalism_fashion.png', "https://www.musinsa.com/brands/musinsastandard")
                elif height_index == 2 and weight_index == 0 and face_shape_index == 2:
                    self.show_image('male_bohemian_fashion.png', "https://www.musinsa.com/brands/brooksbrothers")
                elif height_index == 2 and weight_index == 1 and face_shape_index == 0:
                    self.show_image('male_tailoring_fashion.png', "https://www.musinsa.com/brands/musinsastandard")
                elif height_index == 2 and weight_index == 1 and face_shape_index == 1:
                    self.show_image('male_minimalism_fashion.png', "https://www.musinsa.com/brands/suare")
                elif height_index == 2 and weight_index == 1 and face_shape_index == 2:
                    self.show_image('male_bohemian_fashion.png', "https://www.ralphlauren.co.kr/")
                elif height_index == 2 and weight_index == 2 and face_shape_index == 0:
                    self.show_image('male_amekaji_fashion.png', "https://www.musinsa.com/brands/uniformbridge")
                elif height_index == 2 and weight_index == 2 and face_shape_index == 1:
                    self.show_image('male_street_fashion.png', "https://www.musinsa.com/brands/nomanual")
                elif height_index == 2 and weight_index == 2 and face_shape_index == 2:
                    self.show_image('male_athleisure_fashion.png', "https://www.musinsa.com/brands/alphaindustries")
        except ValueError:
            QMessageBox.critical(self, "Invalid input", "선택하신 내용을 다시 한번 확인해주세요")

    def show_image(self, image_path, url):
        pixmap = QPixmap(image_path)
        if True:
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))
            self.image_label.set_url(url)

def main():
    app = QApplication(sys.argv)
    ex = StyleApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()