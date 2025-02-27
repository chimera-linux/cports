pkgname = "libsodium"
pkgver = "1.0.20"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["lt_cv_prog_compiler_static_works=yes"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Modern and easy-to-use crypto library"
license = "ISC"
url = "https://libsodium.org"
source = f"https://download.libsodium.org/libsodium/releases/libsodium-{pkgver}.tar.gz"
sha256 = "ebb65ef6ca439333c2bb41a0c1990587288da07f6c7fd07cb3a18cc18d30ce19"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsodium-devel")
def _(self):
    return self.default_devel()
