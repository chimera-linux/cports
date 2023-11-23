pkgname = "parallel"
pkgver = "20231122"
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
sha256 = "822c9cf8aa171520ad867db13ef13426669bd164c81b900a3dbcb556611beae2"
