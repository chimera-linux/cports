pkgname = "gnupg"
pkgver = "2.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-all-tests"]
configure_gen = []
make_check_env = {"TESTFLAGS": f"--parallel={self.conf_jobs}"}
hostmakedepends = ["pkgconf", "libgpg-error-progs"]
# TODO: switch to libedit once it gains missing features
makedepends = [
    "libbz2-devel",
    "libassuan-devel",
    "libksba-devel",
    "npth-devel",
    "libgpg-error-devel",
    "libgcrypt-devel",
    "gnutls-devel",
    "libusb-devel",
    "sqlite-devel",
    "readline-devel",
]
depends = ["pinentry"]
pkgdesc = "GNU Privacy Guard (2.x)"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a271ae6d732f6f4d80c258ad9ee88dd9c94c8fdc33c3e45328c4d7c126bd219d"
