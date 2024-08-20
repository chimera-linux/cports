pkgname = "qcoro"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DQCORO_BUILD_EXAMPLES=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
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
sha256 = "b7c8f00273ad27d85814bf4ec93eb6922c75656800a61d11854d36355a4a1aec"
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
