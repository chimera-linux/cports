pkgname = "schismtracker"
pkgver = "20240503"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "7f86895eb3851e81940e966927570e4c94c76dc2884cb7f95ca9fff1425815f1"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
