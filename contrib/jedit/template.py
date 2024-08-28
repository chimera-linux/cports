pkgname = "jedit"
# update version in patches on updates
pkgver = "5.6.0"
pkgrel = 3
prepare_after_patch = True
hostmakedepends = ["apache-ant", "docbook-xsl-nons", "openjdk17-jdk"]
depends = ["virtual:java-jre!openjdk17-jre"]
pkgdesc = "Programming text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://jedit.org"
# build.xml executes javascript and java 15 removed nashorn, so it's separate
_nashorn_ver = "15.4"
_asm_ver = "9.7"
source = [
    f"$(SOURCEFORGE_SITE)/jedit/{pkgver}/jedit{pkgver}source.tar.bz2",
    f"!https://repo1.maven.org/maven2/org/openjdk/nashorn/nashorn-core/{_nashorn_ver}/nashorn-core-{_nashorn_ver}.jar",
    f"!https://repo1.maven.org/maven2/org/ow2/asm/asm/{_asm_ver}/asm-{_asm_ver}.jar",
    f"!https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/{_asm_ver}/asm-commons-{_asm_ver}.jar",
    f"!https://repo1.maven.org/maven2/org/ow2/asm/asm-util/{_asm_ver}/asm-util-{_asm_ver}.jar",
]
sha256 = [
    "76c16ae0168d9b64ecddd8bf08aa49ab352adb2c9687191bc71895a96a8dfe1d",
    "6f816e84dfd63a81d4eaa7829c08337bbaff3ec683ff3bf6bbd90d017a00dc6f",
    "adf46d5e34940bdf148ecdd26a9ee8eea94496a72034ff7141066b3eea5c4e9d",
    "389bc247958e049fc9a0408d398c92c6d370c18035120395d4cba1d9d9304b7a",
    "37a6414d36641973f1af104937c95d6d921b2ddb4d612c66c5a9f2b13fc14211",
]
env = {
    "ANT_HOME": "/usr/share/apache-ant",
    "JAVA_HOME": "/usr/lib/jvm/java-17-openjdk",
}


def post_extract(self):
    self.cp(self.files_path / "build.properties", ".")
    self.cp(self.sources_path / f"nashorn-core-{_nashorn_ver}.jar", ".")
    self.cp(self.sources_path / f"asm-{_asm_ver}.jar", ".")
    self.cp(self.sources_path / f"asm-commons-{_asm_ver}.jar", ".")
    self.cp(self.sources_path / f"asm-util-{_asm_ver}.jar", ".")


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
