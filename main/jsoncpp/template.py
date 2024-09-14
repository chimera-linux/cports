pkgname = "jsoncpp"
pkgver = "1.9.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C++ library for interacting with JSON"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://github.com/open-source-parsers/jsoncpp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f93b6dd7ce796b13d02c108bc9f79812245a82e577581c4c9aabe57075c90ea2"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("jsoncpp-devel")
def _(self):
    return self.default_devel()
