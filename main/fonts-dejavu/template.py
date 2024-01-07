pkgname = "fonts-dejavu"
pkgver = "2.37"
pkgrel = 2
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "full-otf"
make_build_args = ["full-ttf"]
hostmakedepends = ["gmake", "fontforge-cli", "perl-font-ttf"]
depends = ["mkfontscale"]
pkgdesc = "DejaVu family of fonts"
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

    self.install_dir("etc/fonts/conf.d")

    for f in (self.cwd / "fontconfig").glob("*.conf"):
        if "lgc" in f.name:
            continue
        self.install_file(f, "usr/share/fontconfig/conf.avail")
        self.install_link(
            f"/usr/share/fontconfig/conf.avail/{f.name}",
            f"etc/fonts/conf.d/{f.name}",
        )


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fonts-dejavu-otf")
def _otf(self):
    self.pkgdesc = "DejaVu family of fonts - OpenType"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "!fonts-dejavu-ttf"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/share/fonts/dejavu/*.otf"]


@subpackage("fonts-dejavu-ttf")
def _ttf(self):
    self.pkgdesc = "DejaVu family of fonts - TrueType"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "!fonts-dejavu-otf"]

    return ["usr/share/fonts/dejavu/*.ttf"]
