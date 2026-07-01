pkgname = "libsodium"
pkgver = "1.0.22"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["lt_cv_prog_compiler_static_works=yes"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Modern and easy-to-use crypto library"
license = "ISC"
url = "https://libsodium.org"
source = f"https://download.libsodium.org/libsodium/releases/libsodium-{pkgver}.tar.gz"
sha256 = "adbdd8f16149e81ac6078a03aca6fc03b592b89ef7b5ed83841c086191be3349"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsodium-devel")
def _(self):
    return self.default_devel()
