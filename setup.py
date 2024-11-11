from setuptools import setup, find_packages

setup(
    name="my_package",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List of dependencies that will be installed with your package
        "numpy",  # Example dependency
        "requests",  # Example dependency
    ],
    description="A short description of your package",  # A short description of your package
    long_description=open('README.md').read(),  # Long description from a README file
    long_description_content_type="text/markdown",  # Format of the long description (e.g., markdown)
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email
    url="https://github.com/yourusername/yourproject",  # URL of the project
    classifiers=[  # Classifiers help users find your package by category
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python version required
)
