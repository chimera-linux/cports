pkgname = "libyaml"
pkgver = "0.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Fast YAML 1.1 parser and emitter library"
license = "MIT"
url = "https://pyyaml.org/wiki/LibYAML"
source = f"https://github.com/yaml/libyaml/archive/{pkgver}.tar.gz"
sha256 = "fa240dbf262be053f3898006d502d514936c818e422afdcf33921c63bed9bf2e"


def post_install(self):
    self.install_license("License")


@subpackage("libyaml-devel")
def _(self):
    return self.default_devel()
