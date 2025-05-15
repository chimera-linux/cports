pkgname = "gnupg"
pkgver = "2.4.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--enable-all-tests",
]
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
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = f"https://gnupg.org/ftp/gcrypt/gnupg/gnupg-{pkgver}.tar.bz2"
sha256 = "b58c80d79b04d3243ff49c1c3fc6b5f83138eb3784689563bcdd060595318616"
