pkgname = "chimerautils"
pkgver = "14.2.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib/chimerautils",
    "-Dchimera_realpath=enabled",
]
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel",
    "bzip2-devel",
    "libedit-devel",
    "libxo-devel",
    "musl-bsd-headers",
    "ncurses-devel",
    "openssl-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = ["base-files", "debianutils"]
# compat
provides = [
    self.with_pkgver("musl-fts"),
    self.with_pkgver("musl-rpmatch"),
]
pkgdesc = "Chimera Linux userland"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimerautils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "122ee06196ad237148070b9dd9c7ab0a66aab8369090d21650da606492943bf2"
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


def post_install(self):
    # license
    self.install_license("LICENSE")
    # less
    self.uninstall("usr/bin/zless")
    self.uninstall("usr/share/man/man1/zless.1")
    # base shell
    self.install_shell("/usr/bin/sh")
    # tiny tools
    tdest = "usr/lib/chimerautils/tiny"
    self.install_dir(tdest)
    for f in (self.destdir / "usr/bin").glob("*.tiny"):
        self.mv(f, self.destdir / tdest / f.stem)
    # etc files, handled with tmpfiles
    self.install_dir("usr/share/chimerautils")
    self.install_tmpfiles(self.files_path / "chimerautils.conf")
    self.install_tmpfiles(
        self.files_path / "chimerautils-extra.conf", name="chimerautils-extra"
    )
    for f in (self.destdir / "etc").iterdir():
        self.mv(f, self.destdir / "usr/share/chimerautils")


@subpackage("chimerautils-devel-man")
def _(self):
    # former conflicts with fts/rpmatch manpages
    self.replaces = ["man-pages-devel<6.9.1-r3"]
    return ["usr/share/man/man3"]


@subpackage("chimerautils-devel")
def _(self):
    # compat
    self.provides = [
        self.with_pkgver("musl-fts-devel"),
        self.with_pkgver("musl-rpmatch-devel"),
    ]
    # explicitly non-lto
    self.options = ["ltostrip", "!splitstatic"]
    return self.default_devel()


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
        "usr/lib/chimerautils/locate.*",
        "usr/lib/tmpfiles.d/chimerautils-extra.conf",
        "usr/share/chimerautils/locate.rc",
        "usr/share/vi",
    ]
