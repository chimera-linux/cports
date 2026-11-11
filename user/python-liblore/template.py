pkgname = "python-liblore"
pkgver = "0.10.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-authheaders",
    "python-requests",
]
checkdepends = [
    "python-pytest",
    "python-pytest-asyncio",
    "python-responses",
    "python-typing_extensions",
    *depends,
]
pkgdesc = "Library for lore.kernel.org access"
license = "GPL-2.0-or-later"
url = "https://git.kernel.org/pub/scm/utils/liblore/liblore.git"
# pypi source does not have conftest.py
source = f"https://git.kernel.org/pub/scm/utils/liblore/liblore.git/snapshot/liblore-{pkgver}.tar.gz"
sha256 = "0c295f518e199e51cbd51d88e3e81b6d11dd441ee00ae027cb7d7bebff945663"
