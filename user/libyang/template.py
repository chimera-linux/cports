pkgname = "libyang"
pkgver = "2.1.148"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "YANG data modelling language parser and toolkit"
license = "BSD-3-Clause"
url = "https://github.com/CESNET/libyang"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "77a0aaaeb3df720aeb70d6896e32e2c2be099d48df73e3cfb52567051af3e44b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libyang-devel")
def _(self):
    return self.default_devel()
