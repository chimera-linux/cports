pkgname = "supersonic"
pkgver = "0.21.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = [
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "mpv-devel",
]
go_build_tags = ["migrated_fynedo"]
pkgdesc = "Client for Subsonic and Jellyfin music servers"
license = "GPL-3.0-or-later AND BSD-3-Clause AND MIT"
url = "https://github.com/dweymouth/supersonic"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b532e5fb0c2e03949a704ac12576713a85eb1890012befd2f2479caa35723804"


def post_install(self):
    self.rename("usr/bin/supersonic", "supersonic-desktop")
    self.install_license("LICENSE")
    for res in [128, 256, 512]:
        self.install_file(
            f"res/appicon-{res}.png",
            f"usr/share/icons/hicolor/{res}x{res}/apps",
            name="supersonic-desktop.png",
        )
    self.install_file(
        "res/supersonic-desktop.desktop",
        "usr/share/applications",
    )
