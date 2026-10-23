pkgname = "qcoro"
pkgver = "0.13.0"
pkgrel = 0
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
    "dbus",
]
pkgdesc = "Qt C++ Coroutine Library"
license = "MIT"
url = "https://qcoro.dvratil.cz"
source = (
    f"https://github.com/danvratil/qcoro/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "4bff7513c5c8e301b66308df05795043b1792ed16381a484e5c990171b8ff19e"
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
