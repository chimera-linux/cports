pkgname = "python-xapp"
pkgver = "3.0.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "python"]
depends = ["python-gobject", "python-psutil", "xapp"]
pkgdesc = "Python bindings and helpers for Xapp"
license = "LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/python3-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "30cf81249a7c5cabc25e465e369928724e091e95c5095704518f14ca6fd11f41"
# no tests
options = ["!check"]
