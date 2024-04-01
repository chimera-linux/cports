pkgname = "parallel"
pkgver = "20240322"
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
sha256 = "0b17029a203dabf7ba6ca7e52c2d3910fff46b2979476e12a9110920b79e6a95"
