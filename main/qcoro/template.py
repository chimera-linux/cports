pkgname = "qcoro"
pkgver = "0.11.0"
pkgrel = 2
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://qcoro.dvratil.cz"
source = (
    f"https://github.com/danvratil/qcoro/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "9942c5b4c533192f6c5954dc6d10178b3829075e6a621b67df73f0a4b74d8297"
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
