from setuptools import setup, find_packages

setup(
    name='flashdeberta',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        # 'flash-attn'
        'transformers==4.43.3',
    ],
    url='https://github.com/michaelfeil/flash-deberta',
    description='Flash-attention with deberta',
    author='Michael Feil',
    author_email='github@michaelfeil.eu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
)