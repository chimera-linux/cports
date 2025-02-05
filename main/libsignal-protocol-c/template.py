pkgname = "libsignal-protocol-c"
pkgver = "2.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
]
hostmakedepends = ["cmake", "pkgconf", "ninja", "openssl3-devel"]
makedepends = ["openssl3-devel"]
checkdepends = ["check-devel"]
pkgdesc = "Signal protocol C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.whispersystems.org"
source = f"https://github.com/signalapp/libsignal-protocol-c/archive/v{pkgver}.tar.gz"
sha256 = "c22e7690546e24d46210ca92dd808f17c3102e1344cd2f9a370136a96d22319d"


@subpackage("libsignal-protocol-c-devel")
def _(self):
    return self.default_devel()
