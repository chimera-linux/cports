pkgname = "qbittorrent"
pkgver = "5.1.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DSTACKTRACE=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "boost-devel",
    "libtorrent-rasterbar-devel",
    "openssl3-devel",
    "qt6-qtbase-private-devel",  # qtcore-config_p.h
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "QT-based torrent client"
license = "GPL-2.0-or-later"
url = "https://www.qbittorrent.org"
source = f"https://github.com/qbittorrent/qBittorrent/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "a35448f3c8cb57d033bd3c4bd66c63417b0ca793ae7e9c5c5053960e2229ad9e"
# CFI: BitTorrent::SessionImpl::SessionImpl crash
hardening = ["vis", "!cfi"]
# don't build
options = ["!check"]


def configure(self):
    from cbuild.util import cmake

    cmake.configure(self, build_dir="build-gui", extra_args=self.configure_args)
    cmake.configure(
        self,
        build_dir="build-nox",
        extra_args=[*self.configure_args, "-DGUI=OFF"],
    )


def build(self):
    from cbuild.util import cmake

    cmake.build(self, "build-gui")
    cmake.build(self, "build-nox")


def install(self):
    from cbuild.util import cmake

    cmake.install(self, "build-gui")
    cmake.install(self, "build-nox")

    self.install_service("^/qbittorrent-nox")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")


@subpackage("qbittorrent-nox")
def _(self):
    self.subdesc = "headless daemon"

    return [
        "usr/bin/qbittorrent-nox",
        "usr/lib/dinit.d",
        "usr/lib/sysusers.d",
        "usr/lib/tmpfiles.d",
        "usr/share/man/man1/qbittorrent-nox.1",
    ]
