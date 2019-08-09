import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exampe_pip_package",   # 模块名,
    version="0.0.1",             # 1.0.0（版本号，更新函数记得更新版本号）
    author="geekpanshi",
    author_email="vincentsxg@gmail.com",
    description="Just a pip package example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XingangShi/exampe_pip_package.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
