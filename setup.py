from setuptools import setup

setup(
    name='binance-liquidation-feeder',
    version=__import__('binance_liquidation_feeder').__version__,
    packages=['binance_liquidation_feeder'],
    description='Notify liquidation on Binance.',
    install_requires=["requests", "websocket"],
    author='aoki-h-jp',
    author_email='aoki.hirotaka.biz@gmail.com',
    license='MIT',
)
