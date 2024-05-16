pkgname = "schismtracker"
pkgver = "20240515"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "ac4a320b8cf4cb5ec44b8f384df2276d053791fb5161b974008c6867c84da3f9"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
