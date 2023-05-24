pkgname = "libsodium"
pkgver = "1.0.18"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["lt_cv_prog_compiler_static_works=yes"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Modern and easy-to-use crypto library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://libsodium.org"
source = f"https://download.libsodium.org/{pkgname}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "6f504490b342a4f8a4c4a02fc9b866cbef8622d5df4e5452b46be121e46636c1"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsodium-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
