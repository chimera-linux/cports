pkgname = "netavark"
pkgver = "1.14.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protobuf-protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fd4a25db0abe73e2d0d7a9958f298ace134671edc64259cbc8ea3c2907f89dd8"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/lib/podman",
        0o755,
    )
