pkgname = "v2ray"
pkgver = "5.29.0"
pkgrel = 1
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
sha256 = "74884fecb10ae7e556b917388928ca942bd15e0a730b658b32a1af7e20e3a7ab"
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
