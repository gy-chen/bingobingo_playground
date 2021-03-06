from setuptools import setup, find_packages

setup(
    name='bingobingo_playground',
    packages=find_packages(),
    author='gychen',
    author_email='gy.chen@gms.nutc.edu.tw',
    install_requires=[
        'pandas',
        'scikit-learn',
        'sqlalchemy',
        'beautifulsoup4',
        'gunicorn',
        'flask',
        'matplotlib',
        'numpy',
        'scipy',
        'requests']
)
