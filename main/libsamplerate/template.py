pkgname = "libsamplerate"
pkgver = "0.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["fftw-devel", "libsndfile-devel"]
pkgdesc = "Sample Rate Converter for audio"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://libsndfile.github.io/libsamplerate"
source = f"https://github.com/libsndfile/libsamplerate/releases/download/{pkgver}/libsamplerate-{pkgver}.tar.xz"
sha256 = "3258da280511d24b49d6b08615bbe824d0cacc9842b0e4caf11c52cf2b043893"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libsamplerate-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])
