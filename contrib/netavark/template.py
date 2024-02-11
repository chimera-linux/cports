pkgname = "netavark"
pkgver = "1.10.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fdc3010cb221f0fcef0302f57ef6f4d9168a61f9606238a3e1ed4d2e348257b7"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/libexec/podman",
        0o755,
    )
