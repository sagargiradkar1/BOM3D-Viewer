"""Data structures for extraction results"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class WebAssetsData:
    """Data structure for web assets"""
    glb_file: Optional[str] = None
    file_size: int = 0
    format: str = ""
    three_js_compatible: bool = False
    conversion_unavailable: Optional[str] = None
    conversion_error: Optional[str] = None
