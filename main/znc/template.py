pkgname = "znc"
pkgver = "1.9.1"
pkgrel = 2
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
    "icu-devel",
    "libsasl-devel",
    "openssl3-devel",
    "python-devel",
    "tcl-devel",
    "zlib-ng-devel",
]
pkgdesc = "IRC bouncer with module support"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "Apache-2.0"
url = "https://znc.in"
source = f"{url}/releases/znc-{pkgver}.tar.gz"
sha256 = "e8a7cf80e19aad510b4e282eaf61b56bc30df88ea2e0f64fadcdd303c4894f3c"


def post_install(self):
    self.install_service(self.files_path / "znc")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
