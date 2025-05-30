pkgname = "rtrlib"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
# require network
make_check_args = ["-E", "(test_dynamic_groups|test_live_validation)"]
hostmakedepends = ["cmake", "doxygen", "ninja", "pkgconf"]
makedepends = ["libssh-devel"]
pkgdesc = "Open-source C implementation of the RPKI/Router Protocol client"
license = "MIT"
url = "https://github.com/rtrlib/rtrlib"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8cc99343dc3ea8908cd9710ba1f72a1ddce591bf80bfd7d656dbc4568f560ada"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rtrlib-devel")
def _(self):
    return self.default_devel()
