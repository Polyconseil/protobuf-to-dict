from setuptools import setup

setup(
    name='protobuf-to-dict',
    description='A teeny Python library for creating Python dicts from '
                'protocol buffers and the reverse. Useful as an intermediate step '
                'before serialisation (e.g. to JSON).',
    version='0.1.3+polyconseil',
    author='Ben Hodgson',
    author_email='ben@benhodgson.com',
    url='https://github.com/benhodgson/protobuf-to-dict',
    license='Public Domain',
    keywords=['protobuf', 'json', 'dict'],
    install_requires=['protobuf>=3.0.0b1.post1'],
    package_dir={'': 'src'},
    py_modules=['protobuf_to_dict'],
    test_suite='nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
