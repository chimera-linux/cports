pkgname = "lua5.4-mediator_lua"
pkgver = "1.1.0"
pkgrel = 0
pkgdesc = "Mediator pattern implementation for pub-sub management"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "http://www.olivinelabs.com/mediator_lua"
source = f"https://github.com/Olivine-Labs/mediator_lua/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b4fda8c0455c41b13a2bfabcad4d937f818547bf8ed4258f5d37cf5e350a9850"
# reamde claims the code is  MIT licensed however noLICENSE file is shipped
options = ["!distlicense"]


def install(self):
    self.install_file(
        "src/mediator.lua",
        "usr/share/lua/5.4",
        name="mediator.lua",
    )
