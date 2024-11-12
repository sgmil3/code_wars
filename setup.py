from setuptools import setup

setup(
    name="utilities",
    version="0.1",
    packages=["utilities"],
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        "console_scripts": [
            # Add any command line scripts here
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of utility functions",
    url="https://github.com/yourusername/utilities",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
