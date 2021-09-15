#!/usr/bin/python3.9+
# -*- coding: utf-8 -*-
# 📌️ M4nifest0 Black Hat Hacking Team™💪
# 📌️ 𝕿𝖍𝖎𝖘 𝕴𝖘 𝕿𝖍𝖊 𝓜4𝓷𝓲𝓯𝓮𝓼𝓽0 𝕿𝖊𝖆𝖒™
# 📌️ Author hack4lx 👊 
# 📌 💪 Site : https://m4nifest0.com 👊
# 📌 💪 Site : https://m4nifest0.group 👊
# 📌 💪 Site : https://m4nifest0.shop 👊
# 📌 💪 Channel Telegram : https://t.me/M4nifest0 👊
# 📌 2021 💪
# 📌 Version 1.0.0 💪


from setuptools import setup, find_packages


print ("")
print ("██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗██╗     ██╗  ██╗")
print ("██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║██║     ╚██╗██╔╝")
print ("███████║███████║██║     █████╔╝ ███████║██║      ╚███╔╝ ")
print ("██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║      ██╔██╗ ")
print ("██║  ██║██║  ██║╚██████╗██║  ██╗     ██║███████╗██╔╝ ██╗")
print ("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝") 



setup(
    name='M4nifest0',
    version="1.0.0",
    packages=find_packages(),
    author="hack4lx",
    install_requires=["argparse","tabulate","httpx","tqdm","unicodecsv"],
    description="Find very important information including email, phone number, etc. on Instagram pages",
    include_package_data=True,
    #url='https://github.com/attakercyebr/M4nifest0-IG-Finder',
    entry_points = {'console_scripts': ['M4nifest0 = M4nifest0.hack4lx:main']},
    classifiers=[
        "Programming Language :: Python",
      
    ],
)
