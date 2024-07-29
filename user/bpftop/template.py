pkgname = "bpftop"
pkgver = "0.5.2"
pkgrel = 3
build_style = "cargo"
prepare_after_patch = True
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
sha256 = "d8e1faa10ad8e60a92e8ae93f65037dec976bcd1c40a4a33d3f176bf41390393"


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bpftop")
