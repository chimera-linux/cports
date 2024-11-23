pkgname = "direnv"
pkgver = "2.35.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Environment variables loader"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/direnv/direnv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a7aaec49d1b305f0745dad364af967fb3dc9bb5befc9f29d268d528b5a474e57"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)
