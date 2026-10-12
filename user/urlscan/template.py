pkgname = "urlscan"
pkgver = "1.2.0"
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
sha256 = "27ffbc49a98da0f3d0a533b23e04c71784d4e10fbf2ee4e1f443ef39364fce5b"
# no tests defined
options = ["!check"]
