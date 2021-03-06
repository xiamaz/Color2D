import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color2d",
    version="0.0.1",
    author="Max Zhao",
    author_email="alcasa.mz@gmail.com",
    description="2D colormaps for visualization of multiple channels",
    long_description=long_description,
    url="https://github.com/xiamaz/Color2D",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "imageio",
    ],
    include_package_data=True,
    package_data={
        'color2D': ['data/*.png'],
    },
)
