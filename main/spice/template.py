pkgname = "spice"
pkgver = "0.15.2"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-opengl",
    "--enable-opus",
    "--enable-smartcard",
    "--enable-xinerama",
    "--with-sasl",
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "gdk-pixbuf-devel",
    "gnutls-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libcacard-devel",
    "libjpeg-turbo-devel",
    "libsasl-devel",
    "lz4-devel",
    "openssl3-devel",
    "opus-devel",
    "pixman-devel",
    "spice-protocol",
    "zlib-ng-compat-devel",
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
def _(self):
    return self.default_devel()
