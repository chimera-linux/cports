pkgname = "fonts-xorg"
pkgver = "1.0.4"
pkgrel = 0
build_style = "meta"
depends = [
    f"fonts-xorg-100dpi={pkgver}-r{pkgrel}",
    f"fonts-xorg-75dpi={pkgver}-r{pkgrel}",
    f"fonts-xorg-cyrillic={pkgver}-r{pkgrel}",
    f"fonts-xorg-misc={pkgver}-r{pkgrel}",
    f"fonts-xorg-type1={pkgver}-r{pkgrel}",
]
pkgdesc = "X.org font packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://xorg.freedesktop.org"


@subpackage("fonts-xorg-100dpi")
def _100dpi(self):
    self.pkgdesc = f"{pkgdesc} (100dpi)"
    self.depends = [
        "font-adobe-100dpi",
        "font-adobe-utopia-100dpi",
        "font-bh-100dpi",
        "font-bh-lucidatypewriter-100dpi",
        "font-bitstream-100dpi",
    ]

    return []


@subpackage("fonts-xorg-75dpi")
def _75dpi(self):
    self.pkgdesc = f"{pkgdesc} (100dpi)"
    self.depends = [
        "font-adobe-75dpi",
        "font-adobe-utopia-75dpi",
        "font-bh-75dpi",
        "font-bh-lucidatypewriter-75dpi",
        "font-bitstream-75dpi",
    ]

    return []


@subpackage("fonts-xorg-cyrillic")
def _cyrillic(self):
    self.pkgdesc = f"{pkgdesc} (cyrillic)"
    self.depends = [
        "font-cronyx-cyrillic",
        "font-misc-cyrillic",
        "font-screen-cyrillic",
        "font-winitzki-cyrillic",
    ]

    return []


@subpackage("fonts-xorg-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (misc)"
    self.depends = [
        "font-arabic-misc",
        "font-cursor-misc",
        "font-daewoo-misc",
        "font-dec-misc",
        "font-isas-misc",
        "font-jis-misc",
        "font-micro-misc",
        "font-misc-ethiopic",
        "font-misc-meltho",
        "font-misc-misc",
        "font-mutt-misc",
        "font-schumacher-misc",
        "font-sony-misc",
        "font-sun-misc",
    ]

    return []


@subpackage("fonts-xorg-type1")
def _type1(self):
    self.pkgdesc = f"{pkgdesc} (type1)"
    self.depends = [
        "font-adobe-utopia-type1",
        "font-bh-type1",
        "font-bitstream-type1",
        "font-ibm-type1",
        "font-xfree86-type1",
    ]

    return []
