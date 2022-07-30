pkgname = "bsdutils"
_commit="7ad373fe2b60f33cd2a49f23746bb0ac53cbe743"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel", "liblzma-devel",
    "zlib-devel", "libbz2-devel",
    "musl-bsd-headers" # temporary
]
depends = ["base-files"]
pkgdesc = "FreeBSD userland utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils"
source = f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"
sha256 = "689045a08ac0bb141a23bd42e23464d6e480772da1c76597aed0b5853365a197"
# no test suite
options = ["bootstrap", "!check"]

if self.stage > 0:
    makedepends += ["libxo-devel"]
else:
    makedepends += ["libxo-tiny-devel"]

def init_configure(self):
    if self.stage > 0:
        return

    from cbuild.core import paths

    spath = str(paths.bldroot() / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = spath
    self.configure_args += [
        f"-Dfts_path={spath}", f"-Drpmatch_path={spath}"
    ]

def post_install(self):
    # less
    self.rm(self.destdir / "usr/bin/zless")
    self.rm(self.destdir / "usr/share/man/man1/zless.1")
    # base shell
    self.install_shell("/usr/bin/sh")

if self.stage > 0:
    makedepends += ["linux-headers"]
