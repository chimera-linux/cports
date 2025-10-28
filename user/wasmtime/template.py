pkgname = "wasmtime"
pkgver = "37.0.2"
pkgrel = 0
build_style = "cargo"
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
license = "Apache-2.0"
url = "https://wasmtime.dev"
source = f"https://github.com/bytecodealliance/wasmtime/releases/download/v{pkgver}/wasmtime-v{pkgver}-src.tar.gz"
sha256 = "df4b9b77cc607728b20fac730531c8dbe2039989f8e2654dce901228c51d65b1"


def post_extract(self):
    # comes with prevendor; we redo it
    self.rm(".cargo/config.toml")


def post_configure(self):
    from cbuild.util import cmake

    cmake.configure(
        self,
        build_dir="build-capi",
        cmake_dir="crates/c-api",
        extra_args=[f"-DWASMTIME_TARGET={self.profile().triplet}"],
    )


def post_build(self):
    from cbuild.util import cargo, cmake

    renv = cargo.get_environment(self)
    self.env.update(renv)

    cmake.build(self, "build-capi")


def install(self):
    from cbuild.util import cmake

    cmake.install(self, "build-capi")
    self.install_bin(f"target/{self.profile().triplet}/release/wasmtime")


@subpackage("wasmtime-libs")
def _(self):
    return ["usr/lib/libwasmtime.so"]


@subpackage("wasmtime-devel")
def _(self):
    self.depends = [self.with_pkgver("wasmtime-libs")]
    return self.default_devel()
