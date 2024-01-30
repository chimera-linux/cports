pkgname = "schismtracker"
pkgver = "20240129"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "77ad153c088208926b2d43254463aab9a0b3cb2e103db912c3ac30d3fda0d016"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
