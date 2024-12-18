pkgname = "libopenmpt"
pkgver = "0.7.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-portaudio",
    "--without-portaudiocpp",
]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "flac-devel",
    "libogg-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "mpg123-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for rendering tracker music to PCM"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "79ab3ce3672601e525b5cc944f026c80c03032f37d39caa84c8ca3fdd75e0c98"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _(self):
    return self.default_devel()
