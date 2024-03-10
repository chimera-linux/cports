pkgname = "schismtracker"
pkgver = "20240308"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "8e0a69f51c19527ea91f7e27a640b38d8814e860e1b9af22d541f6c0743b63d9"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
