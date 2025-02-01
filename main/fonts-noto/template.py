pkgname = "fonts-noto"
pkgver = "2025.02.01"
pkgrel = 0
pkgdesc = "Google Noto fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/notofonts/notofonts.github.io"
source = f"{url}/archive/refs/tags/noto-monthly-release-{pkgver}.zip"
sha256 = "9919772b968399febf8eb9e77301caab92382c9d3c300dbeefb8f7f9cceee927"


def install(self):
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
    @subpackage(f"fonts-noto-{subn}")
    def _(self):
        self.subdesc = subd
        self.depends = [self.parent, f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [self.parent]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{subn}",
            f"usr/share/fonts/noto/Noto*-Regular.{subn}",
        ]

    @subpackage(f"fonts-noto-extra-{subn}")
    def _(self):
        self.subdesc = f"{subd} additional variants"
        self.depends = [
            self.with_pkgver(f"{pkgname}-extra"),
            f"!{pkgname}-extra-{subc}",
            f"!{pkgname}-{subc}",
        ]
        if subn == "otf":
            self.install_if = [self.with_pkgver(f"{pkgname}-extra")]

        return [f"usr/share/fonts/noto/*.{subn}"]


for _subn, _subd, _subc in [
    ("otf", "OpenType", "ttf"),
    ("ttf", "TrueType", "otf"),
]:
    _gensub(_subn, _subd, _subc)


@subpackage("fonts-noto-extra")
def _(self):
    self.subdesc = "additional variants"
    self.depends = [self.parent]
    self.options = ["empty"]

    return []
