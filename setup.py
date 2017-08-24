from setuptools import setup, find_packages

setup(
    name='sample-hydra-client',
    version='0.0.1',
    description='',
    long_description='',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'run-hydra-sample-client=hydra_sample_client.client:cli',
        ]
    },
    tests_require=['nose'],
    test_suite='nose.collector'
)
