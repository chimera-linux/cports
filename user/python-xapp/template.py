pkgname = "python-xapp"
pkgver = "2.4.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
depends = ["gtk+3", "python-gobject", "python-psutil", "xapp"]
pkgdesc = "Python Xapp library"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/python3-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "39e4c3f06732e9d197b9aed31444653da2976c1d66dded870b52cc9782f2237d"
# No tests
options = ["!check"]
