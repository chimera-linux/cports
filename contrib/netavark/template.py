pkgname = "netavark"
pkgver = "1.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8870d36f87cfef802a6af06f64069397b7e69b0de0e6b0ba79c06d785c2e9bb7"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/libexec/podman",
        0o755,
    )
