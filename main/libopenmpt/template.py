pkgname = "libopenmpt"
pkgver = "0.8.9"
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
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "d7ce84fd05d686c4bcf66af40eae857afa371442db60eeda3f874bd6cf6fc318"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _(self):
    return self.default_devel()
