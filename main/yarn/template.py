pkgname = "yarn"
pkgver = "1.22.22"
pkgrel = 0
depends = ["nodejs"]
pkgdesc = "Package manager for Node"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://yarnpkg.com"
source = f"https://github.com/yarnpkg/yarn/releases/download/v{pkgver}/yarn-v{pkgver}.tar.gz"
sha256 = "88268464199d1611fcf73ce9c0a6c4d44c7d5363682720d8506f6508addf36a0"


def install(self):
    self.install_file("lib/v8-compile-cache.js", "usr/lib/yarn")
    self.install_file("lib/cli.js", "usr/lib/yarn")
    self.install_bin("bin/yarn.js", name="yarn")
    self.install_license("LICENSE")
