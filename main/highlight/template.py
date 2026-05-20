pkgname = "highlight"
pkgver = "4.19"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["boost-devel", "lua5.4-devel"]
pkgdesc = "Syntax highlighter program"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause"
url = "http://www.andre-simon.de/doku/highlight/en/highlight.html"
source = f"http://www.andre-simon.de/zip/highlight-{pkgver}.tar.bz2"
sha256 = "11c01ec5965ae9b0319bd7cb1a04ffd85ad8586176033a1fbe9a82f08e99ed56"
hardening = ["vis", "cfi"]
# No tests, can't be bothered to fix cross
options = ["!check", "!distlicense", "!cross"]
