from pathlib import Path

def test_video_exists():

    assert Path("data/raw_videos").exists()