pkgname = "spice"
pkgver = "0.15.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-opengl",
    "--enable-smartcard",
    "--with-sasl",
    "--disable-static",
    "--enable-xinerama",
    "--enable-opus",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "python"]
makedepends = [
    "spice-protocol",
    "pixman-devel",
    "libjpeg-turbo-devel",
    "zlib-devel",
    "libsasl-devel",
    "libcacard-devel",
    "opus-devel",
    "gstreamer-devel",
    "lz4-devel",
    "openssl-devel",
    "gnutls-devel",
    "gdk-pixbuf-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "opus-devel",
]
checkdepends = ["glib-networking"]
pkgdesc = "Simple Protocol for Independent Computing Environments"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://www.spice-space.org"
source = f"https://www.spice-space.org/download/releases/spice-{pkgver}.tar.bz2"
sha256 = "6d9eb6117f03917471c4bc10004abecff48a79fb85eb85a1c45f023377015b81"

if self.profile().endian == "big":
    broken = "only supports little-endian"


@subpackage("spice-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
