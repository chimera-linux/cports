pkgname = "v2ray"
pkgver = "5.20.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./main"]
hostmakedepends = ["go"]
pkgdesc = "Platform for building proxies to bypass network restrictions"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://v2fly.org"
source = (
    f"https://github.com/v2fly/v2ray-core/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "2de8ac3429705f594ca1a75a2a0fca09820938c94e912370902f87bd72680693"
# check: needs network access
options = ["!check"]


def install(self):
    self.install_bin("build/main", name="v2ray")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "v2ray")
    self.install_file(
        "release/config/config.json",
        dest="usr/share/examples/v2ray",
        name="config.json",
    )
