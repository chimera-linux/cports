pkgname = "v2ray"
pkgver = "5.47.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./main"]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Platform for building proxies to bypass network restrictions"
license = "MIT"
url = "https://v2fly.org"
source = (
    f"https://github.com/v2fly/v2ray-core/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "90ef85f8f2c5478fc1e4f455b40eaf35a1738e06ef519b85a62c0763e2391405"
# check: needs network access
options = ["!check"]


def install(self):
    self.install_bin("build/main", name="v2ray")
    self.install_license("LICENSE")
    self.install_file(
        "release/config/config.json",
        dest="usr/share/etc/v2ray",
    )
    self.install_sysusers("^/sysusers.conf")
    self.install_service("^/v2ray")
