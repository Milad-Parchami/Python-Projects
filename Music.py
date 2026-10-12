
import sys
import os
import random

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog
)
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

class MusicPlayer(QWidget):

    def __init__(self):
        super().__init__()

        ui_file = resource_path("Mu.ui")
        # Load the UI designed in Qt Designer
        uic.loadUi(ui_file , self)
        # -----------------------------
        # Media Player
        # -----------------------------

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()

        self.player.setAudioOutput(self.audio_output)

        # Volume
        self.Slider2.setMinimum(0)
        self.Slider2.setMaximum(100)
        self.Slider2.setValue(50)

        self.audio_output.setVolume(0.5)

        # Reapet
        self.reapet_f = False
       
        # Progress
        self.Slider1.setMinimum(0)
        self.Slider1.setMaximum(0)

        # -----------------------------
        # Variables
        # -----------------------------

        self.songs = []
        self.current_song = -1

        # -----------------------------
        # Buttons
        # -----------------------------

        self.b4.clicked.connect(self.open_songs)

        self.b5.clicked.connect(self.play_song)

        self.b6.clicked.connect(self.pause_song)

        self.b7.clicked.connect(self.previous_song)

        self.b8.clicked.connect(self.next_song)

        self.b10.clicked.connect(self.shuffle_songs)

        self.b11.clicked.connect(lambda:self.repeat())

        # -----------------------------
        # Playlist
        # -----------------------------

        self.listWidget1.itemDoubleClicked.connect(
            self.play_selected_song
        )

        # -----------------------------
        # Sliders
        # -----------------------------

        self.Slider1.sliderMoved.connect(
            self.change_position
        )
       
        self.Slider2.valueChanged.connect(
            self.change_volume
        )

        # -----------------------------
        # Player Signals
        # -----------------------------

        self.player.positionChanged.connect(
            self.position_changed
        )## موقعیت آهنگ تغییر کرد تابع پوزیشن چنج اجرا شود

        self.player.durationChanged.connect(
            self.duration_changed
        ) ## مدت آهنگ مشخص شد تابع چنج اجرا شود

        self.player.mediaStatusChanged.connect(
            # self.media_status_changed
            self.Change
        )## وقتی وضعیت مدیا پلیر تغییر کرد تابع مربوطه اجرا شود مثل آهنگ تمام شد

        # -----------------------------
        # Search
        # -----------------------------

        self.line1.textChanged.connect(
            self.search_songs
        )


    # =================================
    # Open Songs
    # =================================

    def open_songs(self):

        files , _= QFileDialog.getOpenFileNames(
            self,
            "Select Music",
            "",
            "Audio Files (*.mp3 *.wav *.ogg *.flac *.m4a)"
        )

        if not files:
            return

        self.songs = files

        self.listWidget1.clear()

        for file in self.songs:

            song_name = os.path.basename(file)

            self.listWidget1.addItem(song_name)


        # Select first song
        if self.songs:

            self.current_song = 0
            self.listWidget1.setCurrentRow(0)


    # =================================
    # Play Song
    # =================================

    def play_song(self):

        if not self.songs:
            return

        if self.current_song == -1:
            self.current_song = 0

        song = self.songs[self.current_song]

        self.player.setSource(
            QUrl.fromLocalFile(song)
        )

        self.player.play()

        self.update_song_info(song)


    # =================================
    # Pause
    # =================================

    def pause_song(self):

        self.player.pause()


    # =================================
    # Previous
    # =================================

    def previous_song(self):

        if not self.songs:
            return

        if self.current_song > 0:

            self.current_song -= 1

            self.listWidget1.setCurrentRow(
                self.current_song
            )

            self.play_song()


    # =================================
    # Next
    # =================================

    def next_song(self):

        if not self.songs:
            return

        if self.current_song < len(self.songs) - 1:

            self.current_song += 1

            self.listWidget1.setCurrentRow(
                self.current_song
            )

            self.play_song()

    # =================================
    # Shuffle
    # =================================

    def shuffle_songs (self):

         if not self.songs:
            return
         
         self.current_song = random.shuffle(self.songs)
         
         self.listWidget1.clear()

         for song in self.songs:
             song_name = os.path.basename(song)
             self.listWidget1.addItem(song_name)

    # =================================
    # Repeat
    # =================================
     
    def repeat(self):
        self.reapet_f = not self.reapet_f
     
    # =================================
    # Play Selected Song
    # =================================

    def play_selected_song(self, item):

        row = self.listWidget1.row(item)

        if row < 0 or row >= len(self.songs):
            return

        self.current_song = row

        self.play_song()


    # =================================
    # Update Song Information
    # =================================

    def update_song_info(self, song):

        name = os.path.splitext(
            os.path.basename(song)
        )[0]

        self.l2.setText(name)

        self.l3.setText("Unknown Artist")


    # =================================
    # Position Changed
    # =================================

    def position_changed(self, position):

        self.Slider1.setValue(position)
        ## هماهنگ کردن اسلایدر با موقعیت آهنگ

    # =================================
    # Duration Changed
    # =================================

    def duration_changed(self, duration):

        self.Slider1.setMaximum(duration)
        ## وقتی مدت آهنگ مشخص میشود این تابع اجرا میشود و حداکثر را برابر میکند با طول آهنگ

    # =================================
    # Change Position
    # =================================

    def change_position(self, position):

        self.player.setPosition(position)
        ## تغییر موقعیت آهنگ وقتی کاربر اسلایدر را جابهجا میکند کد بالا ینی آهنگ را ببر به همان نقطه 


    # =================================
    # Change Volume
    # =================================

    def change_volume(self, value):

        self.audio_output.setVolume(
            value / 100
        )


    # =================================
    # When Song Ends
    # =================================

    def Change(self, status):

       if status == QMediaPlayer.MediaStatus.EndOfMedia:

            if self.reapet_f ==  True:
                self.player.setPosition(0)
                self.player.play()

            else:
                 self.next_song()
    # =================================
    # Search
    # =================================

    def search_songs(self, text):

        text = text.lower()

        for i in range(self.listWidget1.count()):

            item = self.listWidget1.item(i)

            item.setHidden(
                text not in item.text().lower()
            )


# =====================================
# Run Application
# =====================================

app = QApplication(sys.argv)

window = MusicPlayer()

window.show()

sys.exit(app.exec())