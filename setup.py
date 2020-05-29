from setuptools import setup, find_packages

setup(
    name="stockStalker",
    author="Ankush Patil",
    version="0.0.1",
    url="https://github.com/asprazz/stockStalker",
    description="Python CLI Application for Tracking portfolio.",
    packages=[
        "stockStalker"
    ],
    install_requires=[
        'requests>=2.23',
        'argparse',
        'prettytable',
        'colorama',
        'halo',
        'platform'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'stockStalker=stockStalker.__main__:main'
        ]
    },
    author_mail='aspraz2658@gmail.com',
    keywords=['stock', 'python-cli', 'stock-market', 'bse', 'nse'],
    license='MIT'
)