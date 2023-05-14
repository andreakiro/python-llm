from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='python-llm',
    version='0.1.2',
    author='Daniel Gross',
    author_email='d@dcgross.com',
    description='An LLM wrapper for Humans',
    packages=find_namespace_packages(include=['llm', 'llm.*']),
    classifiers=[
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
