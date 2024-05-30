pkgname = "schismtracker"
pkgver = "20240529"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "73c475b3344c460cbc543878f8c728af3c62fba11211604834d880c0a41a506e"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
