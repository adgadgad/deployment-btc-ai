from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='1.0.0',
    description='Your project description',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'ta',
        'alpha_vantage',
        'scikit-learn'
    ]
)
