pkgname = "libopenmpt"
pkgver = "0.7.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-portaudio",
    "--without-portaudiocpp",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "flac-devel",
    "libogg-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "mpg123-devel",
    "zlib-devel",
]
pkgdesc = "Library for rendering tracker music to PCM"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "87778c8046a226c6cbfb114f4c8e3e27c121b7b3dccce5cb7de45899250274cc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _devel(self):
    return self.default_devel()
