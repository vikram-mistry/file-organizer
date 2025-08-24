import pathlib
import sys

# Patch py2app to disable codesigning (must be before importing setup)
try:
    import py2app.util
    def dummy_codesign_adhoc(bundle):
        # Override code signing to no-op to avoid signing errors
        return None
    py2app.util.codesign_adhoc = dummy_codesign_adhoc
except ImportError:
    # py2app not installed or not building with py2app, ignore
    pass

from setuptools import setup, find_packages

# Read README file for long description
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

APP = ['file_organizer/main.py']  # Adjust if your main script path differs

OPTIONS = {
    'argv_emulation': True,
    # Add any packages your app requires here, e.g.
    # 'packages': ['some_package'],
}

if 'py2app' in sys.argv:
    setup(
        app=APP,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
        name="file-organizer-advanced",
        version="1.0.2",
        description="A CLI tool to automatically organize files into categorized folders",
        long_description=README,
        long_description_content_type="text/markdown",
        author="Vikram Mistry",
        author_email="mvikram43@gmail.com",
        url="https://github.com/vikram-mistry/file-organizer",
        packages=find_packages(),
        install_requires=[],
        python_requires=">=3.6",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
    )
else:
    setup(
        name="file-organizer-advanced",
        version="1.0.2",
        description="A CLI tool to automatically organize files into categorized folders",
        long_description=README,
        long_description_content_type="text/markdown",
        author="Vikram Mistry",
        author_email="mvikram43@gmail.com",
        url="https://github.com/vikram-mistry/file-organizer",
        packages=find_packages(),
        entry_points={
            "console_scripts": [
                "file-organizer-advanced=file_organizer.main:main",
            ],
        },
        install_requires=[],
        python_requires=">=3.6",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
    )