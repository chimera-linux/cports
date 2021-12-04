pkgname = "fonts-dejavu-otf"
pkgver = "2.37"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "full-otf"
make_build_args = ["full-ttf"]
hostmakedepends = ["gmake", "fontforge-cli", "perl-font-ttf"]
depends = ["fonts-dejavu-common"]
provides = [f"fonts-dejavu={pkgver}-r{pkgrel}"]
provider_priority = 2
pkgdesc = "DejaVu family of fonts (OpenType)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:Bitstream-Vera AND custom:Arev-Fonts AND custom:none"
url = "https://github.com/dejavu-fonts/dejavu-fonts"
source = f"{url}/archive/refs/tags/version_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "c4d10a1b665db893adc0c0aaee7ecd81b2b47c877d5cea0b40216707cbf327e4"
# font
options = ["!check"]

def post_patch(self):
    (self.cwd / "scripts/ogenerate.pe").chmod(0o755)

def do_install(self):
    for f in (self.cwd / "build").glob("*.otf"):
        self.install_file(f, "usr/share/fonts/dejavu")

    for f in (self.cwd / "build").glob("*.ttf"):
        self.install_file(f, "usr/share/fonts/dejavu")

    for f in (self.cwd / "fontconfig").glob("*.conf"):
        if "lgc" in f.name:
            continue
        self.install_file(f, "etc/fonts/conf.avail")

def post_install(self):
    self.install_license("LICENSE", pkgname = "fonts-dejavu-common")

@subpackage("fonts-dejavu-common")
def _common(self):
    self.pkgdesc = "DejaVu family of fonts (common files)"
    self.depends = ["mkfontscale"]
    return ["etc/fonts", "usr/share/licenses"]

@subpackage("fonts-dejavu-ttf")
def _ttf(self):
    self.pkgdesc = "DejaVu family of fonts (TrueType)"
    self.depends = ["fonts-dejavu-common"]
    self.provides = [f"fonts-dejavu={pkgver}-r{pkgrel}"]
    self.provider_priority = 1

    return ["usr/share/fonts/dejavu/*.ttf"]
