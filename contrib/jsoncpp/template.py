pkgname = "jsoncpp"
pkgver = "1.9.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C++ library for interacting with JSON"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://github.com/open-source-parsers/jsoncpp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f409856e5920c18d0c2fb85276e24ee607d2a09b5e7d5f0a371368903c275da2"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("jsoncpp-devel")
def _devel(self):
    return self.default_devel()
