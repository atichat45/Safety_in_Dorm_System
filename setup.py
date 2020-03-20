import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="safety-indorm", # Replace with your own username
    version="0.0.1",
    author="Atichat Auppakansang",
    author_email="atichat645@gmail.com",
    description="Safety in Dorm System is the project for increase security in the dormitory using OpenCV and Webcam.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atichat45/Safety_in_Dorm_System",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)