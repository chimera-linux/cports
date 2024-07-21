pkgname = "libopenmpt"
pkgver = "0.7.9"
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
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for rendering tracker music to PCM"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "0386e918d75d797e79d5b14edd0847165d8b359e9811ef57652c0a356a2dfcf4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _devel(self):
    return self.default_devel()
