pkgname = "gnupg"
pkgver = "2.4.7"
pkgrel = 0
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
    "openldap-devel",
    "readline-devel",
    "sqlite-devel",
]
depends = ["pinentry"]
pkgdesc = "GNU Privacy Guard 2.x"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = f"https://gnupg.org/ftp/gcrypt/gnupg/gnupg-{pkgver}.tar.bz2"
sha256 = "7b24706e4da7e0e3b06ca068231027401f238102c41c909631349dcc3b85eb46"
