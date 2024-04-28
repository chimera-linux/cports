pkgname = "schismtracker"
pkgver = "20240426"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "2d478fc4caab297a3f08270a0ac19d01fe2860957094791eaf50c6c99227e668"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
