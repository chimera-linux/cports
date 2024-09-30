pkgname = "libopenmpt"
pkgver = "0.7.10"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "093713c1c1024f4f10c4779a66ceb2af51fb7c908a9e99feb892d04019220ba1"
patch_style = "patch"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _(self):
    return self.default_devel()
