pkgname = "netavark"
pkgver = "1.12.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "71e44922204da923b9f03b1306b9b0ba82673a201f3d96afc544f4ccdd4824d3"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/libexec/podman",
        0o755,
    )
