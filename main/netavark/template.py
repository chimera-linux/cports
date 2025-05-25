pkgname = "netavark"
pkgver = "1.15.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "go-md2man", "protobuf-protoc"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "Container network stack"
license = "Apache-2.0"
url = "https://github.com/containers/netavark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "efda776e538ce33050b1f6ce58c5070efeb45653d48fe4d17a47524c8fc17cf1"


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
