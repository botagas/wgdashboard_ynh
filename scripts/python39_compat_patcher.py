#!/usr/bin/env python3
"""
Python 3.9 Compatibility Patcher for WGDashboard
Converts Python 3.10+ union type hints to Python 3.9 compatible syntax
"""

import sys
import os
import re
import argparse
from pathlib import Path

def check_python_version():
    """Check if we're running Python 3.9 and need patching"""
    return sys.version_info.major == 3 and sys.version_info.minor == 9

def patch_utilities_file(file_path):
    """Patch the Utilities.py file for Python 3.9 compatibility"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already patched
        if 'from typing import Union' in content:
            print(f"✓ {file_path} already patched for Python 3.9 compatibility")
            return True
        
        # Check if patching is needed
        if ' | ' not in content or 'tuple[bool,' not in content:
            print(f"✓ {file_path} doesn't need Python 3.9 compatibility patches")
            return True
        
        print(f"🔧 Applying Python 3.9 compatibility patches to {file_path}")
        
        # Add Union import after existing imports
        lines = content.split('\n')
        import_added = False
        
        for i, line in enumerate(lines):
            if line.startswith('import ') and not import_added:
                # Add Union import after the first import
                lines.insert(i + 1, 'from typing import Union')
                import_added = True
                break
        
        # If no imports found, add at the beginning
        if not import_added:
            lines.insert(0, 'from typing import Union')
        
        # Join back and apply regex replacements
        content = '\n'.join(lines)
        
        # Replace union type hints
        # Pattern: tuple[bool, str] | tuple[bool, None] -> Union[tuple[bool, str], tuple[bool, None]]
        pattern = r'tuple\[bool, str\] \| tuple\[bool, None\]'
        replacement = r'Union[tuple[bool, str], tuple[bool, None]]'
        content = re.sub(pattern, replacement, content)
        
        # Write back the patched content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Successfully patched {file_path} for Python 3.9 compatibility")
        return True
        
    except Exception as e:
        print(f"❌ Error patching {file_path}: {e}")
        return False

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Python 3.9 Compatibility Patcher for WGDashboard')
    parser.add_argument('install_dir', nargs='?', default=None, 
                       help='WGDashboard installation directory (optional)')
    args = parser.parse_args()
    
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python version: {python_version}")
    
    if not check_python_version():
        print(f"✓ Python {python_version} supports union operators natively, no patching needed")
        return 0
    
    print(f"🔧 Python 3.9 detected, applying compatibility patches...")
    
    # Find Utilities.py file
    if args.install_dir:
        # Use provided install directory
        utilities_path = Path(args.install_dir) / 'src' / 'Utilities.py'
        if not utilities_path.exists():
            print(f"❌ Could not find Utilities.py at {utilities_path}")
            return 1
    else:
        # Fallback to searching multiple possible locations
        possible_paths = [
            Path('src/Utilities.py'),          # When run from install_dir
            Path('Utilities.py'),              # When run from src dir
            Path('../src/Utilities.py'),       # When run from scripts dir
        ]
        
        utilities_path = None
        for path in possible_paths:
            if path.exists():
                utilities_path = path
                break
        
        if utilities_path is None:
            print("❌ Could not find Utilities.py file in any expected location")
            print("   Searched paths:", [str(p) for p in possible_paths])
            print("   Try passing the install directory as an argument")
            return 1
    
    success = patch_utilities_file(utilities_path)
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
