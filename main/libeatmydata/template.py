pkgname = "libeatmydata"
pkgver = "131"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "libtool",
]
checkdepends = [
    "bash",
    "strace",
]
pkgdesc = "Preloadable library to stub out fsync"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.flamingspork.com/projects/libeatmydata"
source = f"https://github.com/stewartsmith/libeatmydata/releases/download/v{pkgver}/libeatmydata-{pkgver}.tar.gz"
sha256 = "cf18a8c52138a38541be3478af446c06048108729d7e18476492d62d54baabc4"
