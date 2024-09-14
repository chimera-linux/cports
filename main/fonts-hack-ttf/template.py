pkgname = "fonts-hack-ttf"
pkgver = "3.003"
pkgrel = 0
pkgdesc = "Typeface designed for source code"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT AND custom:Bitstream-Vera"
url = "https://sourcefoundry.org/hack"
source = (
    f"https://github.com/source-foundry/Hack/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3c6f1a20e86744077e83c9bacf879a5b13f659f1c07e9c5c57d6efc3cbe66c07"


def install(self):
    self.install_file(
        "config/fontconfig/45-Hack.conf", "usr/share/fontconfig/conf.avail"
    )
    self.install_file("build/ttf/*.ttf", "usr/share/fonts/hack", glob=True)
    self.install_license("LICENSE.md")
