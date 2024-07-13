pkgname = "mozjs128"
pkgver = "128.0"
pkgrel = 1
make_cmd = "gmake"
hostmakedepends = [
    "cargo",
    "cbindgen",
    "gawk",
    "gm4",
    "gmake",
    "perl",
    "pkgconf",
    "python",
]
makedepends = [
    "icu-devel",
    "libedit-devel",
    "libffi-devel",
    "linux-headers",
    "nspr-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Mozilla JavaScript interpreter and library, version 128.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.mozilla.org/firefox"
source = f"$(MOZILLA_SITE)/firefox/releases/{pkgver}esr/source/firefox-{pkgver}esr.source.tar.xz"
sha256 = "c5ba7dcfbaf8600667766891eca9069392b659e18255d91d742ac69f224c697c"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=1048576"]}
env = {
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "RUST_TARGET": self.profile().triplet,
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


def post_patch(self):
    self.mv("js/src/gc/SweepingAPI.h", "js/public/SweepingAPI.h")


def init_configure(self):
    from cbuild.util import cargo

    self.env["MOZBUILD_STATE_PATH"] = str(self.chroot_srcdir / ".mozbuild")
    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["MOZ_OBJDIR"] = f"{self.chroot_cwd / 'objdir'}"
    self.env["RUST_TARGET"] = self.profile().triplet
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))


def do_configure(self):
    self.rm("objdir", recursive=True, force=True)
    self.mkdir("objdir")

    extra_opts = []

    if self.has_lto():
        extra_opts += ["--enable-lto=cross"]

    self.do(
        self.chroot_cwd / "mach",
        "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--disable-hardening",
        "--disable-install-strip",
        "--disable-strip",
        "--enable-application=js",
        "--enable-linker=lld",
        "--enable-optimize",
        "--enable-release",
        # system libs
        "--with-system-icu",
        "--with-system-nspr",
        "--with-system-zlib",
        # features
        "--enable-ctypes",
        "--enable-readline",
        "--enable-shared-js",
        "--enable-system-ffi",
        "--enable-tests",
        "--with-intl-api",
        # disabled features
        "--disable-debug",
        "--disable-jemalloc",
        # conditional opts
        *extra_opts,
        wrksrc="objdir",
    )


def do_build(self):
    self.do(
        self.chroot_cwd / "mach",
        "build",
        "--priority",
        "normal",
        wrksrc="objdir",
    )


def do_install(self):
    self.do(
        "gmake", "-C", "objdir", "install", f"DESTDIR={self.chroot_destdir}"
    )


def post_install(self):
    self.uninstall("usr/lib/libjs_static.ajs")
    # it has correct soname but not the right file name
    self.rename("usr/lib/libmozjs-128.so", "libmozjs-128.so.0")
    self.install_link("usr/lib/libmozjs-128.so", "libmozjs-128.so.0")


def do_check(self):
    self.do("objdir/dist/bin/jsapi-tests")


@subpackage("mozjs128-devel")
def _devel(self):
    # include the interactive interpreter
    return self.default_devel(extra=["usr/bin"])
