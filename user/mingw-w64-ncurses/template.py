pkgname = "mingw-w64-ncurses"
pkgver = "6.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-big-core",
    "--enable-ext-colors",
    "--enable-colorfgbg",
    "--enable-database",
    "--enable-ext-mouse",
    "--enable-interop",
    "--enable-pc-files",
    "--enable-term-driver",
    "--enable-widec",
    "--disable-home-terminfo",
    "--disable-rpath-hack",
    "--disable-root-access",
    "--disable-setuid-environ",
    "--disable-symlinks",
    "--without-ada",
    "--without-debug",
    "--without-manpages",
    "--without-pthread",
    "--without-tests",  # TODO fix
    # "--enable-sp-funcs",
    "--with-shared",
    "ac_cv_header_alloca_h=no",  # not provided by mingw toolchain and only used for tests anyway
    # "ac_cv_path_ac_pt_PKG_CONFIG=/usr/bin/pkg-config",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
depends = []
pkgdesc = "Unix curses library for Windows development"
license = "MIT"
url = "http://www.gnu.org/software/ncurses"
source = f"$(GNU_SITE)/ncurses/ncurses-{pkgver}.tar.gz"
sha256 = "355b4cbbed880b0381a04c46617b7656e362585d52e9cf84a67e2009b749ff11"
# Check stage fails to build:
# /builddir/mingw-w64-ncurses-6.6/wrksrc/ncurses/curses.priv.h:533:45: note: expanded from macro 'SP_TERMTYPE'
#   533 | #define SP_TERMTYPE TerminalType(TerminalOf(sp)).
#       |                                             ^~
# /builddir/mingw-w64-ncurses-6.6/wrksrc/ncurses/tty/lib_mvcur.c:1365:55: error: use of undeclared identifier 'sp'
#  1365 |                 mvcur(roll(lines), roll(columns), roll(lines), roll(columns));
# TODO fix:
options = ["empty", "!check"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [
        f"mingw-w64-libssp-static-{_an}",
        f"clang-mingw-w64-{_an}",
    ]


def configure(self):
    for an in _targets:
        at = an + "-w64-mingw32"
        eargs = [
            f"--host={at}",
            f"--prefix=/usr/{at}",
            f"--with-pkg-config-libdir=/usr/{at}/lib/pkgconfig",
        ]
        self.mkdir(f"build-{an}")
        with self.stamp(f"{an}_configure") as s:
            _mingw_cflags = "-O2 -pipe -Wformat -Werror=format-security -fPIC"
            if an != "armv7" and an != "aarch64":
                _mingw_cflags += " -fcf-protection"
            s.check()
            self.do(
                self.chroot_cwd / "configure",
                *configure_args,
                *eargs,
                wrksrc=f"build-{an}",
                env={
                    "CC": f"{at}-clang",
                    "CFLAGS": _mingw_cflags,
                    "LDFLAGS": "",
                    "PKG_CONFIG_LIBDIR": f"/usr/{at}/lib/pkgconfig",
                },
            )


def build(self):
    for an in _targets:
        self.make_build_args = [f"-j{self.make_jobs}"]
        self.make.build(wrksrc=f"build-{an}")


def check(self):
    for an in _targets:
        self.make_check_args = [f"-j{self.make_jobs}"]
        self.make.check(wrksrc=f"build-{an}")


def install(self):
    for an in _targets:
        self.make.install(wrksrc=f"build-{an}")
        self.install_license("COPYING", name=f"{an}.COPYING")


def _gen(an, at):
    @subpackage(f"mingw-w64-ncurses-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.options = ["!strip", "hardlinks"]
        self.depends = []
        return [f"usr/{at}"]

    depends.append(self.with_pkgver(f"mingw-w64-ncurses-{an}"))


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
