pkgname = "netavark"
pkgver = "1.10.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "go-md2man", "protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5df03e3dc82e208dd49684e7b182ffe6c158ad9d9d06cba0c3d4820f471bfaa4"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/libexec/podman",
        0o755,
    )
