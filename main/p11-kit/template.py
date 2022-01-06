pkgname = "p11-kit"
pkgver = "0.24.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibffi=enabled", "-Dsystemd=disabled", "-Dbash_completion=disabled",
    "-Dgtk_doc=true", "-Dman=true", "-Dnls=true", "-Dtrust_module=enabled",
    "-Dtrust_paths=/etc/ssl/certs/ca-certificates.crt", "-Dtest=true",
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "gtk-doc-tools", "libtasn1-progs"
]
makedepends = [
    "libtasn1-devel", "libffi-devel"
]
pkgdesc = "Provides a way to load and enumerate PKCS#11 modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/p11-glue/p11-kit"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "81e6140584f635e4e956a1b93a32239acf3811ff5b2d3a5c6094e94e99d2c685"

def post_install(self):
    self.install_license("COPYING")

    self.mv(
        self.destdir / "etc/pkcs11/pkcs11.conf.example",
        self.destdir / "etc/pkcs11/pkcs11.conf"
    )

@subpackage("p11-kit-devel")
def _devel(self):
    return self.default_devel()
