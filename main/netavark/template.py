pkgname = "netavark"
pkgver = "1.13.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protobuf-protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b3698021677fb3b0fd1dc5f669fd62b49a7f4cf26bb70f977663f6d1a5046a31"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/lib/podman",
        0o755,
    )
