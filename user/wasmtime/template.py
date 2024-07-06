pkgname = "wasmtime"
pkgver = "22.0.0"
pkgrel = 1
# no implementation for other architectures
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
# make_build_env = {"CARGO_PROFILE_RELEASE_DEBUG": "2"}
make_check_args = [
    "--",
    # who knows
    "--skip=custom_limiter_detect_os_oom_failure",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "ninja",
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
sha256 = "9fe87339e61b57338473b857d8ddebda958d8bb7534ddddf463b1f7648faf1e5"
# wast tests take like an hour
options = ["!check"]


def post_extract(self):
    # comes with prevendor; we redo it
    self.rm(".cargo/config.toml")


def post_configure(self):
    from cbuild.util import cmake

    cmake.configure(
        self, build_dir="build-capi-headers", cmake_dir="crates/c-api"
    )


def post_build(self):
    self.cargo.build(args=["-p", "wasmtime-c-api"])


def do_install(self):
    from cbuild.util import cmake

    cmake.install(self, "build-capi-headers")
    self.install_bin(f"target/{self.profile().triplet}/release/wasmtime")
    self.install_lib(f"target/{self.profile().triplet}/release/libwasmtime.so")
    self.install_lib(f"target/{self.profile().triplet}/release/libwasmtime.a")


@subpackage("wasmtime-libs")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (libraries)"
    return ["usr/lib/libwasmtime.so"]


@subpackage("wasmtime-devel")
def _devel(self):
    self.depends = [f"wasmtime-libs={pkgver}-r{pkgrel}"]
    return self.default_devel()
