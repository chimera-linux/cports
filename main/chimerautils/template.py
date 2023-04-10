pkgname = "chimerautils"
pkgver = "13.2.2"
pkgrel = 0
build_style = "meson"
_commit = "e9bc60ba87f05df1113cf9e06c7975c04c892826"
configure_args = []
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel", "liblzma-devel",
    "zlib-devel", "libbz2-devel", "linux-headers",
    "libxo-devel", "musl-bsd-headers"
]
depends = ["base-files", "iana-etc"]
pkgdesc = "Chimera Linux userland"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimerautils"
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "df4173753dd398ffc1bb9b84d90d7a53421edfcf3d323dbdf108c441d9bcee82"
hardening = ["vis", "cfi"]
# no test suite
options = ["bootstrap", "!check"]

if self.stage > 0:
    makedepends += ["linux-headers"]
    configure_args += ["-Dtiny=enabled"]

def init_configure(self):
    if self.stage > 0:
        return

    from cbuild.core import paths

    spath = str(paths.bldroot() / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = spath
    self.env["PKG_CONFIG_LIBEDIT_LIBDIR"] = spath
    self.configure_args += [
        f"-Dfts_path={spath}", f"-Drpmatch_path={spath}"
    ]

def post_install(self):
    # less
    self.rm(self.destdir / "usr/bin/zless")
    self.rm(self.destdir / "usr/share/man/man1/zless.1")
    # base shell
    self.install_shell("/usr/bin/sh")
    # tiny tools
    tdest = "usr/libexec/chimerautils-tiny"
    self.install_dir(tdest)
    for f in (self.destdir / "usr/bin").glob("*.tiny"):
        self.mv(f, self.destdir / tdest / f.stem)
