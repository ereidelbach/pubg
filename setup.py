from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description="PUBG Finish Placement Prediction: A Kaggle-based playground code competition ending in January 2019. A large number of anonymized game data is provided from which a model shall be created that predicts players' finishing placement based on their final stats, on a scale from 1 (first place) to 0 (last place).",
    author='Eric Reidelbach',
    license='MIT',
)
