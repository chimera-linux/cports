pkgname = "p11-kit"
pkgver = "0.25.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibffi=enabled",
    "-Dsystemd=disabled",
    "-Dbash_completion=disabled",
    "-Dgtk_doc=true",
    "-Dman=true",
    "-Dnls=true",
    "-Dtrust_module=enabled",
    "-Dtrust_paths=/etc/ssl/certs/ca-certificates.crt",
    "-Dglib_prefix=/usr",
    "-Dtest=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "gtk-doc-tools",
    "libtasn1-progs",
]
makedepends = ["libtasn1-devel", "libffi8-devel"]
pkgdesc = "Provides a way to load and enumerate PKCS#11 modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/p11-glue/p11-kit"
source = f"{url}/releases/download/{pkgver}/p11-kit-{pkgver}.tar.xz"
sha256 = "04d0a86450cdb1be018f26af6699857171a188ac6d5b8c90786a60854e1198e5"


def post_install(self):
    self.install_license("COPYING")

    self.rename("etc/pkcs11/pkcs11.conf.example", "pkcs11.conf")


@subpackage("p11-kit-devel")
def _(self):
    return self.default_devel()
