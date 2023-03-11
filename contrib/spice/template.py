pkgname = "spice"
pkgver = "0.15.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-opengl", "--enable-smartcard", "--with-sasl", "--disable-static", "--enable-xinerama",
                  "--enable-opus"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "python"]
makedepends = ["spice-protocol", "pixman-devel", "libjpeg-turbo-devel", "zlib-devel", "libsasl-devel",
               "libcacard-devel", "opus-devel", "gstreamer-devel", "liblz4-devel", "openssl-devel", "gnutls-devel",
               "gdk-pixbuf-devel", "gstreamer-devel", "opus-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "Simple Protocol for Independent Computing Environments"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://www.spice-space.org"
source = f"https://www.spice-space.org/download/releases/spice-{pkgver}.tar.bz2"
sha256 = "ada9af67ab321916bd7eb59e3d619a4a7796c08a28c732edfc7f02fc80b1a37a"

if self.profile().endian == "big":
    broken = "only supports little-endian"


@subpackage("spice-devel")
def _devel(self):
    return self.default_devel()
