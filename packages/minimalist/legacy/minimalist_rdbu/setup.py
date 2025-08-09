from setuptools import setup, find_packages

setup(
    name="minimalist_rdbu",
    version="0.1.0",
    description="A minimalist matplotlib style for scientific presentations with CMU Sans Serif font and RdBu color scheme",
    author="Suraj Sahu",
    author_email="suraj.sahu@example.com",  # Replace with your email
    url="https://github.com/surajsahu/minimalist_rdbu",  # Replace with your GitHub URL
    packages=find_packages(),
    package_data={
        'minimalist_rdbu': ['styles/*.mplstyle', 'styles/*/*.mplstyle'],
    },
    install_requires=[
        'matplotlib>=3.5.0',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    extras_require={
        'latex': [
            'dvipng',  # For converting equations to png
            'ghostscript',  # For handling PostScript
        ],
    },
) 