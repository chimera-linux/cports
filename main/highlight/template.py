pkgname = "highlight"
pkgver = "4.17"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["boost-devel", "lua5.4-devel"]
pkgdesc = "Syntax highlighter program"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause"
url = "http://www.andre-simon.de/doku/highlight/en/highlight.html"
source = f"http://www.andre-simon.de/zip/highlight-{pkgver}.tar.bz2"
sha256 = "d4f7baa98bd162d8f15642793bd7b8671cfa47ad5100707ac609be3ed486ff94"
hardening = ["vis", "cfi"]
# No tests, can't be bothered to fix cross
options = ["!check", "!distlicense", "!cross"]
