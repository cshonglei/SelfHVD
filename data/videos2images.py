# Copyright (c) OpenMMLab. All rights reserved.
"""Extract frames from MP4 files under data/ into data/test_videos/<stem>/."""

import argparse
import sys
from pathlib import Path

import cv2


def extract_one(video_path: Path, out_dir: Path) -> int:
    """Write frames as 00000000.png, ... Returns frame count."""
    out_dir.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f'cannot open video: {video_path}')

    n = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        out_path = out_dir / f'{n:08d}.png'
        if not cv2.imwrite(str(out_path), frame):
            cap.release()
            raise RuntimeError(f'failed to write: {out_path}')
        n += 1
    cap.release()
    return n


def iter_mp4_under_data(data_dir: Path):
    """All .mp4 under data_dir, excluding anything under data_dir/test_videos."""
    test_videos = (data_dir / 'test_videos').resolve()
    for p in sorted(data_dir.rglob('*.mp4')):
        try:
            p.resolve().relative_to(test_videos)
        except ValueError:
            yield p
        else:
            continue


def main():
    parser = argparse.ArgumentParser(
        description='Split MP4 files under data/ into PNG frames in '
        'data/test_videos/<video_stem>/')
    parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path(__file__).resolve().parent,
        help='root directory to search for MP4 (default: this script directory)')
    parser.add_argument(
        '--out-root',
        type=Path,
        default=None,
        help='output root (default: <data-dir>/test_videos)')
    args = parser.parse_args()

    data_dir = args.data_dir.resolve()
    out_root = (args.out_root or (data_dir / 'test_videos')).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    mp4_list = list(iter_mp4_under_data(data_dir))
    if not mp4_list:
        print(f'no MP4 found under {data_dir} (excluding test_videos)', file=sys.stderr)
        return 0

    for video_path in mp4_list:
        stem = video_path.stem
        out_dir = out_root / stem
        try:
            n = extract_one(video_path, out_dir)
            print(f'{video_path} -> {out_dir} ({n} frames)')
        except Exception as e:
            print(f'ERROR {video_path}: {e}', file=sys.stderr)
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
