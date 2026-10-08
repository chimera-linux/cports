pkgname = "znc"
pkgver = "1.10.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWANT_PERL=ON",
    "-DWANT_PYTHON=ON",
    "-DWANT_TCL=ON",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "perl",
    "pkgconf",
    "python",
]
makedepends = [
    "argon2-devel",
    "boost-devel",
    "dinit-chimera",
    "icu-devel",
    "libsasl-devel",
    "openssl3-devel",
    "python-devel",
    "tcl-devel",
    "zlib-ng-devel",
]
pkgdesc = "IRC bouncer with module support"
license = "Apache-2.0"
url = "https://znc.in"
source = f"{url}/releases/archive/znc-{pkgver}.tar.gz"
sha256 = "68f3f6641b480c041010c5596e1234043e05c9137eda06233845017603095f5b"


def post_install(self):
    self.install_service(self.files_path / "znc")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
