pkgname = "apk-tools"
pkgver = "3.0.0_pre2"
pkgrel = 1
_gitrev = "c8c9df1825760e558f44397500af2a2f4bca18d4"
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
sha256 = "5f01de0805649b6f77a88351a7e08c4b6b5b51e1bb1354f517dae6f158f5b217"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers", "musl-devel-static"]
    if self.stage > 1:
        depends = ["ca-certificates"]
else:
    configure_args += [
        "-Dhelp=disabled",
        "-Ddocs=disabled",
        "-Dstatic_apk=false",
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
