pkgname = "libomemo-c"
pkgver = "0.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "protobuf-c-devel",
]
makedepends = [
    "check-devel",
    "openssl3-devel",
    "protobuf-c-devel",
]
pkgdesc = "Fork of libsignal-protocol-c with OMEMO 0.4.0+ support"
license = "GPL-3.0-or-later"
url = "https://github.com/dino/libomemo-c"
source = f"https://github.com/dino/libomemo-c/releases/download/v{pkgver}/libomemo-c-{pkgver}.tar.gz"
sha256 = "766827c07ff2cdc4deaf87bd9485474ed4aeea2fa5152593bf49fabe22b5865f"


@subpackage("libomemo-c-devel")
def _(self):
    return self.default_devel()
