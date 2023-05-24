pkgname = "fonts-liberation"
pkgver = "2.1.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "fontforge-cli", "python-fonttools"]
depends = ["mkfontscale"]
pkgdesc = "Liberation family of fonts - OpenType"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://github.com/liberationfonts/liberation-fonts"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9a823ccb33c8a8a865e84b982bcdc44d03ba4914adb91e6000df035dc0e55936"
# font
options = ["!check"]


def pre_build(self):
    self.make.invoke("versionupdate")


def do_install(self):
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
        self.install_file(f, "etc/fonts/conf.avail")


@subpackage("fonts-liberation-otf")
def _otf(self):
    self.pkgdesc = "Liberation family of fonts - OpenType"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "!fonts-liberation-ttf"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/share/fonts/liberation/*.otf"]


@subpackage("fonts-liberation-ttf")
def _ttf(self):
    self.pkgdesc = "Liberation family of fonts - TrueType"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "!fonts-liberation-otf"]

    return ["usr/share/fonts/liberation/*.ttf"]
