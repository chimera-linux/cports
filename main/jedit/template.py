pkgname = "jedit"
# update version in patches on updates
pkgver = "5.7.0"
pkgrel = 0
prepare_after_patch = True
hostmakedepends = ["apache-ant", "docbook-xsl-nons", "openjdk17-jdk"]
depends = ["virtual:java-jre!openjdk17-jre"]
pkgdesc = "Programming text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://jedit.org"
source = f"$(SOURCEFORGE_SITE)/jedit/{pkgver}/jedit{pkgver}source.tar.bz2"
sha256 = "8e71e9fbd5e535e6164d57545f7490d3b351eac7cec6041bee14b4fc3baffdc5"
env = {
    "ANT_HOME": "/usr/share/apache-ant",
    "JAVA_HOME": "/usr/lib/jvm/java-17-openjdk",
}


def post_extract(self):
    self.cp(self.files_path / "build.properties", ".")


def prepare(self):
    # fetch dependencies separately while we have network
    self.do(
        "ant",
        "-propertyfile",
        "build.properties",
        "retrieve",
        allow_network=True,
    )


def build(self):
    self.do("ant", "-propertyfile", "build.properties", "build")
    self.do("ant", "-propertyfile", "build.properties", "docs-html")


def install(self):
    self.install_file("build/jedit.jar", "usr/share/jedit")

    for f in [
        "jars",
        "keymaps",
        "macros",
        "modes",
        "properties",
        "startup",
    ]:
        self.install_files(f"build/{f}", "usr/share/jedit")

    for x in (self.cwd / "build/doc").iterdir():
        self.install_files(x, "usr/share/doc/jedit")

    self.install_link("usr/share/jedit/doc", "../doc/jedit")

    self.install_man("package-files/linux/jedit.1")

    self.install_file(
        "package-files/linux/deb/jedit.desktop",
        "usr/share/applications",
        mode=0o755,
    )
    self.install_file("doc/jedit.png", "usr/share/icons/hicolor/128x128/apps")

    self.install_bin(self.files_path / "jedit")


@subpackage("jedit-doc")
def _(self):
    self.subdesc = "docs"

    return [
        "usr/share/doc/jedit",
    ]
