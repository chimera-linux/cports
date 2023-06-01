pkgname = "gnupg"
pkgver = "2.4.2"
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
sha256 = "97eb47df8ae5a3ff744f868005a090da5ab45cb48ee9836dbf5ee739a4e5cf49"
