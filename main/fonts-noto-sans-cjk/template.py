pkgname = "fonts-noto-sans-cjk"
pkgver = "2.004"
pkgrel = 1
pkgdesc = "Google Noto Sans CJK fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/googlefonts/noto-cjk"

source = [
    f"{url}/releases/download/Sans{pkgver}/03_NotoSansCJK-OTC.zip",
    f"{url}/releases/download/Sans{pkgver}/04_NotoSansCJK-OTF.zip",
]
sha256 = [
    "528f4e1b25ff3badb0321b38d015d954c4c0de926c7830ef50e4a1948f6a3eed",
    "8516970d4ff5f9d1f8bdd4ad5b9d6b5e1d292c816303e288c4933390b0e8abdb",
]


def install(self):
    self.install_file(
        self.files_path / "70-noto-sans-cjk.conf",
        "usr/share/fontconfig/conf.avail",
    )

    self.install_file("*.ttc", "usr/share/fonts/noto", glob=True)
    self.install_file("OTF/*/*.otf", "usr/share/fonts/noto", glob=True)


def post_install(self):
    self.install_license("LICENSE")


def _gensub(subn, subd, subc, sube):
    @subpackage(f"fonts-noto-sans-cjk-{subn}")
    def _(self):
        self.subdesc = subd
        self.depends = [self.parent, f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [self.parent]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{sube}",
            f"usr/share/fonts/noto/Noto*-Regular.{sube}",
        ]

    @subpackage(f"fonts-noto-sans-cjk-extra-{subn}")
    def _(self):
        self.subdesc = f"{subd} (additional variants"
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


@subpackage("fonts-noto-sans-cjk-extra")
def _(self):
    self.subdesc = "additional variants"
    self.depends = [self.parent]
    self.options = ["empty"]

    return []
