import os
import argparse
import math
import moviepy.editor as mp

# CREDIT TO https://twitter.com/Xx__Eric_xX
LAUGH_AUDIO = mp.AudioFileClip('./laughs/latd_final.m4a')
TOTAL_SECS = LAUGH_AUDIO.duration
# 16:9 aspect ratio , default youtube size
DEFAULT_YT_SIZE = (854, 480)
# when to cut frames
START_POINTS = [0, 5, 8, 11.5, 14, 16, 19, 23, 26, 29, 31, 34]

def main(input_dir, output_file):
    filenames = [x for x in os.listdir(input_dir) if not x.startswith('.')]
    assert len(filenames) >= len(START_POINTS), 'Not enough images to create a good slideshow.'

    if len(filenames) > len(START_POINTS):
        print('Too many files, ignoring last {}'.format(len(filenames) - len(START_POINTS)))
        filenames = filenames[:len(START_POINTS)]

    clips = []
    for idx, fn in enumerate(filenames):
        sp = START_POINTS[idx]
        if idx < (len(filenames) - 1):
            duration = START_POINTS[idx + 1] - sp
        else:
            duration = TOTAL_SECS - sp

        clip = mp.ImageClip(input_dir + fn).fx(mp.vfx.resize, height=480)
        clip = clip.set_duration(duration)
        clip = clip.set_pos('center')
        clip = clip.set_start(sp)
        clips.append(clip)

    # audio credit to laugh creator
    watermark = mp.TextClip('audio by @Xx__Eric_xX', color='white', size=(250, None))
    watermark = watermark.set_opacity(0.7)
    watermark = watermark.set_pos((570, 440))
    watermark = watermark.set_duration(TOTAL_SECS)
    clips.append(watermark)

    final_clip = mp.CompositeVideoClip(clips, size=DEFAULT_YT_SIZE)
    final_clip = final_clip.set_audio(LAUGH_AUDIO)
    final_clip.write_videofile(output_file, fps=24, codec='libx264', audio_codec='aac')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input_dir', help='input directory with source images')
    ap.add_argument('-o', '--output_file', help='output file')
    args = ap.parse_args()

    assert args.input_dir is not None, 'No input file provided...'
    assert args.output_file is not None, 'No output file provided...'

    main(args.input_dir, args.output_file)
