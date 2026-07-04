from pathlib import Path

def test_manifest_directory():

    assert Path("data/manifests").exists()