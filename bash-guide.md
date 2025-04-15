# Bash Guide

> [!NOTE]
> This guide goes through how to clone this repository using a bash terminal (git). I recommend to read everything **within** just because of text formatting and everything (I am used to using [mystmd](https://mystmd.org) and [myst-parser](https://myst-parser.readthedocs.io/en/latest/) but I intentionally switched to use [GitHub Flavoured Markdown](https://github.github.com/gfm/) for this)

[![GitHub - Git Guides](https://img.shields.io/badge/Github-Git_Guides-181717?style=for-the-badge&logo=github&logoColor=snow)](https://github.com/git-guides/)

## GitHub Desktop
[![GitHub Desktop Documentation](https://img.shields.io/badge/GitHub_Desktop-Documentation-mediumorchid?style=for-the-badge&logo=github&logoColor=lavender)](https://docs.github.com/en/desktop) [![GitHub Desktop Release Note](https://img.shields.io/badge/GitHub_Desktop-Release_Note-mediumorchid?style=for-the-badge&logo=github&logoColor=lavendar)](https://desktop.github.com/release-note/) [![GitHub Desktop Download](https://img.shields.io/badge/GitHub_Desktop-Download-mediumorchid?style=for-the-badge&logo=github&logoColor=lavender)](https://desktop.github.com/download/)

The easiest way is to install [GitHub Desktop](https://github.com/apps/desktop) which will install Git along.

## Windows

###

1. Visit Git's Download page and install the latest version<br />[![Git Download](https://img.shields.io/badge/Git-Downloads-F05032?style=for-the-badge&logo=git&logoColor=snow)](https://git-scm.com/downloads)

> [!NOTE]
> Alternatively, you can also download it from Git for Windows, but I strongly recommend downloading from actual git page just because it has a seperate bash terminal.<br />
[![Git for Windows](https://img.shields.io/badge/Git_for_Windows-80b3ff?style=for-the-badge&logo=gitforwindows&logoColor=snow)](https://gitforwindows.org/)

> The latest version as of I'm making this guide for Git is 2.49.0

2. Activate the installation application and following the instruction from git setup wizard until installation is completed.
3. Go to `Git Bash` and type the following line to verify your installation
```bash
git version
```
4. In `Git Bash`, add the following line, which will clone this repository
> [!CAUTION]
> Note that if you do `git clone` immediately without choosing a specific folder, you will waste time to dig through your C drive! Otherwise, for Windows 11, you can go to the folder you want to clone this repository to, right click at an empty area, choose `Show more options`, then choose `Open Git Bash here`. It should open `Git Bash` terminal, then you can clone it and save your folder in there. For Windows 10, you should be able to see `Open Git Bash here` as soon as you right click.  

```bash
git clone https://github.com/beatrix-chan/rootFinding-numericalMethods.git
```