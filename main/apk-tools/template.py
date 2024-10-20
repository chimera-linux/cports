pkgname = "apk-tools"
pkgver = "3.0.0_pre10"
pkgrel = 2
_gitrev = "0e459970971579626ddf9f8f7b47a7ff16a03af4"
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
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "openssl-devel-static",
    "zlib-ng-compat-devel-static",
]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"https://gitlab.alpinelinux.org/alpine/apk-tools/-/archive/{_gitrev}.tar.gz"
sha256 = "e17f050d9dfc5108ba4eed9e651c2c064312309dcdc1a30c52ba47ec84cd429b"
compression = "deflate"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers", "musl-devel-static", "zstd-devel-static"]
    if self.stage > 1:
        depends = ["ca-certificates"]
else:
    configure_args += [
        "-Dhelp=disabled",
        "-Ddocs=disabled",
        "-Dzstd=false",
    ]


def post_extract(self):
    with open(self.cwd / "VERSION", "w") as f:
        f.write(f"{pkgver} ({_gitrev})")


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
        return

    self.install_bin("build-static/src/apk", name="apk.static")
    self.install_dir("etc/apk")
    self.ln_s("../../var/cache/apk", self.destdir / "etc/apk/cache")
    (self.destdir / "etc/apk/interactive").touch()


@subpackage("apk-tools-devel")
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
