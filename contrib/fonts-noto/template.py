pkgname = "fonts-noto"
pkgver = "24.2.1"
pkgrel = 0
pkgdesc = "Google Noto fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/notofonts/notofonts.github.io"
source = f"{url}/archive/refs/tags/noto-monthly-release-{pkgver}.zip"
sha256 = "5c76e5b40040768fa7babe2d080bbe6dc4d630c48112797216448f94567449e4"


def do_install(self):
    for f in self.files_path.glob("*.conf"):
        self.install_file(f, "usr/share/fontconfig/conf.avail")

    self.install_file(
        "fonts/Noto*/hinted/ttf/*.ttf", "usr/share/fonts/noto", glob=True
    )

    self.install_file(
        "fonts/Noto*/unhinted/otf/*.otf", "usr/share/fonts/noto", glob=True
    )


def post_install(self):
    self.install_license("fonts/LICENSE")


def _gensub(subn, subd, subc):
    @subpackage(f"{pkgname}-{subn}")
    def _sub(self):
        self.pkgdesc = f"{pkgdesc} - {subd}"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{subn}",
            f"usr/share/fonts/noto/Noto*-Regular.{subn}",
        ]

    @subpackage(f"{pkgname}-extra-{subn}")
    def _sub_extra(self):
        self.pkgdesc = f"{pkgdesc} - {subd} (additional variants)"
        self.depends = [
            f"{pkgname}-extra={pkgver}-r{pkgrel}",
            f"!{pkgname}-extra-{subc}",
            f"!{pkgname}-{subc}",
        ]
        if subn == "otf":
            self.install_if = [f"{pkgname}-extra={pkgver}-r{pkgrel}"]

        return [f"usr/share/fonts/noto/*.{subn}"]


for _subn, _subd, _subc in [
    ("otf", "OpenType", "ttf"),
    ("ttf", "TrueType", "otf"),
]:
    _gensub(_subn, _subd, _subc)


@subpackage("fonts-noto-extra")
def _extra(self):
    self.pkgdesc = f"{pkgdesc} (additional variants)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["empty"]

    return []
