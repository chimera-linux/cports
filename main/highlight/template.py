pkgname = "highlight"
pkgver = "4.13"
pkgrel = 1
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["boost-devel", "lua5.4-devel"]
pkgdesc = "Syntax highlighter program"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause"
url = "http://www.andre-simon.de/doku/highlight/en/highlight.html"
source = f"http://www.andre-simon.de/zip/highlight-{pkgver}.tar.bz2"
sha256 = "5ea95f9ab03dd857de4ce0cde68ffacc041d0223bbce0893e2ada9c85503488c"
hardening = ["vis", "cfi"]
# No tests, can't be bothered to fix cross
options = ["!check", "!distlicense", "!cross"]
