pkgname = "gmic"
pkgver = "3.2.6"
pkgrel = 2
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "lib"
make_build_args = [
    "cli_shared",
    "gmic_qt_shared",
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
sha256 = "55993e55a30fe2da32f9533b9db2a3250affa2b32003b0c49c36eec2b2c6e007"
# vis broken
# FIXME int: gmic_qt PreviewWidget::updateOriginalImagePosition
hardening = ["!int"]
# no tests
# breaks in parallel if lib isn't built first by itself
options = ["!check", "!parallel"]


if self.profile().arch == "riscv64":
    broken = "qmake busted under emulation (https://bugreports.qt.io/browse/QTBUG-98951)"


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
