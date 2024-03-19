pkgname = "bandwhich"
pkgver = "0.22.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Terminal bandwidth utilization tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/imsnif/bandwhich"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4c41719549e05dbaac1bc84828269e59b2f2032e76ae646da9b9e3b87e5a5fd1"


def post_install(self):
    self.install_license("LICENSE.md")
