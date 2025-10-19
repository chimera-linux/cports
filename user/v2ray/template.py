pkgname = "v2ray"
pkgver = "5.41.0"
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
sha256 = "c67caa2d73f35a9562ecaeb5184733c943c9dafb47e8f1cfeacb892a9247e9b5"
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
