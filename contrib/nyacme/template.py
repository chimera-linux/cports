pkgname = "nyacme"
pkgver = "0.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-dnspython",
    "uacme",
]
pkgdesc = "Wrapper for uacme"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://git.ddd.rip/ptrcnull/nyacme"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "41cb2814ce1bd2f466a91743f550f455cd31be8de9c9127845d86c67c799b598"
# tests do not exist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
