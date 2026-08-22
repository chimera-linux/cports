pkgname = "netavark"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protobuf-protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "96677048168ddd1abe313e4c2e17f1cace72b60ee1bac8ca12a4bd7dfcadfbbb"


def post_build(self):
    self.do("make", "docs", wrksrc="docs")


def install(self):
    self.do(
        "make",
        "install",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
        wrksrc="docs",
    )
    self.install_file(
        f"target/{self.profile().triplet}/release/netavark",
        "usr/lib/podman",
        0o755,
    )
