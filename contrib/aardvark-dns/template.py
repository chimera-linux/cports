pkgname = "aardvark-dns"
pkgver = "1.10.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b3e77b3ff4eb40f010c78ca00762761e8c639c47e1cb67686d1eb7f522fbc81e"


def do_install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/libexec/podman",
        0o755,
    )
