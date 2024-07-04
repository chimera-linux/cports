pkgname = "chimerautils"
pkgver = "14.0.7"
pkgrel = 2
build_style = "meson"
configure_args = []
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel",
    "ncurses-devel",
    "libedit-devel",
    "openssl-devel",
    "musl-fts-devel",
    "musl-rpmatch-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "bzip2-devel",
    "libxo-devel",
    "musl-bsd-headers",
]
depends = ["base-files"]
pkgdesc = "Chimera Linux userland"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimerautils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e6af4876242128036faa51ae129c3eb2e8042a684e4e86339ab3a747cbcf0317"
hardening = ["vis", "cfi"]
# no test suite
options = ["bootstrap", "!check"]

if self.stage > 0:
    makedepends += ["linux-headers", "zstd-devel"]
    configure_args += ["-Dtiny=enabled"]
    # don't bother in stage 0
    depends += ["sd-tools"]
else:
    makedepends += ["libxo-devel-static"]
    configure_args += ["-Dzstd=disabled"]


def init_configure(self):
    if self.stage > 0:
        return

    spath = str(self.bldroot_path / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = spath
    self.env["PKG_CONFIG_LIBEDIT_LIBDIR"] = spath
    self.configure_args += [f"-Dfts_path={spath}", f"-Drpmatch_path={spath}"]


def post_install(self):
    # license
    self.install_license("LICENSE")
    # less
    self.uninstall("usr/bin/zless")
    self.uninstall("usr/share/man/man1/zless.1")
    # base shell
    self.install_shell("/usr/bin/sh")
    # tiny tools
    tdest = "usr/libexec/chimerautils-tiny"
    self.install_dir(tdest)
    for f in (self.destdir / "usr/bin").glob("*.tiny"):
        self.mv(f, self.destdir / tdest / f.stem)


@subpackage("chimerautils-extra")
def _full(self):
    self.pkgdesc = f"{pkgdesc} (additional tools)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "etc/locate.rc",
        "usr/bin/calendar",
        "usr/bin/cal",
        "usr/bin/compress",
        "usr/bin/cu",
        "usr/bin/ex",
        "usr/bin/fetch",
        "usr/bin/gencat",
        "usr/bin/locate",
        "usr/bin/m4",
        "usr/bin/nc",
        "usr/bin/ncal",
        "usr/bin/nex",
        "usr/bin/nvi",
        "usr/bin/nview",
        "usr/bin/patch",
        "usr/bin/telnet",
        "usr/bin/uncompress",
        "usr/bin/vi",
        "usr/bin/view",
        "usr/libexec/locate.*",
        "usr/share/man/man1/calendar.1",
        "usr/share/man/man1/cal.1",
        "usr/share/man/man1/compress.1",
        "usr/share/man/man1/cu.1",
        "usr/share/man/man1/ex.1",
        "usr/share/man/man1/fetch.1",
        "usr/share/man/man1/gencat.1",
        "usr/share/man/man1/locate.1",
        "usr/share/man/man1/m4.1",
        "usr/share/man/man1/nc.1",
        "usr/share/man/man1/ncal.1",
        "usr/share/man/man1/nex.1",
        "usr/share/man/man1/nvi.1",
        "usr/share/man/man1/nview.1",
        "usr/share/man/man1/patch.1",
        "usr/share/man/man1/telnet.1",
        "usr/share/man/man1/uncompress.1",
        "usr/share/man/man1/vi.1",
        "usr/share/man/man1/view.1",
        "usr/share/man/man8/locate.updatedb.8",
        "usr/share/man/man8/updatedb.8",
        "usr/share/vi",
    ]
