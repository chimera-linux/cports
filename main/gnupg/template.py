pkgname = "gnupg"
pkgver = "2.4.9"
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
sha256 = "dd17ab2e9a04fd79d39d853f599cbc852062ddb9ab52a4ddeb4176fd8b302964"
