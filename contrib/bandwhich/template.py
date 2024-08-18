pkgname = "bandwhich"
pkgver = "0.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Terminal bandwidth utilization tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/imsnif/bandwhich"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "58b94588ec919fd802fc25cd209084ecc9acdfd99d5478d5ec76670774ff5886"

if self.profile().arch == "ppc64le":
    # tests compare snapshot output which is different on ppc64le on the builder
    # only for some reason
    options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
