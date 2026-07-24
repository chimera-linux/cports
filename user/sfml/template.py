pkgname = "sfml"
pkgver = "3.1.0"
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
    "libssh2-devel",
    "libvorbis-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxrandr-devel",
    "mbedtls-devel",
    "mesa-devel",
]
pkgdesc = "C++ multimedia Library"
license = "Zlib"
url = "https://www.sfml-dev.org"
_sheenbidi_ver = "3.0.0"
source = [
    f"https://github.com/SFML/SFML/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/Tehreer/SheenBidi/archive/refs/tags/v{_sheenbidi_ver}.tar.gz",
]
source_paths = [
    ".",
    "build/_deps/sheenbidi-src",
]
sha256 = [
    "91209a112c2bd0bc6f4ce0d5f3e413cfb48b57c0de59f5507dc81f71b1ad7a5c",
    "86c56014034739ba39a24c23eb00323b0bf6f737354f665786015fca842af786",
]


@subpackage("sfml-devel")
def _(self):
    return self.default_devel()
