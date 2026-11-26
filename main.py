#!/usr/bin/env python3
"""
Write a lost-sock status update to the output directory.
The sock has been washed with gym clothes and now speaks fluent vinegar and regret.
"""

import os
import sys

LINE = "Washed with gym clothes. Now I speak fluent vinegar and regret. Elastic remembers what the cuff tries to forget."

def main():
    # Get output directory from environment, default to /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Content to write (line + newline)
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 120 and content.strip()):
        raise ValueError("Content length must be 1-120 chars and not only whitespace")
    if content.count("\n") != 1 or content.rstrip("\n") != LINE:
        raise ValueError("Content must be exactly one line")
    
    # Create output directory if needed
    os.makedirs(output_dir, exist_ok=True)
    
    # Write to primary output
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also write to /output/entry.txt if different directory (best effort)
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # Ignore errors
    
    # Print output path and character count
    print(f"{output_path} {len(content)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())