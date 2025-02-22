pkgname = "netavark"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protobuf-protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d2ded5412e5037e84f79a28c774378c864aa6f6e43023dd88891c70cfaf963ef"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/lib/podman",
        0o755,
    )
