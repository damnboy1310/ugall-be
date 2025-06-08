#!/usr/bin/env python3

import sys
import os

# === 핵심 부분 → PYTHONPATH 강제 설정 ===
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# === main_flow import 후 실행 ===
from flows.main_flow import main

if __name__ == "__main__":
    # 원하는 URL 입력 
    test_url = "https://gall.dcinside.com/board/view/?id=programming&no=1234567"

    # CLI 인자 받게도 가능
    if len(sys.argv) > 1:
        test_url = sys.argv[1] 

    main(test_url)
