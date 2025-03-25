pkgname = "protontricks"
pkgver = "1.12.1"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-pillow",
    "python-setuptools",
    "python-vdf",
    "winetricks",
    "zenity",
]
checkdepends = [
    "bash",
    "python-pytest",
    *depends,
]
pkgdesc = "Winetricks wrapper for Steam games"
license = "GPL-3.0-only"
url = "https://github.com/Matoking/protontricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2f81d2faca7afc9e041c89862b375f660041a35d36554c06ba9d97d9b7ec22fe"
