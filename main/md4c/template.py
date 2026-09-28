pkgname = "md4c"
pkgver = "0.5.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Fast CommonMark compliant markdown parser"
license = "MIT"
url = "https://github.com/mity/md4c"
source = f"{url}/archive/release-{pkgver}.tar.gz"
sha256 = "353c346f376b87c954a13f3415ede2d51264cc61dc5abcd38ff1d2aa0d059b9e"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("md4c-devel")
def _(self):
    return self.default_devel()
