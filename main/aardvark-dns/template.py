pkgname = "aardvark-dns"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Authoritative DNS server for A/AAAA container records"
license = "Apache-2.0"
url = "https://github.com/containers/aardvark-dns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "daf871488603e659b0501224cf0731ac317809b1d1701fc061cb4f6ae39a894f"


def install(self):
    from cbuild.util import cargo

    self.install_file(
        cargo.target_path(self, "aardvark-dns"),
        "usr/lib/podman",
        mode=0o755,
    )
