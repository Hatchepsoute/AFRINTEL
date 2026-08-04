#!/usr/bin/env python3
import sys
import traceback

from afrintel_connector import AfrintelConnector

if __name__ == "__main__":
    try:
        connector = AfrintelConnector()
        connector.run()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
