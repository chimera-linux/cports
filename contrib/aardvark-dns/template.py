pkgname = "aardvark-dns"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3e95b363f89a945ee6e63f51051f9eb982bdc469bf8e727b5d7adca676789750"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/libexec/podman",
        0o755,
    )
