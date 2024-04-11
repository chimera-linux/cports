pkgname = "schismtracker"
pkgver = "20240409"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "51735768e3b7633678dac6162c5ff94216e2542bae709688f0102af0e97f29eb"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
