pkgname = "pam_p11"
pkgver = "0.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-pamdir=/usr/lib/security"]
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "slibtool"]
makedepends = ["libp11-devel", "linux-pam-devel", "openssl3-devel"]
pkgdesc = "PAM module for PKCS#11 token authentication"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/pam_p11"
source = f"{url}/releases/download/pam_p11-{pkgver}/pam_p11-{pkgver}.tar.gz"
sha256 = "d28693587edfeeea2864af806245817532034c054183c3a9f9f84edec16b4b40"
# no test suite
options = ["!check"]
