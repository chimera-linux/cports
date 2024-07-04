pkgname = "ncurses"
pkgver = "6.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-root-access",
    "--disable-setuid-environ",
    "--enable-big-core",
    "--enable-ext-colors",
    "--enable-fvisibility",
    "--enable-pc-files",
    "--enable-widec",
    "--without-debug",
    "--without-ada",
    "--with-shared",
    "--with-manpage-symlinks",
    "--with-manpage-format=normal",
    "--with-pkg-config-libdir=/usr/lib/pkgconfig",
    "ac_cv_path_ac_pt_PKG_CONFIG=/usr/bin/pkg-config",
]
# a hack to disable ncurses's magic detection code
# see https://ariadne.space/2021/10/25/dont-do-clever-things-in-configure-scripts
configure_env = {"PKG_CONFIG_LIBDIR": "/usr/lib/pkgconfig"}
# reconf is broken
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
depends = [f"ncurses-base={pkgver}-r{pkgrel}"]
# we generally want this in a proper system as a soft dep
install_if = [f"ncurses-libs={pkgver}-r{pkgrel}", "chimerautils"]
pkgdesc = "System V Release 4.0 curses emulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.gnu.org/software/ncurses"
source = f"$(GNU_SITE)/ncurses/{pkgname}-{pkgver}.tar.gz"
sha256 = "136d91bc269a9a5785e5f9e980bc76ab57428f604ce3e5a5a90cebc767971cc6"
tool_flags = {
    "CFLAGS": ["-fPIC"],
}
# FIXME int; prevents some chroots from working
# var-init breaks non-ascii input in catgirl
hardening = ["!int", "!var-init"]
options = ["bootstrap"]


def init_configure(self):
    with self.profile("host"):
        bcflags = self.get_cflags(shell=True)

    self.configure_args += [f"BUILD_CFLAGS={bcflags}"]


def post_install(self):
    self.install_license("COPYING")

    # fool packages looking to link to non-wide-character ncurses libraries
    for lib in ["curses", "ncurses", "form", "panel", "menu"]:
        libp = self.destdir / "usr/lib" / f"lib{lib}.so"
        libp.unlink(missing_ok=True)
        libp.with_suffix(".a").unlink(missing_ok=True)
        with open(libp, "w") as f:
            f.write(f"INPUT(-l{lib}w)\n")
        libp.chmod(0o755)
        self.install_link(f"usr/lib/lib{lib}.a", f"lib{lib}w.a")

    self.uninstall("usr/lib/libncurses++.a")
    self.install_link("usr/lib/libncurses++.a", "libncurses++w.a")

    # some packages look for -lcurses during build
    self.uninstall("usr/lib/libcursesw.so")
    with open(self.destdir / "usr/lib/libcursesw.so", "w") as f:
        f.write("INPUT(-lncursesw)\n")
    (self.destdir / "usr/lib/libcursesw.so").chmod(0o755)

    self.uninstall("usr/lib/libcurses.so")
    self.uninstall("usr/lib/libcursesw.a")
    self.uninstall("usr/lib/libcurses.a")

    self.install_link("usr/lib/libcurses.so", "libncurses.so")
    self.install_link("usr/lib/libcursesw.a", "libncursesw.a")
    self.install_link("usr/lib/libcurses.a", "libncurses.a")

    # create libtinfo symlinks
    self.install_link("usr/lib/libtinfo.so", "libncursesw.so")
    self.install_link(
        f"usr/lib/libtinfo.so.{pkgver}", f"libncursesw.so.{pkgver}"
    )
    self.install_link(
        f"usr/lib/libtinfo.so.{pkgver[0:pkgver.find('.')]}",
        f"libtinfo.so.{pkgver}",
    )
    self.install_link("usr/lib/pkgconfig/tinfo.pc", "ncursesw.pc")

    # remove broken symlink
    self.uninstall("usr/lib/terminfo")


@subpackage("ncurses-libtinfo-libs")
def _tinfo(self):
    self.pkgdesc = f"{pkgdesc} (libtinfo.so symlink)"

    return ["usr/lib/libtinfo*.so.*"]


@subpackage("ncurses-libtinfo-devel")
def _tdevel(self):
    self.pkgdesc = f"{pkgdesc} (libtinfo.so symlink) (development files)"
    self.depends += [f"ncurses-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libtinfo.so",
        "usr/lib/pkgconfig/tinfo.pc",
    ]


@subpackage("ncurses-libs")
def _libs(self):
    return self.default_libs()


@subpackage("ncurses-devel")
def _devel(self):
    return self.default_devel()


@subpackage("ncurses-base")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base terminfo files)"
    self.replaces = [
        # these used to ship their own, compat for upgrade
        "alacritty-terminfo",
        "foot-terminfo",
        # moved from there into here
        "ncurses-term<6.4-r1",
    ]
    self.options = ["hardlinks"]

    flist = []
    with (self.rparent.files_path / "base-files").open() as f:
        for fn in f:
            flist.append(fn.strip()[1:])

    return flist


@subpackage("ncurses-term")
def _term(self):
    self.pkgdesc = f"{pkgdesc} (full terminal descriptions)"
    self.depends = [f"ncurses-base={pkgver}-r{pkgrel}"]
    self.options = ["hardlinks"]

    return [
        "usr/share/tabset",
        "usr/share/terminfo",
    ]
