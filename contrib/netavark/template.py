pkgname = "netavark"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9ec50b715ded0a0699134c001656fdd1411e3fb5325d347695c6cb8cc5fcf572"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/libexec/podman",
        0o755,
    )
