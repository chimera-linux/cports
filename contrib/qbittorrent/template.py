pkgname = "qbittorrent"
pkgver = "4.6.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT6=ON",
    "-DSTACKTRACE=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "boost-devel",
    "libtorrent-rasterbar-devel",
    "openssl-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "qt6-qtsvg-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "QT-based torrent client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.qbittorrent.org"
source = f"https://github.com/qbittorrent/qBittorrent/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "f330042fd0b27530b4a7b70b5d7ab356b2c9246393761df3b06891dc9dd8c106"
# FIXME: BitTorrent::SessionImpl::SessionImpl cfi crash
hardening = ["vis"]
# don't build
options = ["!check"]


def do_configure(self):
    from cbuild.util import cmake

    cmake.configure(self, build_dir="build-gui", extra_args=self.configure_args)
    cmake.configure(
        self,
        build_dir="build-nox",
        extra_args=self.configure_args + ["-DGUI=OFF"],
    )


def do_build(self):
    from cbuild.util import cmake

    cmake.build(self, "build-gui")
    cmake.build(self, "build-nox")


def do_install(self):
    from cbuild.util import cmake

    cmake.install(self, "build-gui")
    cmake.install(self, "build-nox")

    self.install_service(self.files_path / "qbittorrent-nox")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("qbittorrent-nox")
def _nox(self):
    self.depends = []
    return [
        "etc/dinit.d",
        "usr/bin/qbittorrent-nox",
        "usr/lib/sysusers.d",
        "usr/lib/tmpfiles.d",
        "usr/share/man/man1/qbittorrent-nox.1",
    ]
