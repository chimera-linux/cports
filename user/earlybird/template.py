pkgname = "earlybird"
pkgver = "4.6.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["git"]
pkgdesc = "Sensitive data scanner for source code repositories"
license = "Apache-2.0"
url = "https://github.com/americanexpress/earlybird"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "04bfc2de0d6701e20ddba59216bc14af52d5978fade597097cc34c2830361a19"
# check: depends on this package being built from its own cloned git repo, and as this is a tarball, the test is nonfunctional
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
