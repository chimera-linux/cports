pkgname = "bpftop"
pkgver = "0.5.2"
pkgrel = 4
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz>bpftop-asfkashdgkjhsbdgnskdjfgn.tar.gz"
sha256 = "d941314d8716f22d009a031de30edc92586cd434646bf2d2eb14c0a42e94bc95"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/bpftop")
