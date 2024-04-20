pkgname = "apk-tools"
pkgver = "3.0.0_pre5"
pkgrel = 0
_gitrev = "ba6c31a5469ef74fb85119508e55de9631ffef41"
build_style = "meson"
configure_args = ["-Dlua=disabled", "-Dstatic_apk=true", "-Dlua_version=5.4"]
hostmakedepends = ["pkgconf", "meson", "lua5.4", "lua5.4-zlib", "scdoc"]
makedepends = [
    "openssl-devel-static",
    "zlib-devel-static",
    "libunwind-devel-static",
    "libatomic-chimera-devel-static",
]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"https://gitlab.alpinelinux.org/alpine/{pkgname}/-/archive/{_gitrev}.tar.gz"
sha256 = "d9deac8159fb35eb7d03919c1bec1af46ae75b86e11e9646d3f57ea6eef5e226"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers", "musl-devel-static", "zstd-devel-static"]
    if self.stage > 1:
        depends = ["ca-certificates"]
else:
    configure_args += [
        "-Dhelp=disabled",
        "-Ddocs=disabled",
        "-Dstatic_apk=false",
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


def post_install(self):
    if self.stage == 0:
        return
    self.install_dir("etc/apk")
    self.ln_s("../../var/cache/apk", self.destdir / "etc/apk/cache")
    (self.destdir / "etc/apk/interactive").touch()


@subpackage("apk-tools-devel")
def _devel(self):
    return self.default_devel()


@subpackage("apk-tools-static-bin", self.stage > 0)
def _staticbin(self):
    self.pkgdesc = f"{pkgdesc} (static binary)"
    self.depends = []

    return ["usr/bin/apk.static"]


@subpackage("apk-tools-cache", self.stage > 0)
def _cache(self):
    self.pkgdesc = f"{pkgdesc} (default cache)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provides = [f"apk-tools-cache-link={pkgver}-r{pkgrel}"]
    self.options = ["brokenlinks"]

    return ["etc/apk/cache"]


@subpackage("apk-tools-interactive", self.stage > 0)
def _interactive(self):
    self.pkgdesc = f"{pkgdesc} (interactive)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["etc/apk/interactive"]
