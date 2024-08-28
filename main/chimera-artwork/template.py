pkgname = "chimera-artwork"
pkgver = "0.99.2"
pkgrel = 1
pkgdesc = "Chimera Linux artwork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-SA-4.0"
url = "https://chimera-linux.org"
source = f"https://github.com/chimera-linux/chimera-artwork/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "45ada21998df2c45a1d638119eaf450ee31da8a123911e4d15a8f9db9ffdc2c6"


def install(self):
    for f in ["png", "svg"]:
        self.install_file(f"chimera-logo.{f}", "usr/share/chimera-artwork")
    for s in [16, 22, 32, 48, 64, 128, 256, 512, 1024]:
        self.install_file(
            f"icons/chimera-logo-{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name="chimera-logo.png",
        )
    self.install_file(
        "icons/chimera-logo.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    dp = "usr/share/backgrounds/chimera"
    self.install_file("chimera-bg-d.svg", dp, name="bg-d.svg")
    self.install_file("chimera-bg-l.svg", dp, name="bg-l.svg")
    self.install_file(
        self.files_path / "chimera.xml", "usr/share/gnome-background-properties"
    )

    self.install_dir("usr/share/wallpapers/Chimera/contents/images")
    self.install_dir("usr/share/wallpapers/Chimera/contents/images_dark")
    self.install_file(
        "breeze-previews/metadata.json", "usr/share/wallpapers/Chimera"
    )
    self.install_link(
        "usr/share/wallpapers/Chimera/contents/images/2560x1600.svg",
        "../../../../backgrounds/chimera/bg-l.svg",
    )
    self.install_link(
        "usr/share/wallpapers/Chimera/contents/images_dark/2560x1600.svg",
        "../../../../backgrounds/chimera/bg-d.svg",
    )

    for theme in ["breeze", "breezedark", "breezetwilight"]:
        previews_path = f"usr/share/plasma/look-and-feel/org.kde.{theme}.desktop/contents/previews"
        self.install_dir(previews_path)
        self.install_file(
            f"breeze-previews/{theme}-preview.png",
            previews_path,
            name="preview.png",
        )
        self.install_file(
            f"breeze-previews/{theme}-fullscreenpreview.jpg",
            previews_path,
            name="fullscreenpreview.jpg",
        )


@subpackage("chimera-artwork-kde")
def _(self):
    self.subdesc = "KDE files"
    self.replaces = ["plasma-workspace<6.1.1-r1"]

    return ["usr/share/plasma", "usr/share/wallpapers"]
