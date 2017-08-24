from setuptools import setup, find_packages

setup(
    name='sample-hydra-client',
    version='0.0.1',
    description='',
    long_description='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'run-hydra-sample-client=hydra_sample_client.client:cli',
        ]
    },
    include_package_data=True,
    tests_require=['nose'],
    test_suite='nose.collector'
)
