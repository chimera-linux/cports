pkgname = "sfml"
pkgver = "3.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=YES",
    # doesn't install all .pc's, breaks 001_runtime_deps
    "-DSFML_INSTALL_PKGCONFIG_FILES=NO",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "flac-devel",
    "freetype-devel",
    "libogg-devel",
    "libvorbis-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxrandr-devel",
    "mesa-devel",
]
pkgdesc = "C++ multimedia Library"
license = "Zlib"
url = "https://www.sfml-dev.org"
source = f"https://github.com/SFML/SFML/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0034e05f95509e5d3fb81b1625713e06da7b068f210288ce3fd67106f8f46995"


@subpackage("sfml-devel")
def _(self):
    return self.default_devel()
