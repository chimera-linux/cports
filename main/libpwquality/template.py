pkgname = "libpwquality"
pkgver = "1.4.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--enable-pam", "--with-securedir=/usr/lib/security",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "gettext-tiny-devel", "python-devel"]
makedepends = ["cracklib-devel", "linux-pam-devel", "python-devel"]
depends = ["cracklib-words"]
pkgdesc = "Library for password quality checking"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause OR GPL-2.0-or-later"
url = "https://github.com/libpwquality/libpwquality"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d43baf23dc6887fe8f8e9b75cabaabc5f4bbbaa0f9eff44278d276141752a545"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libpwquality-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpwquality-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["cracklib-devel"]

    return ["usr/lib/python*"]
