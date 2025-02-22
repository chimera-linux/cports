pkgname = "aardvark-dns"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d46f170e0439fc97e15bb31d63b7464192f74809b0d54064383e6a0b592d8cfd"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/lib/podman",
        0o755,
    )
