pkgname = "bpftop"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libbpf-devel",
    "rust-std",
]
pkgdesc = "TUI view for running BPF programs"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/Netflix/bpftop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4033c77e99afd9297466c619f9049fddd9fcf26fda25fc9cc80c4a0c0ae7d40a"


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bpftop")
