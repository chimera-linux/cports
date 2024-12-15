pkgname = "highlight"
pkgver = "4.14"
pkgrel = 1
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["boost-devel", "lua5.4-devel"]
pkgdesc = "Syntax highlighter program"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause"
url = "http://www.andre-simon.de/doku/highlight/en/highlight.html"
source = f"http://www.andre-simon.de/zip/highlight-{pkgver}.tar.bz2"
sha256 = "099e0eaf38709fe430108125ad9d35f7aacfa05d5d41ad20f405593b575627c5"
hardening = ["vis", "cfi"]
# No tests, can't be bothered to fix cross
options = ["!check", "!distlicense", "!cross"]
