pkgname = "libopenmpt"
pkgver = "0.8.2"
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
sha256 = "844e4ff98dbd9942bbe4a1048226f91f8bc5b460b7bec6489e67cedb3e0aac37"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _(self):
    return self.default_devel()
