pkgname = "keyd"
pkgver = "2.5.0"
pkgrel = 0
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
sha256 = "93ec6c153ef673a7a8b4d8b686494dee11d182513f4531c71dce15a8db7f6c1c"
hardening = ["vis", "cfi"]
# no tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "keyd")
    self.install_sysusers(self.files_path / "keyd.conf")
