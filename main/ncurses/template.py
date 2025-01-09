pkgname = "ncurses"
pkgver = "6.5"
pkgrel = 3
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
hostmakedepends = ["pkgconf"]
depends = [self.with_pkgver("ncurses-base")]
# we generally want this in a proper system as a soft dep
install_if = [self.with_pkgver("ncurses-libs"), "chimerautils"]
pkgdesc = "System V Release 4.0 curses emulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.gnu.org/software/ncurses"
source = f"$(GNU_SITE)/ncurses/ncurses-{pkgver}.tar.gz"
sha256 = "136d91bc269a9a5785e5f9e980bc76ab57428f604ce3e5a5a90cebc767971cc6"
tool_flags = {
    "CFLAGS": ["-fPIC"],
}
# FIXME int; prevents some chroots from working
# var-init breaks non-ascii input in catgirl
hardening = ["!int", "!var-init"]
options = ["bootstrap"]

_base_tinfos = [
    "9/9term",
    "A/Apple_Terminal",
    "E/Eterm",
    "E/Eterm-256color",
    "E/Eterm-88color",
    "E/Eterm-color",
    "a/alacritty",
    "a/alacritty+common",
    "a/alacritty-direct",
    "a/ansi",
    "a/ansi80x25",
    "a/ansis",
    "c/cons25",
    "c/cygwin",
    "d/dumb",
    "f/foot",
    "f/foot+base",
    "f/foot-direct",
    "g/gnome",
    "g/gnome-2007",
    "g/gnome-256color",
    "g/gnome-fc5",
    "g/gnome-rh62",
    "g/gnome-rh72",
    "g/gnome-rh80",
    "g/gnome-rh90",
    "h/hurd",
    "i/iterm2",
    "i/iterm2-direct",
    "j/jfbterm",
    "k/kitty",
    "k/kitty+common",
    "k/kitty-direct",
    "k/kon",
    "k/kon2",
    "k/konsole",
    "k/konsole-256color",
    "k/konsole-base",
    "k/konsole-direct",
    "l/linux",
    "m/mach",
    "m/mach-bold",
    "m/mach-color",
    "m/mintty",
    "m/mintty+common",
    "m/mintty-direct",
    "m/mlterm",
    "m/mrxvt",
    "n/nsterm",
    "n/nxterm",
    "p/pcansi",
    "p/putty",
    "p/putty-256color",
    "p/putty-vt100",
    "r/rxvt",
    "r/rxvt-16color",
    "r/rxvt-256color",
    "r/rxvt-88color",
    "r/rxvt-basic",
    "r/rxvt-color",
    "r/rxvt-cygwin",
    "r/rxvt-cygwin-native",
    "r/rxvt-xpm",
    "s/screen",
    "s/screen-16color",
    "s/screen-16color-bce",
    "s/screen-16color-bce-s",
    "s/screen-16color-s",
    "s/screen-256color",
    "s/screen-256color-bce",
    "s/screen-256color-bce-s",
    "s/screen-256color-s",
    "s/screen-bce",
    "s/screen-s",
    "s/screen-w",
    "s/screen.linux",
    "s/screen.mlterm",
    "s/screen.rxvt",
    "s/screen.teraterm",
    "s/screen.xterm-new",
    "s/screen.xterm-r6",
    "s/screen.xterm-xfree86",
    "s/st",
    "s/st-direct",
    "s/sun",
    "s/sun1",
    "s/sun2",
    "t/teraterm",
    "t/terminator",
    "t/terminology",
    "t/termite",
    "t/tmux",
    "t/tmux-256color",
    "t/tmux-direct",
    "v/vs100",
    "v/vscode",
    "v/vscode-direct",
    "v/vt100",
    "v/vt100-am",
    "v/vt100-nav",
    "v/vt102",
    "v/vt200",
    "v/vt220",
    "v/vt52",
    "v/vte",
    "v/vte-2014",
    "v/vte-2017",
    "v/vte-2018",
    "v/vte-256color",
    "v/vte-direct",
    "w/wsvt25",
    "w/wsvt25m",
    "x/xfce",
    "x/xterm",
    "x/xterm-1002",
    "x/xterm-1003",
    "x/xterm-16color",
    "x/xterm-24",
    "x/xterm-256color",
    "x/xterm-88color",
    "x/xterm-8bit",
    "x/xterm-basic",
    "x/xterm-bold",
    "x/xterm-color",
    "x/xterm-direct",
    "x/xterm-hp",
    "x/xterm-new",
    "x/xterm-nic",
    "x/xterm-noapp",
    "x/xterm-old",
    "x/xterm-pcolor",
    "x/xterm-r5",
    "x/xterm-r6",
    "x/xterm-sco",
    "x/xterm-sun",
    "x/xterm-vt220",
    "x/xterm-vt52",
    "x/xterm-xf86-v32",
    "x/xterm-xf86-v33",
    "x/xterm-xf86-v333",
    "x/xterm-xf86-v40",
    "x/xterm-xf86-v43",
    "x/xterm-xf86-v44",
    "x/xterm-xfree86",
    "x/xterm-xi",
    "x/xterms",
]


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

    self.install_link("usr/lib/libncurses++.a", "libncurses++w.a")

    # some packages look for -lcurses during build
    with open(self.destdir / "usr/lib/libcursesw.so", "w") as f:
        f.write("INPUT(-lncursesw)\n")
    (self.destdir / "usr/lib/libcursesw.so").chmod(0o755)

    self.uninstall("usr/lib/libcurses.so")
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
        f"usr/lib/libtinfo.so.{pkgver[0 : pkgver.find('.')]}",
        f"libtinfo.so.{pkgver}",
    )
    self.install_link("usr/lib/pkgconfig/tinfo.pc", "ncursesw.pc")

    # remove broken symlink
    self.uninstall("usr/lib/terminfo")


@subpackage("ncurses-libtinfo-libs")
def _(self):
    self.subdesc = "libtinfo.so symlink"

    return ["usr/lib/libtinfo*.so.*"]


@subpackage("ncurses-libtinfo-devel")
def _(self):
    self.subdesc = "libtinfo.so development files"
    self.depends += [self.with_pkgver("ncurses-devel")]

    return [
        "usr/lib/libtinfo.so",
        "usr/lib/pkgconfig/tinfo.pc",
    ]


@subpackage("ncurses-libs")
def _(self):
    return self.default_libs()


@subpackage("ncurses-devel")
def _(self):
    return self.default_devel()


@subpackage("ncurses-base")
def _(self):
    self.subdesc = "base terminfo files"
    self.replaces = [
        # these used to ship their own, compat for upgrade
        "alacritty-terminfo",
        "foot-terminfo",
        # moved from there into here
        "ncurses-term<6.4-r1",
    ]
    self.options = ["hardlinks"]

    return [*map(lambda v: f"usr/share/terminfo/{v}", _base_tinfos)]


@subpackage("ncurses-term")
def _(self):
    self.subdesc = "full terminal descriptions"
    self.depends = [self.with_pkgver("ncurses-base")]
    self.options = ["hardlinks"]

    return [
        "usr/share/tabset",
        "usr/share/terminfo",
    ]
