pkgname = "apk-tools"
pkgver = "3.0.0_pre0"
pkgrel = 0
_gitrev = "d5ff6c96e41210f5a88ba48d85513751e36868f4"
build_style = "meson"
configure_args = ["-Dlua=disabled", "-Dstatic_apk=true", "-Dlua_version=5.4"]
hostmakedepends = ["pkgconf", "meson", "lua5.4", "lua5.4-zlib", "scdoc"]
makedepends = [
    "openssl-devel-static", "zlib-devel-static", "libunwind-devel-static",
    "libatomic-chimera-devel-static",
]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"https://gitlab.alpinelinux.org/alpine/{pkgname}/-/archive/{_gitrev}.tar.gz"
sha256 = "899234523be26c65c22c700f9a2976be22b2c06da62a15e34d09faf94ad164c3"
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers", "musl-devel-static"]
    if self.stage > 1:
        depends = ["ca-certificates"]
else:
    configure_args += [
        "-Dhelp=disabled", "-Ddocs=disabled", "-Dstatic_apk=false"
    ]

def init_configure(self):
    if self.stage > 0:
        return

    from cbuild.core import paths

    ldir = str(paths.bldroot() / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_ZLIB_LIBDIR"] = ldir
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = ldir
    self.env["PKG_CONFIG_LIBSSL_LIBDIR"] = ldir

@subpackage("apk-tools-devel")
def _devel(self):
    return self.default_devel()

@subpackage("apk-tools-static-bin", self.stage > 0)
def _staticbin(self):
    self.pkgdesc += " (static binary)"
    self.depends = []

    return ["usr/bin/apk.static"]
