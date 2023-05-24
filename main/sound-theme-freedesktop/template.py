pkgname = "sound-theme-freedesktop"
pkgver = "0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Freedesktop sound theme"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:sound-theme-freedesktop"
url = "https://freedesktop.org/wiki/Specifications/sound-theme-spec"
source = (
    f"https://people.freedesktop.org/~mccann/dist/{pkgname}-{pkgver}.tar.bz2"
)
sha256 = "cb518b20eef05ec2e82dda1fa89a292c1760dc023aba91b8aa69bafac85e8a14"
# breaks with our intltool removal and there are no tests anyway
options = ["!check"]


def pre_build(self):
    # there is no intltool to do it
    self.cp("index.theme.in", "index.theme")


def post_install(self):
    self.install_license("CREDITS")


configure_gen = []
