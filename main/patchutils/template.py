pkgname = "patchutils"
pkgver = "0.4.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "xmlto"]
makedepends = ["pcre2-devel"]
depends = ["perl"]
pkgdesc = "Collection of programs for manipulating patch files"
license = "GPL-2.0-or-later"
url = "http://cyberelk.net/tim/patchutils"
source = (
    f"http://cyberelk.net/tim/data/patchutils/stable/patchutils-{pkgver}.tar.xz"
)
sha256 = "8386a35a4d2d3cbc28fdcc93c5be007c382c78e3ee079070139f0d822e013325"
