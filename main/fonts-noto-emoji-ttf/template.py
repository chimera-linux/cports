pkgname = "fonts-noto-emoji-ttf"
pkgver = "2.042"
pkgrel = 1
pkgdesc = "Google Noto emoji fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-emoji"
source = f"{url}/archive/v{pkgver}/font-noto-emoji-{pkgver}.tar.gz"
sha256 = "b56bd2fa4029d0f057b66b742ac59af243dbc91067fed3eb4929dac762440fc9"
# No copyright header in license text
options = ["!distlicense"]


def install(self):
    self.install_file(
        self.files_path / "66-noto-color-emoji.conf",
        "usr/share/fontconfig/conf.avail",
    )
    self.install_file("fonts/NotoColorEmoji.ttf", "usr/share/fonts/noto")
