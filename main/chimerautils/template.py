pkgname = "chimerautils"
pkgver = "14.1.1"
pkgrel = 1
build_style = "meson"
configure_args = []
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel",
    "bzip2-devel",
    "libedit-devel",
    "libxo-devel",
    "musl-bsd-headers",
    "musl-fts-devel",
    "musl-rpmatch-devel",
    "ncurses-devel",
    "openssl-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = ["base-files"]
pkgdesc = "Chimera Linux userland"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimerautils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e92f590216c3a43d6f6ae7ae63f73ffd9147068e33a76e995d644d721434e7e2"
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
def _(self):
    self.subdesc = "additional tools"
    self.depends = [self.parent]

    return [
        "cmd:calendar",
        "cmd:cal",
        "cmd:compress",
        "cmd:cu",
        "cmd:ee",
        "cmd:ex",
        "cmd:fetch",
        "cmd:gencat",
        "cmd:locate*",
        "cmd:m4",
        "cmd:nc",
        "cmd:ncal",
        "cmd:nex",
        "cmd:nvi",
        "cmd:nview",
        "cmd:patch",
        "cmd:telnet",
        "cmd:tip",
        "cmd:uncompress",
        "cmd:vi",
        "cmd:view",
        "man:remote.5",
        "man:locate.updatedb.8",
        "man:updatedb.8",
        "etc/locate.rc",
        "usr/libexec/locate.*",
        "usr/share/vi",
    ]
