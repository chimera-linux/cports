pkgname = "parallel"
pkgver = "20231222"
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
sha256 = "19466ddc6fa9bbd7be1886f5404129af12448f12ecd3b9562e985ada84da9baa"
