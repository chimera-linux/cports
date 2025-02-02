pkgname = "gnuplot"
pkgver = "6.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-readline=bsd",
    "--with-gpic",
    "--with-metapost",
    "--with-metafont",
]
make_check_args = ["-j1"]
make_check_env = {"GNUTERM": "dumb"}
hostmakedepends = [
    "automake",
    "lua5.1",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
    "slibtool",
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
depends = [self.with_pkgver("gnuplot-common")]
pkgdesc = "Command-line-driven graphing utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "gnuplot"
url = "http://www.gnuplot.info"
source = f"$(SOURCEFORGE_SITE)/gnuplot/gnuplot/{pkgver}/gnuplot-{pkgver}.tar.gz"
sha256 = "f68a3b0bbb7bbbb437649674106d94522c00bf2f285cce0c19c3180b1ee7e738"
# fails tests
hardening = ["!int"]
# parallel: build fails since 6.0.2 with parallelism
options = ["!cross", "!parallel"]


def configure(self):
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


def build(self):
    with self.stamp("build-nox") as s:
        s.check()
        self.do("make", "-C", "build", f"-j{self.make_jobs}")

    with self.stamp("build-wx") as s:
        s.check()
        self.do("make", "-C", "build-wx", f"-j{self.make_jobs}")

    with self.stamp("build-qt") as s:
        s.check()
        self.do("make", "-C", "build-qt", f"-j{self.make_jobs}")


def install(self):
    self.do(
        "make",
        "-C",
        "build-qt",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.rename("usr/bin/gnuplot", "gnuplot-qt")

    self.do(
        "make",
        "-C",
        "build-wx",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )
    self.rename("usr/bin/gnuplot", "gnuplot-wx")

    self.do(
        "make",
        "-C",
        "build",
        f"-j{self.make_jobs}",
        "install",
        f"DESTDIR={self.chroot_destdir}",
    )

    self.install_license("Copyright")


@subpackage("gnuplot-common-x11")
def _(self):
    self.subdesc = "X11 common files"
    self.depends += [self.with_pkgver("gnuplot-common")]

    return ["usr/libexec/gnuplot/*/gnuplot_x11"]


@subpackage("gnuplot-qt")
def _(self):
    self.subdesc = "Qt frontend"
    self.depends += [self.with_pkgver("gnuplot-common-x11")]

    return [
        "usr/bin/gnuplot-qt",
        "usr/libexec/gnuplot/*/gnuplot_qt",
        "usr/share/gnuplot/*/qt",
    ]


@subpackage("gnuplot-wx")
def _(self):
    self.subdesc = "wxWidgets frontend"
    self.depends += [self.with_pkgver("gnuplot-common-x11")]

    return ["usr/bin/gnuplot-wx"]


@subpackage("gnuplot-common")
def _(self):
    self.subdesc = "common files"

    return ["usr/share"]
