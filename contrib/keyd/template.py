pkgname = "keyd"
pkgver = "2.4.3"
pkgrel = 2
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = ["linux-headers"]
pkgdesc = "Key remapping daemon for linux"
maintainer = "feurry <=feurry@gmail.com>"
license = "MIT"
url = "https://github.com/rvaiya/keyd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d4075f673879f4950c1c0d43985797603200e993596a5d7fcec1597c2350c380"
hardening = ["vis", "cfi"]
# no tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "keyd")
    self.install_file(self.files_path / "keyd.conf", "usr/lib/sysusers.d")
