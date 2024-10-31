pkgname = "aardvark-dns"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "192d49837b8f156cbe4d2839c830988ec90a8f85a3e75e475436115f4fd08b0a"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/lib/podman",
        0o755,
    )
