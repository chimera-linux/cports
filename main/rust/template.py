pkgname = "rust"
pkgver = "1.84.0"
pkgrel = 0
hostmakedepends = [
    "cargo-bootstrap",
    "cmake",
    "curl",
    "libffi-devel",
    "libxml2-devel",
    "llvm-devel",
    "llvm-tools",
    "ncurses-devel",
    "pkgconf",
    "python",
    "wasi-libc",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
makedepends = [
    "libffi-devel",
    "libxml2-devel",
    "llvm-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [self.with_pkgver("rust-std"), "clang", "musl-devel"]
pkgdesc = "Rust programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://static.rust-lang.org/dist/rustc-{pkgver}-src.tar.xz"
sha256 = "bc2c1639f26814c7b17a323992f1e08c3b01fe88cdff9a27d951987d886e00b3"
tool_flags = {
    "RUSTFLAGS": [
        # make the std debugging symbols point to rust-src
        "--remap-path-prefix=library=/usr/lib/rustlib/src/rust/library",
    ]
}
# global environment
env = {
    "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    "OPENSSL_NO_VENDOR": "1",
    "RUST_BACKTRACE": "1",
}
# disable check at least for now
# lto always breaks across major llvm vers because of consumer/reader mismatch,
# because it builds some not useful C stuff that is part of rust
# we manually enable it below for librustc_driver itself
options = ["!check", "!lto"]

if self.profile().cross:
    hostmakedepends += ["rust"]
    env["PKG_CONFIG_ALLOW_CROSS"] = "1"
elif self.current_target == "custom:bootstrap":
    hostmakedepends += ["rust"]
else:
    hostmakedepends += ["rust-bootstrap"]

_rlib_dir = f"usr/lib/rustlib/{self.profile().triplet}"

if self.current_target == "custom:bootstrap":
    # bootstrap binaries are statically linked to llvm to
    # avoid cyclic pains when updating llvm to a newer version
    #
    # since there is just one static switch, we need static llvm
    # for both host and target rustc builds
    hostmakedepends += ["llvm-devel-static"]
    makedepends += ["llvm-devel-static"]
    # avoid debug cflags and so on for vendor libs
    options += ["!debug"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "compiler_builtins-0.1.138")
    # nice fucking meme
    cargo.clear_vendor_checksums(self, "libc-0.2.94")
    cargo.clear_vendor_checksums(self, "libc-0.2.97")
    cargo.clear_vendor_checksums(self, "libc-0.2.107")
    cargo.clear_vendor_checksums(self, "libc-0.2.112")
    cargo.clear_vendor_checksums(self, "libc-0.2.119")
    cargo.clear_vendor_checksums(self, "libc-0.2.121")
    cargo.clear_vendor_checksums(self, "libc-0.2.124")
    cargo.clear_vendor_checksums(self, "libc-0.2.150")
    cargo.clear_vendor_checksums(self, "libc-0.2.155")
    cargo.clear_vendor_checksums(self, "libc-0.2.158")
    cargo.clear_vendor_checksums(self, "libc-0.2.159")
    cargo.clear_vendor_checksums(self, "libc-0.2.161")
    cargo.clear_vendor_checksums(self, "libc-0.2.162")
    cargo.clear_vendor_checksums(self, "libc-0.2.164")


def configure(self):
    _tools = ["rustdoc"]
    if self.current_target == "custom:bootstrap":
        _llvm_shared = "false"
        _use_docs = "false"
        _use_rpath = "true"
        _extended = "false"
        _profiler = "false"
    else:
        _llvm_shared = "true"
        # fails to build for wasm targets
        _use_docs = "false"
        _use_rpath = "false"
        _extended = "true"
        _profiler = "true"
        # while we'd love to build cargo and rust in one build, this is
        # unfortunately not possible as rustbuild is junk and breaks rather
        # hard when trying that
        _tools += ["clippy", "src", "rustfmt"]
        # for rust-analyzer, only builds on these archs
        match self.profile().arch:
            case "aarch64" | "ppc64" | "ppc64le" | "x86_64":
                _tools += ["rust-analyzer-proc-macro-srv"]

    if self.profile().cross:
        _local_rebuild = "true"
    else:
        _local_rebuild = "false"

    if self.build_dbg:
        _debug = "2"
        _debug_rustc = "1"
    else:
        _debug = "0"
        _debug_rustc = "0"

    if self.current_target != "custom:bootstrap":
        _comp = "gz"
        _comp_prof = "fast"
        # thin-local is the default value
        _lto = "thin" if self.can_lto() else "thin-local"
    else:
        _comp = "xz"
        _comp_prof = "best"
        _lto = "thin-local"

    tgt_profile = self.profile()
    _tgt_spec = [f"'{tgt_profile.triplet}'"]
    if self.current_target != "custom:bootstrap":
        _tgt_spec += [
            "'wasm32-unknown-unknown'",
            "'wasm32-wasip1'",
            "'wasm32-wasip1-threads'",
            "'wasm32-wasip2'",
        ]

    # this is a hack that violates packaging guidelines, but it's only
    # for bootstrapping anyway, and conditionally patching it is worse
    #
    # we need to ensure to link to these otherwise we get undefined refs
    if _llvm_shared == "false":
        with open(self.cwd / "compiler/rustc_llvm/src/lib.rs", "a") as f:
            f.write(
                """
#[link(name = "ffi")]
extern {}
#[link(name = "z")]
extern {}
#[link(name = "zstd")]
extern {}
#[link(name = "ncursesw")]
extern {}
"""
            )

    with self.profile("host") as hpf:
        host_profile = hpf

    with open(self.cwd / "config.toml", "w") as cfg:
        cfg.write(
            f"""
change-id = 133207

[llvm]
ninja = false
link-shared = {_llvm_shared}
static-libstdcpp = false
use-libcxx = true

[build]

build = '{host_profile.triplet}'
host = ['{tgt_profile.triplet}']
target = [{",".join(_tgt_spec)}]

cargo = '/usr/bin/cargo'
rustc = '/usr/bin/rustc'

docs = {_use_docs}

python = 'python'

locked-deps = true
vendor = true

extended = {_extended}

tools = [{", ".join(map(lambda v: '"' + v + '"', _tools))}]

profiler = {_profiler}

local-rebuild = {_local_rebuild}

[install]

prefix = '/usr'

[rust]

optimize = true
debug = false
backtrace-on-ice = true
codegen-units = 1
codegen-units-std = 1

debuginfo-level = {_debug_rustc}
debuginfo-level-std = {_debug}

lto = '{_lto}'

incremental = false
parallel-compiler = false

channel = 'stable'
description = 'Chimera Linux'

rpath = {_use_rpath}

frame-pointers = true

deny-warnings = false

llvm-libunwind = 'system'

[dist]

vendor = false
src-tarball = true
compression-formats = ['{_comp}']
compression-profile = '{_comp_prof}'

[target.{host_profile.triplet}]

cc = '{self.get_tool("CC", target="host")}'
cxx = '{self.get_tool("CXX", target="host")}'
ar = '/usr/bin/llvm-ar'
ranlib = '/usr/bin/llvm-ranlib'
linker = '{self.get_tool("CC", target="host")}'
llvm-config = '/usr/bin/llvm-config'
crt-static = false

"""
        )
        # cross-target definition if used
        if tgt_profile.cross:
            cfg.write(
                f"""
[target.{tgt_profile.triplet}]

cc = '{self.get_tool("CC")}'
cxx = '{self.get_tool("CXX")}'
ar = '/usr/bin/llvm-ar'
ranlib = '/usr/bin/llvm-ranlib'
linker = '{self.get_tool("CC")}'
llvm-config = '/usr/bin/llvm-config'
crt-static = false
"""
            )
        # wasm targets for non-bootstrap
        if self.current_target != "custom:bootstrap":
            cfg.write(
                """
[target.wasm32-unknown-unknown]

sanitizers = false
profiler = false

[target.wasm32-wasip1]

sanitizers = false
profiler = false
wasi-root = '/usr/wasm32-unknown-wasi'

[target.wasm32-wasip1-threads]

sanitizers = false
profiler = false
wasi-root = '/usr/wasm32-unknown-wasi'

[target.wasm32-wasip2]

sanitizers = false
profiler = false
wasi-root = '/usr/wasm32-unknown-wasi'
"""
            )


def build(self):
    benv = {}
    benv["CARGO_HOME"] = str(self.chroot_cwd / ".cargo")
    # we don't want the default cross sysroot here
    with self.profile("target:native"):
        benv["RUSTFLAGS"] = self.get_rustflags(shell=True)
    # ensure correct flags are used for host C/C++ code
    with self.profile("host") as pf:
        benv["CFLAGS_" + pf.triplet] = self.get_cflags(shell=True)
        benv["CXXFLAGS_" + pf.triplet] = self.get_cxxflags(shell=True)
    # ensure correct flags are used for target C/C++ code
    with self.profile("target") as pf:
        benv["CFLAGS_" + pf.triplet] = self.get_cflags(shell=True)
        benv["CXXFLAGS_" + pf.triplet] = self.get_cxxflags(shell=True)
    # and hope it does not fail
    #
    # we also need to ensure PKG_CONFIG is unset because otherwise the
    # target pkg-config will leak into some host build stuff and will
    # affect the sysroot used (which will result in link failures)
    #
    self.do(
        "env",
        "-u",
        "PKG_CONFIG",
        # prevent global flags from being applied to wasi/other targets
        "-u",
        "CFLAGS",
        "-u",
        "CXXFLAGS",
        "--",
        "python",
        "x.py",
        "dist",
        "--jobs",
        str(self.make_jobs),
        env=benv,
    )


def check(self):
    self.do(
        "python",
        "x.py",
        "test",
        f"-j{self.make_jobs}",
        "--no-fail-fast",
        "src/test/codegen",
        "src/test/codegen-units",
        "src/test/incremental",
        "src/test/mir-opt",
        "src/test/pretty",
        "src/test/run-make",
        "src/test/run-make-fulldeps",
        "src/test/ui",
        "src/test/ui-fulldeps",
    )


def _untar(self, name, has_triple=True):
    trip = self.profile().triplet

    fname = f"{name}-{pkgver}"
    if isinstance(has_triple, str):
        fname += f"-{has_triple}"
    elif has_triple:
        fname += f"-{trip}"
    fname += ".tar.gz"

    self.do(
        "tar",
        "xf",
        self.chroot_cwd / f"build/dist/{fname}",
        "-C",
        self.chroot_destdir / "usr",
        "--strip-components=2",
        "--exclude=manifest.in",
        "--no-same-owner",
    )


@custom_target("bootstrap", "build")
def _(self):
    # already done
    pass


def install(self):
    self.install_license("COPYRIGHT")
    self.install_license("LICENSE-MIT")

    # used if we decide to ship src
    self.install_dir("usr/src")

    # extract the archives
    for f in [
        "rustc",
        "rust-std",
        "rustc-dev",
        "clippy",
        "rustfmt",
    ]:
        self.log(f"unpacking {f}...")
        _untar(self, f)
    # wasm shit
    self.log("unpacking wasm targets...")
    _untar(self, "rust-std", "wasm32-unknown-unknown")
    _untar(self, "rust-std", "wasm32-wasip1")
    _untar(self, "rust-std", "wasm32-wasip1-threads")
    _untar(self, "rust-std", "wasm32-wasip2")

    self.log("unpacking rust-src...")
    _untar(self, "rust-src", False)

    # remove rust copies of llvm tools
    self.log("cleaning up tools...")
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()

    # usr/lib stuff should be symlinks into rustlib
    self.log("relinking rustlibs...")
    for f in (self.destdir / "usr/lib").glob("*.so"):
        rlibf = self.destdir / _rlib_dir / "lib" / f.name
        rlibf.unlink()
        self.mv(f, rlibf)
        f.symlink_to(rlibf.relative_to(f.parent))


@subpackage("rust-wasm")
def _(self):
    self.pkgdesc = "WebAssembly targets"
    self.depends = [self.parent, "lld", "wasi-libc"]
    self.options = ["!strip"]

    return ["usr/lib/rustlib/wasm32-*"]


@subpackage("rust-clippy")
def _(self):
    self.pkgdesc = "Lints to catch common mistakes"
    self.depends = [self.parent]

    return [
        "usr/bin/cargo-clippy",
        "usr/bin/clippy-driver",
    ]


@subpackage("rustfmt")
def _(self):
    self.pkgdesc = "Rust code formatter"
    self.depends = [self.parent]

    return [
        "usr/bin/rustfmt",
        "usr/bin/cargo-fmt",
    ]


@subpackage("rust-std")
def _(self):
    self.subdesc = "static rlibs"
    self.options = ["!strip"]

    return [
        f"{_rlib_dir}/lib/*.rlib",
        f"{_rlib_dir}/lib/*.rmeta",
    ]


@subpackage("rust-src")
def _(self):
    self.subdesc = "source"

    return [
        "usr/lib/rustlib/rustc-src",
        "usr/lib/rustlib/src",
    ]
