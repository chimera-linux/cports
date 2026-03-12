pkgname = "aardvark-dns"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "42556bf547c435a8f0ccb586b4f5000da3106a58c26f82e22d9db81ee5bd7eb2"


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/aardvark-dns",
        "usr/lib/podman",
        0o755,
    )
