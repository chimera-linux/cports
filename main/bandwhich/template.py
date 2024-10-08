pkgname = "bandwhich"
pkgver = "0.23.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Terminal bandwidth utilization tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/imsnif/bandwhich"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aafb96d059cf9734da915dca4f5940c319d2e6b54e2ffb884332e9f5e820e6d7"

if self.profile().arch == "ppc64le":
    # tests compare snapshot output which is different on ppc64le on the builder
    # only for some reason
    options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
