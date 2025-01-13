pkgname = "libvncserver"
pkgver = "0.9.15"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_EXAMPLES=OFF",
    "-DWITH_GCRYPT=OFF",
    "-DWITH_GNUTLS=OFF",
    "-DWITH_SYSTEMD=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "openssl-devel",
    "lzo-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "VNC client/server libraries"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/LibVNC/libvncserver"
source = f"{url}/archive/refs/tags/LibVNCServer-{pkgver}.tar.gz"
sha256 = "62352c7795e231dfce044beb96156065a05a05c974e5de9e023d688d8ff675d7"


@subpackage("libvncserver-devel")
def _(self):
    return self.default_devel()
