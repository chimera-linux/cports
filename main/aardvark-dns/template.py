pkgname = "aardvark-dns"
pkgver = "1.13.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8c21dbdb6831d61d52dde6ebc61c851cfc96ea674cf468530b44de6ee9e6f49e"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/lib/podman",
        0o755,
    )
