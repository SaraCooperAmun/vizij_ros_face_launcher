from setuptools import setup, find_packages

package_name = 'vizij_ros_face_launcher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/launch',
            ['launch/vizij_ros_face.launch.py']
        ),
        (
            'share/' + package_name + '/scripts',
            ['scripts/launch-vizij-face.sh']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nvidia',
    maintainer_email='sara.cooper@iiia.csic.es',
    description='Launcher for vizij_ros face and Vizij face bridge',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    },
)
