pkgname = "gnupg"
pkgver = "2.4.5"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-all-tests"]
configure_gen = []
make_check_env = {"TESTFLAGS": f"--parallel={self.conf_jobs}"}
hostmakedepends = ["pkgconf", "libgpg-error-progs"]
# TODO: switch to libedit once it gains missing features
makedepends = [
    "bzip2-devel",
    "gnutls-devel",
    "libassuan-devel",
    "libgcrypt-devel",
    "libgpg-error-devel",
    "libksba-devel",
    "libusb-devel",
    "npth-devel",
    "readline-devel",
    "sqlite-devel",
]
depends = ["pinentry"]
pkgdesc = "GNU Privacy Guard (2.x)"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f68f7d75d06cb1635c336d34d844af97436c3f64ea14bcb7c869782f96f44277"
