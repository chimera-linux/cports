pkgname = "qbittorrent"
pkgver = "5.1.0"
pkgrel = 0
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
sha256 = "ac54cd8b3c6035cfcd684be5afd0eccc8c5fbbc3008a9b6f9ba42f6ef91105af"
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

    self.install_service(self.files_path / "qbittorrent-nox")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


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
