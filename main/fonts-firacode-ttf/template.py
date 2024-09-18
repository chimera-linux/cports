pkgname = "fonts-firacode-ttf"
pkgver = "6.2"
pkgrel = 0
pkgdesc = "Free monospaced font with programming ligatures"
maintainer = "triallax <triallax@tutanota.com>"
license = "OFL-1.1"
url = "https://github.com/tonsky/FiraCode"
source = f"{url}/releases/download/{pkgver}/Fira_Code_v{pkgver}.zip"
sha256 = "0949915ba8eb24d89fd93d10a7ff623f42830d7c5ffc3ecbf960e4ecad3e3e79"
# no license in tarball
options = ["!distlicense"]


def install(self):
    self.install_file("ttf/*.ttf", "usr/share/fonts/firacode", glob=True)
    self.install_file(
        "variable_ttf/*.ttf", "usr/share/fonts/firacode", glob=True
    )
