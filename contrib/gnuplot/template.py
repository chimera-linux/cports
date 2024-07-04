pkgname = "gnuplot"
pkgver = "6.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-readline=bsd",
    "--with-gpic",
    "--with-metapost",
    "--with-metafont",
]
make_cmd = "gmake"
make_check_args = ["-j1"]
make_check_env = {"GNUTERM": "dumb"}
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "lua5.1",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "cairo-devel",
    "libcerf-devel",
    "libgd-devel",
    "lua5.1-devel",
    "pango-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "wxwidgets-devel",
    "zlib-ng-compat-devel",
]
depends = [f"gnuplot-common={pkgver}-r{pkgrel}"]
pkgdesc = "Command-line-driven graphing utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "gnuplot"
url = "http://www.gnuplot.info"
source = f"$(SOURCEFORGE_SITE)/gnuplot/gnuplot/{pkgver}/gnuplot-{pkgver}.tar.gz"
sha256 = "e85a660c1a2a1808ff24f7e69981ffcbac66a45c9dcf711b65610b26ea71379a"
# fails tests
hardening = ["!int"]
options = ["!cross"]


def do_configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.replace_guess(self)

    with self.stamp("autogen") as s:
        s.check()
        self.do("autoreconf", "-if")

    with self.stamp("configure-nox") as s:
        s.check()
        gnu_configure.configure(
            self,
            build_dir="build",
            extra_args=["--disable-wxwidgets", "--without-x", "--without-qt"],
            generator=False,
        )

    with self.stamp("configure-wx") as s:
        s.check()
        gnu_configure.configure(
            self,
            build_dir="build-wx",
            extra_args=["--enable-wxwidgets", "--without-qt"],
            generator=False,
        )

    with self.stamp("configure-qt") as s:
        s.check()
        gnu_configure.configure(
            self,
            build_dir="build-qt",
            extra_args=["--disable-wxwidgets", "--with-qt"],
            generator=False,
        )


def do_build(self):
    with self.stamp("build-nox") as s:
        s.check()
        self.do("gmake", "-C", "build", f"-j{self.make_jobs}")

    with self.stamp("build-wx") as s:
        s.check()
        self.do("gmake", "-C", "build-wx", f"-j{self.make_jobs}")

    with self.stamp("build-qt") as s:
        s.check()
        self.do("gmake", "-C", "build-qt", f"-j{self.make_jobs}")


def do_install(self):
    self.do(
        "gmake",
        "-C",
        "build-qt",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.rename("usr/bin/gnuplot", "gnuplot-qt")

    self.do(
        "gmake",
        "-C",
        "build-wx",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.rename("usr/bin/gnuplot", "usr/bin/gnuplot-wx")

    self.do(
        "gmake",
        "-C",
        "build",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )

    self.install_license("Copyright")


@subpackage("gnuplot-common-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 common files)"
    self.depends += [f"gnuplot-common={pkgver}-r{pkgrel}"]

    return ["usr/libexec/gnuplot/*/gnuplot_x11"]


@subpackage("gnuplot-qt")
def _qt(self):
    self.pkgdesc = f"{pkgdesc} (Qt frontend)"
    self.depends += [f"gnuplot-common-x11={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/gnuplot-qt",
        "usr/libexec/gnuplot/*/gnuplot_qt",
        "usr/share/gnuplot/*/qt",
    ]


@subpackage("gnuplot-wx")
def _wx(self):
    self.pkgdesc = f"{pkgdesc} (wxWidgets frontend)"
    self.depends += [f"gnuplot-common-x11={pkgver}-r{pkgrel}"]

    return ["usr/bin/gnuplot-wx"]


@subpackage("gnuplot-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"

    return ["usr/share"]
