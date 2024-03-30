pkgname = "schismtracker"
pkgver = "20240328"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "e1c57f8973ed83eabbb30e81f6a766c1f6c42f7a753ec76511835e2b30da7298"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
