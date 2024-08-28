pkgname = "fonts-liberation"
pkgver = "2.1.5"
pkgrel = 2
build_style = "makefile"
hostmakedepends = ["fontforge-cli", "python-fonttools"]
depends = ["mkfontscale"]
pkgdesc = "Liberation family of fonts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://github.com/liberationfonts/liberation-fonts"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9a823ccb33c8a8a865e84b982bcdc44d03ba4914adb91e6000df035dc0e55936"
# font
options = ["!check"]


def pre_build(self):
    self.make.invoke("versionupdate")


def install(self):
    self.install_file(
        f"liberation-fonts-otf-{pkgver}/*.otf",
        "usr/share/fonts/liberation",
        glob=True,
    )
    self.install_file(
        f"liberation-fonts-ttf-{pkgver}/*.ttf",
        "usr/share/fonts/liberation",
        glob=True,
    )
    for f in self.files_path.glob("*.conf"):
        self.install_file(f, "usr/share/fontconfig/conf.avail")


@subpackage("fonts-liberation-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-liberation-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/liberation/*.otf"]


@subpackage("fonts-liberation-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-liberation-otf"]

    return ["usr/share/fonts/liberation/*.ttf"]
