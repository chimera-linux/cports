pkgname = "patchutils"
pkgver = "0.4.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "xmlto"]
makedepends = ["pcre2-devel"]
depends = ["perl"]
pkgdesc = "Collection of programs for manipulating patch files"
maintainer = "reocat <ng.ct_ml@tuta.io>"
license = "GPL-2.0-or-later"
url = "http://cyberelk.net/tim/patchutils"
source = (
    f"http://cyberelk.net/tim/data/patchutils/stable/patchutils-{pkgver}.tar.xz"
)
sha256 = "8875b0965fe33de62b890f6cd793be7fafe41a4e552edbf641f1fed5ebbf45ed"
patch_style = "patch"
