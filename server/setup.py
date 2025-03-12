from setuptools import setup, find_packages

setup(
    name='stock_server',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.1',
        'flask-cors>=3.0.10',
        'akshare>=1.1.0',
        'pandas>=1.3.3',
        'requests>=2.26.0'
    ],
    entry_points={
        'console_scripts': [
            'stock-server=server.server:main'
        ]
    }
)