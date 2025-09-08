pkgname = "highlight"
pkgver = "4.16"
pkgrel = 1
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["boost-devel", "lua5.4-devel"]
pkgdesc = "Syntax highlighter program"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause"
url = "http://www.andre-simon.de/doku/highlight/en/highlight.html"
source = f"http://www.andre-simon.de/zip/highlight-{pkgver}.tar.bz2"
sha256 = "92261ff5c27c73e7a5c85ab65ada2a2edf8aa3dbe9c9c3d8e82e062088e60e5a"
hardening = ["vis", "cfi"]
# No tests, can't be bothered to fix cross
options = ["!check", "!distlicense", "!cross"]
