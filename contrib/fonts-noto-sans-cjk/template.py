pkgname = "fonts-noto-sans-cjk"
pkgver = "2.004"
pkgrel = 0
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


def do_install(self):
    self.install_file(
        self.files_path / "70-noto-sans-cjk.conf",
        "usr/share/fontconfig/conf.avail",
    )

    self.install_file("*.ttc", "usr/share/fonts/noto", glob=True)
    self.install_file("OTF/*/*.otf", "usr/share/fonts/noto", glob=True)


def post_install(self):
    self.install_license("LICENSE")


def _gensub(subn, subd, subc, sube):
    @subpackage(f"{pkgname}-{subn}")
    def _sub(self):
        self.pkgdesc = f"{pkgdesc} - {subd}"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{sube}",
            f"usr/share/fonts/noto/Noto*-Regular.{sube}",
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

        return [f"usr/share/fonts/noto/*.{sube}"]


for _subn, _subd, _subc, _sube in [
    ("otf", "OpenType", "ttf", "otf"),
    ("ttf", "TrueType", "otf", "ttc"),
]:
    _gensub(_subn, _subd, _subc, _sube)


@subpackage("fonts-noto-sans-cjk-extra")
def _extra(self):
    self.pkgdesc = f"{pkgdesc} (additional variants)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.build_style = "meta"

    return []
