pkgname = "mozjs115"
pkgver = "115.6.0"
pkgrel = 1
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "python",
    "python-setuptools",
    "python-six",
    "perl",
    "gm4",
    "gawk",
    "rust",
    "cargo",
]
makedepends = [
    "icu-devel",
    "libffi-devel",
    "nspr-devel",
    "python-devel",
    "zlib-devel",
    "libedit-devel",
    "rust-std",
    "linux-headers",
]
pkgdesc = "Mozilla JavaScript interpreter and library (115.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.mozilla.org/firefox"
source = f"$(MOZILLA_SITE)/firefox/releases/{pkgver}esr/source/firefox-{pkgver}esr.source.tar.xz"
sha256 = "66d7e6e5129ac8e6fe83e24227dc7bb8dc42650bc53b21838e614de80d22bc66"
debug_level = 1  # make the debug size not explode
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=1048576"]}
env = {
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZBUILD_STATE_PATH": f"/builddir/{pkgname}-{pkgver}/.mozbuild",
    "RUST_TARGET": self.profile().triplet,
    "RUSTFLAGS": "",  # our -Clink-arg breaks this build
    "PYTHON": "/usr/bin/python",
    "SHELL": "/usr/bin/sh",
    "MAKE": "gmake",
    "AWK": "gawk",
    "M4": "gm4",
    # firefox checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME int (fails basic/hypot-approx.js)
hardening = ["!int"]
# dependencies are not crossable for now and it's probably tricky
options = ["!cross"]


def init_configure(self):
    from cbuild.util import cargo

    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["MOZ_OBJDIR"] = f"{self.chroot_cwd / 'objdir'}"
    self.env["RUST_TARGET"] = self.profile().triplet
    self.env["RUSTFLAGS"] = ""
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))


def do_configure(self):
    self.rm("objdir", recursive=True, force=True)
    self.mkdir("objdir")

    extra_opts = []

    match self.profile().arch:
        case "x86_64" | "aarch64":
            extra_opts += ["--disable-elf-hack", "--enable-rust-simd"]

    if self.has_lto():
        extra_opts += ["--enable-lto=cross"]

    self.do(
        self.chroot_cwd / "mach",
        "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--enable-application=js",
        "--enable-linker=lld",
        "--enable-release",
        "--enable-hardening",
        "--enable-optimize",
        "--disable-install-strip",
        "--disable-strip",
        # system libs
        "--with-system-zlib",
        "--with-system-nspr",
        "--with-system-icu",
        # features
        "--enable-tests",
        "--enable-ctypes",
        "--enable-readline",
        "--enable-shared-js",
        "--enable-system-ffi",
        "--with-intl-api",
        # disabled features
        "--disable-jemalloc",
        "--disable-debug",
        # conditional opts
        *extra_opts,
        wrksrc="objdir",
    )


def do_build(self):
    self.do(self.chroot_cwd / "mach", "build", wrksrc="objdir")


def do_install(self):
    self.do(
        "gmake", "-C", "objdir", "install", f"DESTDIR={self.chroot_destdir}"
    )


def post_install(self):
    self.rm(self.destdir / "usr/lib/libjs_static.ajs")
    # it has correct soname but not the right file name
    self.mv(
        self.destdir / "usr/lib/libmozjs-115.so",
        self.destdir / "usr/lib/libmozjs-115.so.0",
    )
    self.install_link("libmozjs-115.so.0", "usr/lib/libmozjs-115.so")


def do_check(self):
    self.do("objdir/dist/bin/jsapi-tests", "basic")


@subpackage("mozjs115-devel")
def _devel(self):
    # include the interactive interpreter
    return self.default_devel(extra=["usr/bin"])
