import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='ctd',
	version='1.0.0',
	author="Matthew Greer",
	author_email="pydev302@gmail.com",
        license='MIT',
	description="A tool to compare the differences between two strings.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DFC302/ctd",
        keywords=['compare', 'difference', 'same'],
	packages=setuptools.find_packages(),
        install_requires=[
            "colorama"
        ],
        package_data={'': ['LICENSE'], '': ['README.md']},
        include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
     ],
     entry_points={
            'console_scripts': [
                "ctd = main.ctd:main",
            ],
        },
)
