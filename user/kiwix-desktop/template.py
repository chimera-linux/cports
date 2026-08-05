pkgname = "kiwix-desktop"
pkgver = "2.5.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "qt6-qtbase-devel",
    "qt6-qttools",
]
makedepends = [
    "libkiwix-devel",
    "libzim-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebchannel-devel",
    "qt6-qtwebengine-devel",
]
depends = ["aria2"]
pkgdesc = "Offline reader for web content"
license = "GPL-3.0-or-later"
url = "https://github.com/kiwix/kiwix-desktop"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "30936feca234addcf7dbc58961750a0efe87023284a4a2f0fe36adeb44daaf91"
# no tests
options = ["!check"]


def post_patch(self):
    pro = self.cwd / "kiwix-desktop.pro"
    pro.write_text(pro.read_text().replace("QMAKE_CXXFLAGS += -Werror\n", ""))


def configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


def post_install(self):
    self.install_license("LICENSE")
