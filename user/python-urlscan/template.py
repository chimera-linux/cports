pkgname = "python-urlscan"
pkgver = "1.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-typing_extensions",
    "python-urwid",
]
pkgdesc = "Mutt and terminal url selector"
license = "GPL-2.0-only"
url = "https://github.com/firecat53/urlscan"
source = f"$(PYPI_SITE)/u/urlscan/urlscan-{pkgver}.tar.gz"
sha256 = "e4f01037dcb84f0cc5733b9423732ebf368cb9b4c9714bdaf7dd336d883a78b2"
# no tests defined
options = ["!check"]
