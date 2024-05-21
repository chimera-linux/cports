pkgname = "qt6-qtmultimedia"
pkgver = "6.7.1"
pkgrel = 2
build_style = "cmake"
# these install /usr/lib/qt6/plugins/multimedia/libmockmultimediaplugin.a which
# then has to exist for the -devel to work, but not splitting static keeps around
# stuff that can be split, so just don't build this instead
configure_args = ["-DQT_BUILD_TESTS=OFF"]
make_check_args = [
    "-E",
    "(tst_qscreencapturebackend"  # blacklisted on upstream CI, https://bugreports.qt.io/browse/QTBUG-111190
    "|tst_qwindowcapturebackend)",  # cannot find any windows, "hangs" for 9 mins
]
# tst_q{mediaplayerbackend,videoframecolormanagement} only work under xvfb
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "ffmpeg-devel",
    "gst-plugins-base-devel",
    "libpulse-devel",
    "libva-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtshadertools-devel",
    "qt6-qtsvg-devel",
]
checkdepends = ["xserver-xorg-xvfb", "mesa-dri"]
pkgdesc = "Qt6 Multimedia component"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtmultimedia-everywhere-src-{pkgver}.tar.xz"
sha256 = "656d1543727f5bf1bd39fe2548ac454860109dc8555df77d7940f21e3d65cd3e"
# FIXME: int breaks at least tst_qaudiodecoderbackend
hardening = ["!int"]
# TODO
options = ["!cross"]


match self.profile().arch:
    case "ppc64" | "ppc":
        # vsx assumptions in altivec code
        tool_flags = {"CXXFLAGS": ["-DEIGEN_DONT_VECTORIZE"]}


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True, force=True)


@subpackage("qt6-qtmultimedia-devel")
def _devel(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtshadertools-devel~{pkgver[:-2]}",
        f"qt6-qtsvg-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            # named based on BUILD_TYPE
            # "usr/lib/qt6/plugins/multimedia/objects-*",
            # "usr/lib/qt6/plugins/multimedia/libmockmultimediaplugin.*",
            "usr/lib/*.prl",
        ]
    )
