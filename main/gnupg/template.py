pkgname = "gnupg"
pkgver = "2.4.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-all-tests"]
configure_gen = []
make_check_env = {"TESTFLAGS": f"--parallel={self.conf_jobs}"}
hostmakedepends = ["pkgconf", "libgpg-error-progs"]
# TODO: switch to libedit once it gains missing features
makedepends = [
    "bzip2-devel",
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
sha256 = "67ebe016ca90fa7688ce67a387ebd82c6261e95897db7b23df24ff335be85bc6"
