pkgname = "cpdup"
pkgver = "1.22"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Comprehensive filesystem mirroring and backup program"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-2-Clause"
url = "https://github.com/DragonFlyBSD/cpdup"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2dbfa16a080f8dce1be64a511e785b8491e59be8a0f3d1cef035d08147cc4793"
# Not available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
