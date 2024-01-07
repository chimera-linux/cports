pkgname = "libsodium"
pkgver = "1.0.19"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["lt_cv_prog_compiler_static_works=yes"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Modern and easy-to-use crypto library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://libsodium.org"
source = f"https://download.libsodium.org/{pkgname}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "018d79fe0a045cca07331d37bd0cb57b2e838c51bc48fd837a1472e50068bbea"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsodium-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
