pkgname = "wasmtime"
pkgver = "21.0.1"
pkgrel = 0
# no implementation for other architectures
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
make_check_args = [
    "--",
    # who knows
    "--skip=custom_limiter_detect_os_oom_failure",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "rust-std",
    "rust-wasm",
    "zstd-devel",
]
pkgdesc = "Runtime for webassembly"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://wasmtime.dev"
source = f"https://github.com/bytecodealliance/wasmtime/releases/download/v{pkgver}/wasmtime-v{pkgver}-src.tar.gz"
sha256 = "1e1c85c3c3b69812c7674c14a75ac6d3b917ab121c501d6a348acc2fcdd6a739"


def post_extract(self):
    # comes with prevendor; we redo it
    self.rm(".cargo/config.toml")


def post_build(self):
    self.cargo.build(args=["-p", "wasmtime-c-api"])


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/wasmtime")
    self.install_lib(f"target/{self.profile().triplet}/release/libwasmtime.so")
    self.install_lib(f"target/{self.profile().triplet}/release/libwasmtime.a")
    self.install_files("crates/c-api/include", "usr")


@subpackage("wasmtime-libs")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (libraries)"
    return ["usr/lib/libwasmtime.so"]


@subpackage("wasmtime-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development files)"
    self.depends = [f"wasmtime-libs={pkgver}-r{pkgrel}"]
    return ["usr/include", "usr/lib/libwasmtime.a"]
