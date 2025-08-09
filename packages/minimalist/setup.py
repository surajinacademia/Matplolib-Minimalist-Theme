from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

setup(
    name="minimalist",
    version="0.2.0",
    description="A minimalist matplotlib style package for scientific presentations with custom color palettes",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Suraj Sahu",
    author_email="suraj.sahu@example.com",  # Replace with your email
    url="https://github.com/surajsahu/minimalist",  # Replace with your GitHub URL
    packages=find_packages(),
    package_data={
        'minimalist': [
            'styles/**/*.mplstyle',
        ],
    },
    include_package_data=True,
    install_requires=[
        'matplotlib>=3.5.0',
        'numpy>=1.20.0',
    ],
    extras_require={
        'latex': [
            'dvipng',  # For converting equations to png
            'ghostscript',  # For handling PostScript
        ],
        'dev': [
            'pytest>=6.0',
            'pytest-cov',
            'flake8',
            'black',
        ],
        'examples': [
            'jupyter',
            'pandas',
            'seaborn',
        ]
    },
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering',
    ],
    keywords='matplotlib, plotting, scientific, visualization, style, LaTeX',
    project_urls={
        'Bug Reports': 'https://github.com/surajsahu/minimalist/issues',
        'Source': 'https://github.com/surajsahu/minimalist',
        'Documentation': 'https://github.com/surajsahu/minimalist/blob/main/README.md',
    },
) 