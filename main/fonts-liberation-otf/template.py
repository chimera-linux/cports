pkgname = "fonts-liberation-otf"
pkgver = "2.1.5"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "fontforge-cli", "python-fonttools"]
depends = ["fonts-liberation-common"]
provides = [f"fonts-liberation={pkgver}-r{pkgrel}"]
provider_priority = 2
pkgdesc = "Liberation family of fonts (OpenType)"
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
    for f in (self.cwd / f"liberation-fonts-otf-{pkgver}").glob("*.otf"):
        self.install_file(f, "usr/share/fonts/liberation")

    for f in (self.cwd / f"liberation-fonts-ttf-{pkgver}").glob("*.ttf"):
        self.install_file(f, "usr/share/fonts/liberation")

    for f in self.files_path.glob("*.conf"):
        self.install_file(f, "etc/fonts/conf.avail")

@subpackage("fonts-liberation-common")
def _common(self):
    self.pkgdesc = "Liberation family of fonts (common files)"
    self.depends = ["mkfontscale"]
    return ["etc/fonts"]

@subpackage("fonts-liberation-ttf")
def _ttf(self):
    self.pkgdesc = "Liberation family of fonts (TrueType)"
    self.depends = ["fonts-liberation-common"]
    self.provides = [f"fonts-liberation={pkgver}-r{pkgrel}"]
    self.provider_priority = 1

    return ["usr/share/fonts/liberation/*.ttf"]
