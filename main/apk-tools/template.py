pkgname = "apk-tools"
pkgver = "3.0.0_rc2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlua=disabled",
    "-Dlua_version=5.4",
]
hostmakedepends = [
    "lua5.4",
    "lua5.4-zlib",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["openssl3-devel", "zlib-ng-compat-devel"]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"https://gitlab.alpinelinux.org/alpine/apk-tools/-/archive/v{pkgver}/apk-tools-v{pkgver}.tar.gz"
sha256 = "c8bbcea845fc9d863f103987da68d8b0df6ae353f21266b3c54316bb702bc92a"
compression = "deflate"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += [
        "libatomic-chimera-devel-static",
        "libunwind-devel-static",
        "linux-headers",
        "musl-devel-static",
        "openssl3-devel-static",
        "zlib-ng-compat-devel-static",
        "zstd-devel-static",
    ]
    if self.stage > 1:
        depends = ["ca-certificates"]
else:
    configure_args += [
        "-Dhelp=disabled",
        "-Ddocs=disabled",
        "-Dzstd=false",
    ]


def init_configure(self):
    if self.stage > 0:
        return

    ldir = str(self.bldroot_path / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_ZLIB_LIBDIR"] = ldir
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = ldir
    self.env["PKG_CONFIG_LIBSSL_LIBDIR"] = ldir


def post_configure(self):
    if self.stage == 0:
        return

    from cbuild.util import meson

    meson.configure(
        self,
        "build-static",
        extra_args=[
            "-Dc_link_args=-static-pie",
            "-Ddefault_library=static",
            "-Dprefer_static=true",
            "-Ddocs=disabled",
            *configure_args,
        ],
    )


def post_build(self):
    if self.stage == 0:
        return

    self.do("ninja", f"-j{self.make_jobs}", "-C", "build-static", "src/apk")


def post_install(self):
    if self.stage == 0:
        # drop devel bits for stage 0, not used by anything and it lets
        # us bypass the fact that stage0 packages don't have pc: providers
        self.uninstall("usr/include")
        self.uninstall("usr/lib/libapk.a")
        self.uninstall("usr/lib/libapk.so")
        self.uninstall("usr/lib/pkgconfig")
        return

    self.install_bin("build-static/src/apk", name="apk.static")
    self.install_dir("etc/apk")
    self.ln_s("../../var/cache/apk", self.destdir / "etc/apk/cache")
    (self.destdir / "etc/apk/interactive").touch()


@subpackage("apk-tools-devel", self.stage > 0)
def _(self):
    return self.default_devel()


@subpackage("apk-tools-static-bin", self.stage > 0)
def _(self):
    self.subdesc = "static binary"

    return ["usr/bin/apk.static"]


@subpackage("apk-tools-cache", self.stage > 0)
def _(self):
    self.subdesc = "default cache"
    self.depends = [self.parent]
    self.install_if = [self.parent]
    self.provides = [self.with_pkgver("apk-tools-cache-link")]
    self.options = ["brokenlinks"]

    return ["etc/apk/cache"]


@subpackage("apk-tools-interactive", self.stage > 0)
def _(self):
    self.subdesc = "interactive"
    self.depends = [self.parent]
    self.install_if = [self.parent]

    return ["etc/apk/interactive"]
