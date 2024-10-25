pkgname = "xapp-apps"
pkgver = "1"
pkgrel = 0
build_style = "meta"
depends = [
    # "blueberry", # requires an older version of gnome-bluetooth
    "bulky",
    "pix",
    # "timeshift", # FIXME: timeshift-gtk causes segmentation fault at strlen()
    "xdg-desktop-portal-xapp",
    "xed",
    "xreader",
    "xviewer",
]
pkgdesc = "Collection of X-Apps applications"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "custom:meta"
url = "https://projects.linuxmint.com/xapps"
