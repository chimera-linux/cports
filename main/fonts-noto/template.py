pkgname = "fonts-noto"
pkgver = "2025.08.01"
pkgrel = 0
pkgdesc = "Google Noto fonts"
license = "OFL-1.1"
url = "https://github.com/notofonts/notofonts.github.io"
source = f"{url}/archive/refs/tags/noto-monthly-release-{pkgver}.zip"
sha256 = "5fd3c957c8c8ca00c4b5efbbe6d05a9946c93948b987e997c1c4b180f9d2ce29"


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
