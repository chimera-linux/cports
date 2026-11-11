pkgname = "python-ezgb"
pkgver = "0.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-pygit2",
]
checkdepends = [
    "python-pytest",
    "python-typing_extensions",
    *depends,
]
pkgdesc = "Library for git-bug issues"
license = "GPL-2.0-or-later"
url = "https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git"
# pypi source does not have conftest.py
source = f"https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git/snapshot/ezgb-{pkgver}.tar.gz"
sha256 = "5b70526e35ac1796dd0143c94b6bdc3d335a7ad06f42c17e707b7ecb77fe31a6"
