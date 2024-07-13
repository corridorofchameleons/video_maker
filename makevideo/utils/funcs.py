import cv2
import numpy as np


def make_video(text, pk):
    '''
    Создает видео с бегущей строкой
    '''

    width, height = 100, 100

    out = cv2.VideoWriter(f'media/{pk}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))

    frame = np.zeros((height, width, 3), dtype=np.uint8)

    x, y = width, height // 2

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5
    font_thickness = 3
    font_color = (255, 50, 100)

    for t in range(240):
        frame.fill(0)

        x -= 10

        cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness)

        out.write(frame)

    out.release()
