pkgname = "cmatrix"
pkgver = "2.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DCMAKE_C_COMPILER=clang",
    "-G Ninja",
]
hostmakedepends = [
    "ncurses-devel",
    "cmake"
]
makedepends = [
    "ncurses-devel",
    "ninja",
    "cmake"
]
pkgdesc = "Terminal based 'The Matrix' like implementation"
license = "GPL-3.0-or-later"
url = "https://github.com/abishekvashok/cmatrix"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad93ba39acd383696ab6a9ebbed1259ecf2d3cf9f49d6b97038c66f80749e99a"
