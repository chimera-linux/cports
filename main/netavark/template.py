pkgname = "netavark"
pkgver = "1.12.2"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d1e5a7e65b825724fd084b0162084d9b61db8cda1dad26de8a07be1bd6891dbc"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/lib/podman",
        0o755,
    )
