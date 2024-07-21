pkgname = "parallel"
pkgver = "20240722"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
]
depends = ["perl"]
pkgdesc = "Shell tool for executing jobs in parallel"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/parallel"
source = f"https://ftp.gnu.org/gnu/parallel/parallel-{pkgver}.tar.bz2"
sha256 = "c7335471f776af28bea9464ad85a50f2ed120f78fbf75ead6647aeea8e0e53f0"
