pkgname = "v2ray"
pkgver = "5.29.1"
pkgrel = 5
build_style = "go"
make_build_args = ["./main"]
hostmakedepends = ["go"]
pkgdesc = "Platform for building proxies to bypass network restrictions"
license = "MIT"
url = "https://v2fly.org"
source = (
    f"https://github.com/v2fly/v2ray-core/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "929706448db0aadd812d2fd2978bc4bcbb709e05c401e69919b21c99122806e7"
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
