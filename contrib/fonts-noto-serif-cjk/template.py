pkgname = "fonts-noto-serif-cjk"
pkgver = "2.003"
pkgrel = 0
pkgdesc = "Google Noto Serif CJK fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-cjk"

source = [
    f"{url}/releases/download/Serif{pkgver}/04_NotoSerifCJKOTC.zip",
    f"{url}/releases/download/Serif{pkgver}/05_NotoSerifCJKOTF.zip",
]
sha256 = [
    "c76ed8fd491ce98182ec6430238b90a1eabea8857c7db64e9037efa38e198a31",
    "9a8475c8272209e3e98fa8818b802d80f6b3016b3df77eb7d0893c0c7ae54245",
]


def install(self):
    self.install_file(
        self.files_path / "70-noto-serif-cjk.conf",
        "usr/share/fontconfig/conf.avail",
    )

    self.install_file("OTC/*.ttc", "usr/share/fonts/noto", glob=True)
    self.install_file("OTF/*/*.otf", "usr/share/fonts/noto", glob=True)


def post_install(self):
    self.install_license("LICENSE")


def _gensub(subn, subd, subc, sube):
    @subpackage(f"fonts-noto-serif-cjk-{subn}")
    def _(self):
        self.subdesc = subd
        self.depends = [self.parent, f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [self.parent]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{sube}",
            f"usr/share/fonts/noto/Noto*-Regular.{sube}",
        ]

    @subpackage(f"fonts-noto-serif-cjk-extra-{subn}")
    def _(self):
        self.subdesc = f"{subd} additional variants"
        self.depends = [
            self.with_pkgver(f"{pkgname}-extra"),
            f"!{pkgname}-extra-{subc}",
            f"!{pkgname}-{subc}",
        ]
        if subn == "otf":
            self.install_if = [self.with_pkgver(f"{pkgname}-extra")]

        return [f"usr/share/fonts/noto/*.{sube}"]


for _subn, _subd, _subc, _sube in [
    ("otf", "OpenType", "ttf", "otf"),
    ("ttf", "TrueType", "otf", "ttc"),
]:
    _gensub(_subn, _subd, _subc, _sube)


@subpackage("fonts-noto-serif-cjk-extra")
def _(self):
    self.subdesc = "additional variants"
    self.depends = [self.parent]
    self.options = ["empty"]

    return []
