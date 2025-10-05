pkgname = "qcoro"
pkgver = "0.12.0"
pkgrel = 3
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DQCORO_BUILD_EXAMPLES=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qjsvalue_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtwebsockets-devel",
]
checkdepends = [
    "dbus-x11",
]
pkgdesc = "Qt C++ Coroutine Library"
license = "MIT"
url = "https://qcoro.dvratil.cz"
source = (
    f"https://github.com/danvratil/qcoro/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "809afafab61593f994c005ca6e242300e1e3e7f4db8b5d41f8c642aab9450fbc"
# vis breaks symbols for test-qcorothread build,
# cfi breaks at least test-qcoro{task,websocket}
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("qcoro-devel")
def _(self):
    self.depends += [
        "qt6-qtdeclarative-devel",
        "qt6-qtwebsockets-devel",
    ]

    return self.default_devel(
        extra=[
            "usr/lib/qt6/mkspecs",
        ]
    )
