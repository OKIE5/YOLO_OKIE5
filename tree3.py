#!/usr/bin/env python3
import sys
from pathlib import Path

def list_dir(path: Path):
    files, dirs = [], []
    for p in path.iterdir():
        if p.name.startswith('.'):  # skip hidden
            continue
        (dirs if p.is_dir() else files).append(p)
    files.sort(key=lambda x: x.name.lower())
    dirs.sort(key=lambda x: x.name.lower())
    return files, dirs

def draw_tree(root: Path):
    if not root.exists() or not root.is_dir():
        print(f"Error: {root} is not a directory")
        return
    print(f"{root.name}/")
    root_files, root_dirs = list_dir(root)
    for i, f in enumerate(root_files):
        print(("└─ " if i == len(root_files)-1 and not root_dirs else "├─ ") + f.name)

    for d_i, d in enumerate(root_dirs[:3]):  # only first three subfolders
        is_last = (d_i == 2) or (d_i == len(root_dirs[:3]) - 1)
        print(("└─ " if is_last else "├─ ") + d.name + "/")
        files, dirs = list_dir(d)
        bar = "   " if is_last else "│  "
        for i, f in enumerate(files):
            print(bar + ("└─ " if i == len(files)-1 and not dirs else "├─ ") + f.name)
        for j, sd in enumerate(dirs):
            print(bar + ("└─ " if j == len(dirs)-1 else "├─ ") + sd.name + "/")

if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    draw_tree(root)
