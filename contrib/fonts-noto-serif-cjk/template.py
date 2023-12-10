pkgname = "fonts-noto-serif-cjk"
pkgver = "2.002"
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
    "941985d9fd860492d15640b53edc9668d568877140c524ccd83deb3d9b7a2950",
    "f3c53999f0c65eae5ad73c7db34217ded4d823fb67c9f3902a4b552734e3fba0",
]


def do_install(self):
    self.install_file(
        self.files_path / "70-noto-serif-cjk.conf",
        "usr/share/fontconfig/conf.avail",
    )

    self.install_file("OTC/*.ttc", "usr/share/fonts/noto", glob=True)
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


@subpackage("fonts-noto-serif-cjk-extra")
def _extra(self):
    self.pkgdesc = f"{pkgdesc} (additional variants)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.build_style = "meta"

    return []
