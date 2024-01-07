pkgname = "gmic"
pkgver = "3.3.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "QMAKE=qmake6",
    "OPT_CFLAGS=",
]
make_use_env = True
hostmakedepends = [
    "bash",
    "gimp",
    "gmake",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "fftw-devel",
    "libcurl-devel",
    "libomp-devel",
    "libpng-devel",
    "libtiff-devel",
    "libx11-devel",
    "openexr-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Full-featured Open-Source Framework for Image Processing"
maintainer = "psykose <alice@ayaya.dev>"
license = "CECILL-2.1"
url = "https://gmic.eu"
source = f"https://gmic.eu/files/source/gmic_{pkgver}.tar.gz"
sha256 = "d95ead2339c552378cef2947e844d5ec247f3a8485471786395aee10f566f868"
# vis broken
# FIXME int: gmic_qt PreviewWidget::updateOriginalImagePosition
hardening = ["!int"]
# no tests
options = ["!check"]


if self.profile().arch == "riscv64":
    broken = "qmake busted under emulation (https://bugreports.qt.io/browse/QTBUG-98951)"


def do_build(self):
    # lib has to come first to not be built multiple times for all subsequent
    # targets, rest can be parallel (and so this is faster than -j1)
    self.make.build(["lib"])
    self.make.build(["cli_shared", "gmic_qt_shared"])


def post_install(self):
    self.install_dir("usr/share")
    self.mv(
        self.destdir / "plug-ins",
        self.destdir / "usr/share/gmic",
    )


@subpackage("gmic-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gmic-qt")
def _qt(self):
    self.pkgdesc = "Qt GUI for GMIC"
    return [
        "usr/bin/gmic_qt",
        "usr/share/applications",
        "usr/share/icons",
    ]
