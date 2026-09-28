pkgname = "cmocka"
pkgver = "1.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUNIT_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Unit testing framework in C"
license = "Apache-2.0"
url = "https://cmocka.org"
source = f"{url}/files/{pkgver[:-2]}/cmocka-{pkgver}.tar.xz"
sha256 = "58435b558766d7f4c729ba163bdf3aec38bed3bc766dab684e3526ed0aa7c780"


@subpackage("cmocka-devel")
def _(self):
    return self.default_devel()
