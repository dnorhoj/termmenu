import setuptools

setuptools.setup(
    name="termmenu",
    version="1.2",
    author="dnorhoj",
    author_email="daniel.norhoj@gmail.com",
    description="A tool for making terminal menus.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dnorhoj/termmenus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)