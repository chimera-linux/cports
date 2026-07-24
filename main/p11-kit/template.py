pkgname = "p11-kit"
pkgver = "0.26.4"
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
    "gettext",
    "gtk-doc-tools",
    "libtasn1-progs",
    "meson",
    "pkgconf",
]
makedepends = ["libtasn1-devel", "libffi8-devel"]
pkgdesc = "Provides a way to load and enumerate PKCS#11 modules"
license = "BSD-3-Clause"
url = "https://github.com/p11-glue/p11-kit"
source = f"{url}/releases/download/{pkgver}/p11-kit-{pkgver}.tar.xz"
sha256 = "89c3ffb10e076ee036e14732bf6547a1e1c4fb48699a5dee7ceb5ce4f7c0c462"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")

    self.rename("etc/pkcs11/pkcs11.conf.example", "pkcs11.conf")


@subpackage("p11-kit-devel")
def _(self):
    return self.default_devel()
